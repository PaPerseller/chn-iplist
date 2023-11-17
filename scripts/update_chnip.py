import netaddr
import requests
import logging

logger = logging.getLogger(__name__)

def download_from_url(url, file_path):
    response = requests.get(url)
    if response.status_code != 200:
        logger.error(f"文件下载失败，状态码: {response.status_code}")
        return False

    with open(file_path, "wb") as file:
        file.write(response.content)
    return True

def parse_and_merge_ip(url, save_to_file):
    logger.info(f'connecting to {url}')

    ipNetwork_list = []

    with requests.get(url) as res:
        if res.status_code != 200:
            logger.error(f'status code :{res.status_code}')
            return

        logger.info(f'parsing...')

        lines = res.text.splitlines()
        for line in lines:
            try:
                if '|CN|ipv6|' in line:
                    elems = line.split('|')
                    ip_start = elems[3]
                    cidr_prefix_length = elems[4]
                    ipNetwork_list.append(netaddr.IPNetwork(f'{ip_start}/{cidr_prefix_length}\n'))
            except IndexError:
                logger.warning(f'unexpected format: {line}')

    logger.info('merging')
    ipNetwork_list = netaddr.cidr_merge(ipNetwork_list)
    logger.info('writing to file')

    with open(save_to_file, 'wt') as f:
        f.writelines([f'{x}\n' for x in ipNetwork_list])

def merge_files(file1, file2, output):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
        out.write(f1.read() + f2.read())

def sort_ip(file_path):
    with open(file_path, 'r') as f:
        ipNetwork_list = f.readlines()

    logger.info('merging')
    ipNetwork_list = netaddr.cidr_merge(ipNetwork_list)
    logger.info('writing to file')

    with open(file_path, 'wt') as f:
        for ip_network in ipNetwork_list:
            f.write(str(ip_network) + "\n")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parse_and_merge_ip('https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest', './chnroute-ipv6.txt')

    if download_from_url("https://raw.githubusercontent.com/17mon/china_ip_list/master/china_ip_list.txt", "./china_ip_list.txt") and \
        download_from_url("https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/china.txt", "./china.txt"):
        merge_files("./china_ip_list.txt", "./china.txt", "./chnroute-ipv4.txt")
        sort_ip("./chnroute-ipv4.txt")

    merge_files("./chnroute-ipv4.txt", './chnroute-ipv6.txt', './chnroute.txt')
