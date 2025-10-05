import netaddr
import requests
import logging
import math

logger = logging.getLogger(__name__)


def update_ip():
    url = 'https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
    timeout = 30
    save_to_file = './chnroute.txt'
    save_to_file4 = './chnroute-ipv4.txt'
    save_to_file6 = './chnroute-ipv6.txt'


    logger.info(f'connecting to {url}')

    ipNetwork_list = []
    ipNetwork_list4 = []
    ipNetwork_list6 = []

    with requests.get(url, timeout=timeout) as res:
        if res.status_code != 200:
            raise Exception(f'status code :{res.status_code}')

        logger.info(f'parsing...')

        lines = res.text.splitlines()
        for line in lines:
            try:
                if line.find('|CN|ipv4|') != -1:
                    elems = line.split('|')
                    ip_start = elems[3]
                    count = int(elems[4])
                    cidr_prefix_length = int(32 - math.log(count, 2))
                    ipNetwork_list.append(netaddr.IPNetwork(f'{ip_start}/{cidr_prefix_length}\n'))
                    ipNetwork_list4.append(netaddr.IPNetwork(f'{ip_start}/{cidr_prefix_length}\n'))

                if line.find('|CN|ipv6|') != -1:
                    elems = line.split('|')
                    ip_start = elems[3]
                    cidr_prefix_length = elems[4]
                    ipNetwork_list.append(netaddr.IPNetwork(f'{ip_start}/{cidr_prefix_length}\n')) 
                    ipNetwork_list6.append(netaddr.IPNetwork(f'{ip_start}/{cidr_prefix_length}\n'))
            except IndexError:
                logging.warning(f'unexpected format: {line}')

    logger.info('merging')
    ipNetwork_list = netaddr.cidr_merge(ipNetwork_list)
    ipNetwork_list4 = netaddr.cidr_merge(ipNetwork_list4)
    ipNetwork_list6 = netaddr.cidr_merge(ipNetwork_list6)
    logger.info('writing to file')

    with open(save_to_file, 'wt') as f:
        f.writelines([f'{x}\n' for x in ipNetwork_list])

    with open(save_to_file4, 'wt') as f:
        f.writelines([f'{x}\n' for x in ipNetwork_list4])

    with open(save_to_file6, 'wt') as f:
        f.writelines([f'{x}\n' for x in ipNetwork_list6])

    logger.info('all done')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    update_ip()