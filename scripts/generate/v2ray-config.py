a_content = '''  "routing" : {
    "domainStrategy" : "IPIfNonMatch",
    "rules" : [
      {
        "outboundTag" : "direct",
        "ip" : [
          "geoip:private",
          "::1/128",
          "fc00::/7",
          "fe80::/10",
          "fd00::/8"
        ],
        "type" : "field"
      },
      {
        "outboundTag": "direct",
        "protocol": [
          "bittorrent"
        ],
        "type": "field"
      },
      {
        "outboundTag" : "block",
        "domain" : [
          "domain:ads.fmdisk.com",
          "domain:ads.feemoo.com",
          "domain:ads.google.com",
          "domain:afd.l.google.com",
          "domain:mobileads.google.com",
          "googleads",
          "umeng"
          "adwords",
          "duomeng",
          "guanggao",
          "geosite:category-ads-all",
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "direct",
        "domain" : [
          "domain:ip6-localhost",
          "domain:ip6-loopback",
          "domain:local",
          "domain:localhost",
          "domain:cdn.jsdelivr.net",
          "domain:gh-proxy.com",
          "domain:cdn.jsdelivr.net",
          "moutai",
          "weixin",
          "announce",
          "torrent",
          "tracker"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "proxy",
        "domain" : [
          "domain:assets-cdn.github.com",
          "domain:emby.wtf",
          "domain:g.whatsapp.net",
          "domain:us-west-2.amazonaws.com",
          "domain:ytimg.com",
          "domain:v2ex.com",
          "domain:ggpht.com",
          "geosite:google-cn",
          "domain:fanatical.com",
          "domain:humblebundle.com",
          "domain:underlords.com",
          "domain:valvesoftware.com",
          "domain:playartifact.com",
          "domain:steam-chat.com",
          "domain:steamcommunity.com",
          "domain:steamgames.com",
          "domain:steamstatic.com",
          "domain:steamstat.us",
          "domain:steambroadcast.akamaized.net",
          "domain:steamcommunity-a.akamaihd.net",
          "domain:steamstore-a.akamaihd.net",
          "domain:steamusercontent-a.akamaihd.net",
          "domain:steamuserimages-a.akamaihd.net",
          "domain:steampipe.akamaized.net"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "direct",
        "domain" : [
          "geosite:private",
          "geosite:bilibili",
          "geosite:apple-cn",
          "geosite:category-ai-cn",
          "geosite:sina",
          "geosite:alibaba",
          "geosite:steam@cn",
          "geosite:category-game-platforms-download@cn",
          "geosite:category-games@cn",
          "geosite:cn"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "proxy",
        "domain" : [
          "geosite:google",
          "geosite:telegram",
          "geosite:netflix",
          "geosite:github",
          "geosite:twitter",
          "geosite:amp",
          "geosite:category-ai-!cn",
          "geosite:instagram",
          "geosite:geolocation-!cn"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "proxy",
        "ip" : [
          "geoip:telegram",
          "geoip:twitter"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "direct",
        "ip" : [
          "45.121.184.0/24",
          "103.10.124.0/23",
          "103.28.54.0/24",
          "146.66.152.0/24",
          "146.66.155.0/24",
          "153.254.86.0/24",
          "155.133.224.0/22",
          "155.133.230.0/24",
          "155.133.232.0/23",
          "155.133.234.0/24",
          "155.133.236.0/22",
          "155.133.240.0/23",
          "155.133.244.0/23",
          "155.133.246.0/24",
          "155.133.248.0/21",
          "162.254.192.0/21",
          "185.25.182.0/23",
          "190.217.32.0/22",
          "192.69.96.0/22",
          "205.196.6.0/24",
          "208.64.200.0/22",
          "208.78.164.0/22",
          "205.185.194.0/24",'''

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