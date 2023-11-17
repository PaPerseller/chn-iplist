import netaddr
import requests
import logging
import math

#update chnroute-ipv6
logger = logging.getLogger(__name__)

def update_ip():
    url = 'https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
    timeout = 30
    save_to_file6 = './chnroute-ipv6.txt'

    logger.info(f'connecting to {url}')

    ipNetwork_list6 = []

    with requests.get(url, timeout=timeout) as res:
        if res.status_code != 200:
            raise Exception(f'status code :{res.status_code}')

        logger.info(f'parsing...')

        lines = res.text.splitlines()
        for line in lines:
            try:
                if line.find('|CN|ipv6|') != -1:
                    elems = line.split('|')
                    ip_start = elems[3]
                    cidr_prefix_length = elems[4]
                    ipNetwork_list6.append(netaddr.IPNetwork(f'{ip_start}/{cidr_prefix_length}\n'))
            except IndexError:
                logging.warning(f'unexpected format: {line}')

    logger.info('merging')
    ipNetwork_list6 = netaddr.cidr_merge(ipNetwork_list6)
    logger.info('writing to file')

    with open(save_to_file6, 'wt') as f:
        f.writelines([f'{x}\n' for x in ipNetwork_list6])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    update_ip()

#update chnroute-ipv4
url01 = "https://raw.githubusercontent.com/17mon/china_ip_list/master/china_ip_list.txt"

response = requests.get(url01)

if response.status_code == 200:
    with open("./china_ip_list.txt", "wb") as a_file:
        a_file.write(response.content)
else:
    print(f"文件下载失败，状态码: {response.status_code}")

url02 = "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/china.txt"

response = requests.get(url02)

if response.status_code == 200:
    with open("./china.txt", "wb") as b_file:
        b_file.write(response.content)
else:
    print(f"文件下载失败，状态码: {response.status_code}")

with open("./china_ip_list.txt", 'r') as a_file:
    a_content = a_file.read()

with open("./china.txt", 'r') as b_file:
    b_content = b_file.read()

merged_content = a_content + b_content

with open('./chnroute-ipv4.txt', 'w') as c_file:
    c_file.write(merged_content)

with open('./chnroute-ipv4.txt', 'r') as c_file:
    c_lines = c_file.readlines()

    ipNetwork_list4 = c_lines

    logger.info('merging')
    ipNetwork_list4 = netaddr.cidr_merge(ipNetwork_list4)
    logger.info('writing to file')

with open("./chnroute-ipv4.txt", 'wt') as d_file:
    for ip_network in ipNetwork_list4:
        d_file.write(str(ip_network) + "\n")

#merge v4 & v6
with open("./chnroute-ipv4.txt", 'r') as d_file:
    d_content = d_file.read()

with open('./chnroute-ipv6.txt', 'r') as e_file:
    e_content = e_file.read()

merged_content = d_content + e_content

with open('./chnroute.txt', 'w') as f_file:
    f_file.write(merged_content)