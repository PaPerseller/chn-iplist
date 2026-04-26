import re
import urllib.request
from urllib.parse import urlparse

def get_lines(source):
    """
    统一的数据读取接口，支持本地文件路径和远程HTTP(S)链接
    """
    parsed = urlparse(source)
    if parsed.scheme in ('http', 'https'):
        print(f"Downloading and reading remote file: {source}")
        # 添加 User-Agent 头，防止部分平台拦截默认的 Python UA
        req = urllib.request.Request(source, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8')
            for line in content.splitlines():
                yield line
    else:
        print(f"Reading local file: {source}")
        with open(source, 'r', encoding='utf-8') as file:
            for line in file:
                yield line

def extract_domains(sources):
    """
    从文件或链接列表中提取 RULE-SET 规则格式 (DOMAIN,xxx 等)
    """
    domains = set()
    for source in sources:
        for line in get_lines(source):
            line = line.strip()
            if line.startswith(('DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD')):
                match = re.match(r'^(DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD)\s*,\s*([^\s]+)', line)
                if match:
                    domains.add(match.group(2))
    return domains

def extract_dot_domains(sources):
    """
    从文件或链接列表中提取 DOMAIN-SET 域名格式
    """
    domains = set()
    for source in sources:
        for line in get_lines(source):
            line = line.strip()
            # 忽略空行和注释行
            if line and not line.startswith('#'):
                if line.startswith('.'):
                    domains.add(line[1:])
                else:
                    domains.add(line)
    return domains

def save_domains(domains, output_file):
    sorted_domains = sorted(domains)
    with open(output_file, 'w', encoding='utf-8') as file:
        for domain in sorted_domains:
            file.write(domain + '\n')


# === 1. 处理直连规则 ===

# 1.1 DOMAIN,xxx 格式来源
direct_sources = [
    './ruleset/direct-special.list'
]
direct_domains = extract_domains(direct_sources)

# 1.2 纯域名 / 以点开头的格式来源
direct_extra_sources = [
    'https://raw.githubusercontent.com/PaPerseller/extra-ruleset/refs/heads/main/ruleset/direct-game.list',
    'https://raw.githubusercontent.com/PaPerseller/extra-ruleset/refs/heads/main/ruleset/direct-cdn.list'
    # 未来如果有更多相同格式的来源，直接按格式加在下面
]
direct_extra_domains = extract_dot_domains(direct_extra_sources)

# 将两类格式提取出的直连域名进行合并并去重
direct_domains.update(direct_extra_domains)

# 保存最终合并并排序后的 direct_domains
save_domains(direct_domains, './scripts/generate/pac/direct-domains.txt')


# === 2. 处理代理规则 ===

# 2.1 DOMAIN,xxx 格式来源
proxy_special_sources = [
    './ruleset/proxy-special.list'
]
proxy_domains = extract_domains(proxy_special_sources)

# 2.2 纯域名 / 以点开头的格式来源
proxy_extra_sources =[
    'https://raw.githubusercontent.com/PaPerseller/extra-ruleset/refs/heads/main/ruleset/proxy-ai.list'
    # 未来如果有更多相同格式的来源，直接按格式加在下面，例如：
    # 'https://raw.githubusercontent.com/xxx/yyy/main/another-list.txt'
]
extra_domains = extract_dot_domains(proxy_extra_sources)

# 将两类格式提取出的代理域名进行合并并去重
proxy_domains.update(extra_domains)

# 保存最终合并并排序后的 proxy_domains
save_domains(proxy_domains, './scripts/generate/pac/proxy-domains.txt')

print("Domains extracted and saved successfully.")