before_text = 'IP-CIDR,'
after_text = ',no-resolve'

with open("./chnroute-ipv6.txt", "r") as input_file:
    lines = input_file.readlines()

new_lines = []
for line in lines:
    new_line = before_text + line.strip() + after_text + "\n"
    new_lines.append(new_line)

header = ['# 适用于 shadowrocket 等 ipv6 规则前缀为 IP-CIDR 的应用\n']
header.extend(new_lines)

with open("./ruleset/ipv6-cidr.list", "w") as output_file:
    output_file.writelines(header)