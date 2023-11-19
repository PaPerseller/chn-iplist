import netaddr
import requests
import os

def download_from_url(url, file_path):
    with open(file_path, "wb") as file:
        file.write(requests.get(url).content)

def parse_and_merge_ip(url, save_to_file):
    print(f'Connecting to {url}...')

    ipNetwork_list = []

    lines = requests.get(url).text.splitlines()
    for line in lines:
        if '|CN|ipv6|' in line:
            elems = line.split('|')
            ip_start = elems[3]
            cidr_prefix_length = elems[4]
            ipNetwork_list.append(netaddr.IPNetwork(f'{ip_start}/{cidr_prefix_length}\n'))

    ipNetwork_list = netaddr.cidr_merge(ipNetwork_list)

    with open(save_to_file, 'wt') as f:
        f.writelines([f'{x}\n' for x in ipNetwork_list])

def merge_and_sort_files(file1, file2, output):
    print('Merging and sorting files...')
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        ipNetwork_list = f1.readlines() + f2.readlines()
        
    ipNetwork_list = netaddr.cidr_merge([netaddr.IPNetwork(x) for x in ipNetwork_list])
    with open(output, 'wt') as f:
        for ip_network in ipNetwork_list:
            f.write(str(ip_network) + "\n")

def cleanup(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted file: {file}")

if __name__ == '__main__':
    parse_and_merge_ip('https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest', './chnroute-ipv6.txt')

    download_from_url("https://raw.githubusercontent.com/17mon/china_ip_list/master/china_ip_list.txt", "./china_ip_list.txt")
    download_from_url("https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/china.txt", "./china.txt")

    merge_and_sort_files("./china_ip_list.txt", "./china.txt", "./chnroute-ipv4.txt")
    merge_and_sort_files("./chnroute-ipv4.txt", './chnroute-ipv6.txt', './chnroute.txt')

    # Clean up downloaded files
    cleanup(["./china_ip_list.txt", "./china.txt"])
