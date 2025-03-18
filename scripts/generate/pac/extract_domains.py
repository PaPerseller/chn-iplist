import re

def extract_domains(input_file):
    domains = set()  # 使用集合来避免重复
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith(('DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD')):
                # 使用正则表达式提取域名部分
                match = re.match(r'^(DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD)\s*,\s*([^\s]+)', line)
                if match:
                    domains.add(match.group(2))
    return sorted(domains)  # 返回排序后的域名列表

def save_domains(domains, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for domain in domains:
            file.write(domain + '\n')

# 处理 direct-special.list
direct_domains = extract_domains('./ruleset/direct-special.list')
save_domains(direct_domains, './scripts/generate/pac/direct-domains.txt')

# 处理 proxy-special.list
proxy_domains = extract_domains('./ruleset/proxy-special.list')
save_domains(proxy_domains, './scripts/generate/pac/proxy-domains.txt')
