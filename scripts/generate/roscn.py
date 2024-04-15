def format_cidr(file_path, output_path):
    with open(file_path, 'r') as f:
        cidrs = [cidr.strip() for cidr in f.readlines()]

    with open(output_path, 'w') as f:
        f.write("/ip firewall address-list remove [/ip firewall address-list find list=CN]\n")
        f.write("/ip firewall address-list\n")
        f.write("add address=10.0.0.0/8 list=CN comment=private-network\n")
        f.write("add address=100.64.0.0/10 list=CN comment=private-network\n")
        f.write("add address=127.0.0.0/8 list=CN comment=private-network\n")
        f.write("add address=169.254.0.0/16 list=CN comment=private-network\n")
        f.write("add address=172.16.0.0/12 list=CN comment=private-network\n")
        f.write("add address=192.0.0.0/24 list=CN comment=private-network\n")
        f.write("add address=192.0.2.0/24 list=CN comment=private-network\n")
        f.write("add address=192.88.99.0/24 list=CN comment=private-network\n")
        f.write("add address=192.168.0.0/16 list=CN comment=private-network\n")
        f.write("add address=198.51.100.0/24 list=CN comment=private-network\n")
        f.write("add address=203.0.113.0/24 list=CN comment=private-network\n")
        f.write("add address=224.0.0.0/3 list=CN comment=private-network\n")
        f.write("\n:local cidrList {\n")
        for cidr in cidrs[:-1]:
            f.write(f'  "{cidr}"\n')
        f.write(f'  "{cidrs[-1]}"\n')
        f.write("}\n\n")
        f.write(":foreach cidr in $cidrList do={\n")
        f.write("  /ip firewall address-list add address=$cidr list=CN\n")
        f.write("}")

if __name__ == '__main__':
    format_cidr('./chnroute-ipv4.txt', './cn.rsc')