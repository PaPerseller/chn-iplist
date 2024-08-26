a_content = r'''# 默认代理
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

c_content = r'''
[proxy_list]
# 代理关键词
(^|\.)\w*gmail\w*\.\w*$
(^|\.)\w*google\w*\.\w*$
(^|\.)\w*gstatic\w*\.\w*$
(^|\.)\w*youtube\w*\.\w*$
(^|\.)\w*appledaily\w*\.\w*$
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
