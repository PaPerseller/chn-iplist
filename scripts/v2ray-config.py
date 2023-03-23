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