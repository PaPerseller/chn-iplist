# roscn.rsc
with open("./chnroute-ipv4.txt", "r") as input_file:
    lines = input_file.readlines()

before_text = 'add address='
after_text = ' list=CN'

new_lines = []
for line in lines:
    new_line = before_text + line.strip() + after_text + "\n"
    new_lines.append(new_line)

header = ['/ip firewall address-list remove [/ip firewall address-list find list=CN]\n', '/ip firewall address-list\n','add address=192.168.0.0/16 list=CN comment=private-network\n','add address=10.0.0.0/8 list=CN comment=private-network\n']
header.extend(new_lines)

with open("./roscn.rsc", "w") as output_file:
    output_file.writelines(header) 

# ipv6cidr
with open("./chnroute-ipv6.txt", "r") as input_file:
    lines = input_file.readlines()

before_text = 'IP-CIDR,'
after_text = ',no-resolve'

new_lines = []
for line in lines:
    new_line = before_text + line.strip() + after_text + "\n"
    new_lines.append(new_line)

header = ['# 适用于 shadowrocket 等 ipv6 规则前缀为 IP-CIDR 的应用\n']
header.extend(new_lines)

with open("./ipv6.list", "w") as output_file:
    output_file.writelines(header)

# ipv6cidr6
with open("./chnroute-ipv6.txt", "r") as input_file:
    lines = input_file.readlines()

before_text = 'IP-CIDR6,'
after_text = ',no-resolve'

new_lines = []
for line in lines:
    new_line = before_text + line.strip() + after_text + "\n"
    new_lines.append(new_line)

header = ['# 适用于 Loon、clash 等 ipv6 规则前缀为 IP-CIDR6 的应用\n']
header.extend(new_lines)

with open("./Loon/ruleset/ipv6.list", "w") as output_file:
    output_file.writelines(header)

# acl
a_content = '''# 默认代理
[proxy_all]

# 直连列表
[bypass_list]

# 直连域名
(^|\.)fonts.googleapis\.com$
(^|\.)fonts.gstatic\.com$
(^|\.)softpedia\.com$
(^|\.)mtalk.google\.com$

# 局域网
^(.*\.)?local$
^(.*\.)?localhost$
^(.*\.)?ip6-localhost$
^(.*\.)?ip6-loopback$
:ffff:0:0:0:0/1
:ffff:128:0:0:0/1
::1/128
fc00::/7
fe80::/10
fd00::/8
0.0.0.0/8
10.0.0.0/8
100.64.0.0/10
127.0.0.0/8
169.254.0.0/16
172.16.0.0/12
192.0.0.0/29
192.0.2.0/24
192.88.99.0/24
192.168.0.0/16
199.168.0.0/15
198.51.100.0/24
203.0.113.0/24
224.0.0.0/3

# 国内ip地址
'''

c_content = '''
[proxy_list]
# 代理关键词
(^|\.)\w*gmail\w*\.\w*$
(^|\.)\w*google\w*\.\w*$
(^|\.)\w*gstatic\w*\.\w*$
(^|\.)\w*youtube\w*\.\w*$
(^|\.)\w*appledaily\w*\.\w*$
(^|\.)\w*github\w*\.\w*$
(^|\.)\w*instagram\w*\.\w*$
(^|\.)\w*twitter\w*\.\w*$
(^|\.)\w*twimg\w*\.\w*$
(^|\.)\w*telegram\w*\.\w*$
(^|\.)\w*steam\w*\.\w*$
(^|\.)\w*v2ex\w*\.\w*$'''

with open("./chnroute.txt", 'r') as b_file:
    b_content = b_file.read()

merged_content = a_content + b_content + "\n" + c_content

with open('./chn.acl', 'w') as output_file:
        output_file.write(merged_content)

# v2ray-config
a_content = '''  "routing" : {
    "domainStrategy" : "IPOnDemand",
    "rules" : [
      {
        "outboundTag" : "block",
        "domain" : [
          "geosite:category-ads-all",
          "domain:xcz.im",
          "domain:ads.fmdisk.com",
          "domain:ads.feemoo.com",
          "domain:ads.google.com",
          "domain:afd.l.google.com",
          "domain:mobileads.google.com",
          "domain:g1.tagtic.cn",
          "domain:log.tagtic.cn",
          "domain:pgdt.ugdtimg.com",
          "domain:sdownload.stargame.com",
          "domain:wwads.cn",
          "domain:gzads.com",
          "domain:gozendata.com",
          "domain:gz-data.com",
          "googleads",
          "pagead",
          "umeng",
          "adnyg",
          "admarvel",
          "admaster",
          "adsage",
          "adsmogo",
          "adsrvmedia",
          "adwords",
          "adservice",
          "adsserving",
          "analysis",
          "analytics",
          "applovin",
          "domob",
          "duomeng",
          "dwtrack",
          "guanggao",
          "lianmeng",
          "monitor",
          "omgmta",
          "openx",
          "partnerad",
          "pingfore",
          "socdm",
          "supersonicads",
          "tracking",
          "uedas",
          "usage",
          "wlmonitor",
          "zjtoolbar",
          "adsrvr",
          "gdt"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "proxy",
        "domain" : [
          "geosite:github",
          "geosite:netflix",
          "geosite:telegram",
          "geosite:geolocation-!cn",
          "geosite:appledaily",
          "geosite:github",
          "geosite:twitter",
          "geosite:amp",
          "domain:googleapis.cn",
          "domain:ytimg.com",
          "domain:ggpht.com",
          "domain:humblebundle.com",
          "domain:analytics.twitter.com",
          "domain:g.whatsapp.net",
          "domain:us-west-2.amazonaws.com",
          "t.me",
          "tdesktop.com",
          "instagram",
          "twimg",
          "steam",
          "v2ex"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "direct",
        "domain" : [
          "geosite:cn",
          "domain:fonts.googleapis.com",
          "domain:fonts.gstatic.com",
          "domain:softpedia.com",
          "domain:mtalk.google.com",
          "domain:ip6-localhost",
          "domain:ip6-loopback",
          "domain:local",
          "domain:localhost"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "proxy",
        "ip" : [
          "geoip:telegram"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "direct",
        "ip" : [
          "geoip:private",
          "::1/128",
          "fc00::/7",
          "fe80::/10",
          "fd00::/8",'''

c_content = '''
        ],
        "type" : "field"
      }
    ]
  }，'''

with open("./chnroute.txt", "r") as b_file:
        lines= b_file.readlines()

before_text = "          \""
after_text = "\","

new_lines = []
for line in lines:
    new_line = before_text + line.strip() + after_text + "\n"
    new_lines.append(new_line)

b2_content = ''
for line in new_lines:
  b2_content += line
b1_content = b2_content.rstrip()
b_content = b1_content[:-1]

new_content = a_content + "\n" + b_content + c_content

with open('./v2ray-config_rule.json', 'w') as output_file:
    output_file.write(new_content)