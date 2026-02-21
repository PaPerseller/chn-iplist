import re

def extract_domains(input_file):
    domains = set()
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith(('DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD')):
                match = re.match(r'^(DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD)\s*,\s*([^\s]+)', line)
                if match:
                    domains.add(match.group(2))
    return domains

def extract_dot_domains(input_file):
    domains = set()
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                if line.startswith('.'):
                    domains.add(line[1:])
                else:
                    domains.add(line)
    return domains

def save_domains(domains, output_file):
    sorted_domains = sorted(domains)
    with open(output_file, 'w', encoding='utf-8') as file:
        for domain in sorted_domains:
            file.write(domain + '\n')

# 处理 direct-special.list
direct_domains = extract_domains('./ruleset/direct-special.list')
save_domains(direct_domains, './scripts/generate/pac/direct-domains.txt')

# 处理 proxy-special.list
proxy_domains = extract_domains('./ruleset/proxy-special.list')

# 处理 proxy-ai.list，并将提取的域名合并到 proxy_domains 集合中
ai_domains = extract_dot_domains('./ruleset/proxy-ai.list')
proxy_domains.update(ai_domains)

# 保存合并并排序后的 proxy_domains
save_domains(proxy_domains, './scripts/generate/pac/proxy-domains.txt')