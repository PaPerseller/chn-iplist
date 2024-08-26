import netaddr
import requests

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
    return [netaddr.IPNetwork(line.strip()) for line in requests.get(url).text.splitlines()]

def merge_and_sort_networks(networks1, networks2):
    print('Merging and sorting networks...')
    return netaddr.cidr_merge(networks1 + networks2)

def write_to_file(networks, filename):
    print(f'Writing to {filename}...')
    with open(filename, 'wt') as f:
        for network in networks:
            f.write(str(network) + "\n")

if __name__ == '__main__':
    # Parse and merge IPv6 networks
    ipv6_networks = parse_and_merge_ip('https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest')
    write_to_file(ipv6_networks, './chnroute-ipv6.txt')

    # Download and parse IPv4 networks
    china_ip_list = download_and_parse("https://raw.githubusercontent.com/17mon/china_ip_list/master/china_ip_list.txt")
    china_txt = download_and_parse("https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/china.txt")

    # Merge and sort IPv4 networks
    ipv4_networks = merge_and_sort_networks(china_ip_list, china_txt)
    write_to_file(ipv4_networks, './chnroute-ipv4.txt')

    # Merge IPv4 and IPv6 networks
    all_networks = merge_and_sort_networks(ipv4_networks, ipv6_networks)
    write_to_file(all_networks, './chnroute.txt')
