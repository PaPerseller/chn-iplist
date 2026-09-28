import argparse
import os
import re
import time

import netaddr
import requests
import yaml

# 中国 IPv4 数据源：合并 metowolf 内地列表与 china-operator-ip 的 china.txt
METOWOLF_CHINA_IPV4_URL = 'https://metowolf.github.io/iplist/data/special/china.txt'
GAOYIFAN_CHINA_IPV4_URL = 'https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/china.txt'
# 排除规则配置仍来自 china-operator-ip 项目
OPERATORS_YAML_URL = 'https://raw.githubusercontent.com/gaoyifan/china-operator-ip/master/operators.yaml'
# RIPEstat 公告前缀 API：用于将 exclude_asn 中的 ASN 解析为具体前缀
RIPESTAT_PREFIX_URL = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS{asn}'

def parse_and_merge_ip(url):
    print(f'Connecting to {url}...')
    ipNetwork_list = []
    lines = requests.get(url).text.splitlines()
    for line in lines:
        if '|CN|ipv6|' in line:
            elems = line.split('|')
            ip_start = elems[3]
            cidr_prefix_length = elems[4]
            ipNetwork_list.append(netaddr.IPNetwork(f'{ip_start}/{cidr_prefix_length}'))
    return netaddr.cidr_merge(ipNetwork_list)

