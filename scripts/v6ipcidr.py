# 列出每个行的文本
with open("./chnroute-ipv6.txt", "r") as input_file:
    lines = input_file.readlines()

# 定义要添加的文本
before_text = "IP-CIDR,"
after_text = ",no-resolve"

# 将特定内容添加到每行文本前后
new_lines = []
for line in lines:
    new_line = before_text + line.strip() + after_text + "\n"
    new_lines.append(new_line)

# 将修改后的文本写回文件
with open("./ipv6.list", "w") as output_file:
    output_file.writelines(new_lines)
