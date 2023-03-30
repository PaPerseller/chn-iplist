before_text = 'add address='
after_text = ' list=CN'

with open("./chnroute-ipv4.txt", "r") as input_file:
    lines = input_file.readlines()

new_lines = []
for line in lines:
    new_line = before_text + line.strip() + after_text + "\n"
    new_lines.append(new_line)

header = ['/ip firewall address-list remove [/ip firewall address-list find list=CN]\n', '/ip firewall address-list\n','add address=192.168.0.0/16 list=CN comment=private-network\n','add address=10.0.0.0/8 list=CN comment=private-network\n']
header.extend(new_lines)

with open("./cn.rsc", "w") as output_file:
    output_file.writelines(header)