def download_and_parse(url):
    print(f'Downloading from {url}...')
    if os.path.isfile(url):
        with open(url, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
    else:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        lines = resp.text.splitlines()
    return [netaddr.IPNetwork(line.strip()) for line in lines if line.strip() and not line.lstrip().startswith('#')]

def merge_and_sort_networks(networks1, networks2):
    print('Merging and sorting networks...')
    return netaddr.cidr_merge(networks1 + networks2)

def write_to_file(networks, filename):
    print(f'Writing to {filename}...')
    with open(filename, 'wt') as f:
        for network in networks:
            f.write(str(network) + "\n")

def get_exclude_asn(source):
    """读取 operators.yaml 中所有 operator 的排除 ASN。

    source 为本地文件路径或 URL。文件获取/解析失败时直接退出，避免排除逻辑
    静默失效；除各 operator 的 ``exclude_asn`` 外，googlecn 当前以
    ``AS24424`` pattern 表示，脚本也会从该 pattern 中提取 ASN，并统一去重。
    """
    if os.path.isfile(source):
        with open(source, 'r', encoding='utf-8') as f:
            raw = f.read()
    else:
        print(f'Downloading operators.yaml from {source}...')
        resp = requests.get(source, timeout=30)
        resp.raise_for_status()
        raw = resp.text
    cfg = yaml.safe_load(raw)
    operators = cfg['operators']
    exclude_asn = []
    for operator_name, operator_cfg in operators.items():
        operator_exclude_asn = [str(asn) for asn in operator_cfg.get('exclude_asn', [])]
        if operator_exclude_asn:
            print(f'operators.{operator_name}: 纳入排除 ASN {", ".join(f"AS{asn}" for asn in operator_exclude_asn)}')
            exclude_asn.extend(operator_exclude_asn)

    # googlecn 没有 exclude_asn 字段，而是通过 pattern 标识其 ASN；
    # 将 pattern 中的 AS<数字> 作为排除 ASN，避免硬编码 AS24424。
    googlecn_pattern = operators.get('googlecn', {}).get('pattern', '')
    googlecn_asn = re.findall(r'(?i)\bAS(\d+)\b', googlecn_pattern)
    if googlecn_asn:
        print(f'operators.googlecn: 纳入排除 ASN {", ".join(f"AS{asn}" for asn in googlecn_asn)}')
    else:
        print('WARNING> operators.googlecn.pattern 中未找到 ASN，本次跳过 googlecn 排除')

    merged_asn = list(dict.fromkeys(exclude_asn + googlecn_asn))
    if not merged_asn:
        print('WARNING> 未配置任何排除 ASN，本次跳过排除')
    return merged_asn


def fetch_asn_ipv4_prefixes(asn):
    """获取单个 ASN 当前公告的 IPv4 前缀列表（RIPEstat，RIS 观测数据）。

    仅收集 IPv4：排除规则只作用于 IPv4 合并结果，IPv6 保持 APNIC 数据原样。
    请求失败时指数退避重试 3 次，仍失败返回 None，由调用方决定是否跳过该 ASN。
    """
    url = RIPESTAT_PREFIX_URL.format(asn=asn)
    for attempt in range(3):
        try:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            prefixes = data.get('data', {}).get('prefixes') or []
            # 仅保留 IPv4 前缀（IPv6 地址必然含冒号，据此过滤）
            return [item['prefix'] for item in prefixes if ':' not in item['prefix']]
        except Exception as exc:
            if attempt < 2:
                time.sleep(2 ** attempt)
            else:
                print(f'WARNING> 获取 AS{asn} 前缀失败: {exc}')
    return None


def build_excluded_ipv4_set(asns):
    """把 exclude_asn 列表转换为对应的 IPv4 前缀集合。

    单个 ASN 拉取失败仅告警并跳过，避免偶发网络问题阻断整次更新。
    """
    excluded = netaddr.IPSet()
    for asn in asns:
        prefixes = fetch_asn_ipv4_prefixes(asn)
        if prefixes is None:
            print(f'WARNING> AS{asn} 前缀不可用，跳过该 ASN')
            continue
        excluded = excluded | netaddr.IPSet(prefixes)
        print(f'AS{asn}: 排除 {len(prefixes)} 个 IPv4 前缀')
    if not excluded:
        print('WARNING> 排除前缀集合为空，本次不会移除任何前缀')
    return excluded


def main():
    parser = argparse.ArgumentParser(description='生成并合并去重 chnroute IP 列表')
    parser.add_argument('--operators-yaml',
                        default=os.environ.get('CHINA_OPERATOR_IP_YAML', OPERATORS_YAML_URL),
                        help='china-operator-ip operators.yaml 的本地路径或 URL')
    parser.add_argument('--metowolf-china-ip-list',
                        default=os.environ.get('METOWOLF_CHINA_IPV4_SOURCE', METOWOLF_CHINA_IPV4_URL),
                        help='metowolf special/china.txt 的本地路径或 URL')
    parser.add_argument('--gaoyifan-china-ip-list',
                        default=os.environ.get('GAOYIFAN_CHINA_IPV4_SOURCE', GAOYIFAN_CHINA_IPV4_URL),
                        help='gaoyifan/china.txt 的本地路径或 URL')
    parser.add_argument('--skip-exclude', action='store_true',
                        help='跳过 operators.yaml/RIPEstat 排除步骤，适用于仅有 ip-lists 分支文件的本地合并')
    args = parser.parse_args()

    exclude_asn = [] if args.skip_exclude else get_exclude_asn(args.operators_yaml)
    excluded_v4 = build_excluded_ipv4_set(exclude_asn) if exclude_asn else netaddr.IPSet()

    # Parse and merge IPv6 networks
    ipv6_networks = parse_and_merge_ip('https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest')
    write_to_file(ipv6_networks, './chnroute-ipv6.txt')

    # Download and parse IPv4 networks
    metowolf_china = download_and_parse(args.metowolf_china_ip_list)
    gaoyifan_china = download_and_parse(args.gaoyifan_china_ip_list)

    # Merge and sort IPv4 networks
    ipv4_networks = merge_and_sort_networks(metowolf_china, gaoyifan_china)

    # 剔除放在合并之后，确保排除规则同时作用于两个 IPv4 数据源。
    if excluded_v4:
        before = len(ipv4_networks)
        ipv4_networks = list((netaddr.IPSet(ipv4_networks) - excluded_v4).iter_cidrs())
        excluded_count = len(list(excluded_v4.iter_cidrs()))
        print(f'Excluded {excluded_count} IPv4 prefixes, lines {before} -> {len(ipv4_networks)}')
    write_to_file(ipv4_networks, './chnroute-ipv4.txt')

    # Merge IPv4 and IPv6 networks
    all_networks = merge_and_sort_networks(ipv4_networks, ipv6_networks)
    write_to_file(all_networks, './chnroute.txt')


if __name__ == '__main__':
    main()
