a_content = '''  "routing" : {
    "domainStrategy" : "IPIfNonMatch",
    "rules" : [
      {
        "outboundTag" : "block",
        "domain" : [
          "geosite:category-ads-all",
          "domain:ads.fmdisk.com",
          "domain:ads.feemoo.com",
          "domain:ads.google.com",
          "domain:afd.l.google.com",
          "domain:mobileads.google.com",
          "googleads",
          "umeng",
          "adnyg",
          "adwords",
          "duomeng",
          "guanggao"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "proxy",
        "domain" : [
          "geosite:netflix",
          "geosite:telegram",
          "geosite:geolocation-!cn",
          "geosite:appledaily",
          "geosite:github",
          "geosite:twitter",
          "geosite:amp",
          "domain:ytimg.com",
          "domain:ggpht.com",
          "domain:humblebundle.com",
          "domain:g.whatsapp.net",
          "domain:us-west-2.amazonaws.com",
          "t.me",
          "tdesktop.com",
          "instagram",
          "v2ex"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "direct",
        "domain" : [
          "geosite:cn",
          "domain:softpedia.com",
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