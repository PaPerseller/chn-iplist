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
          "umeng"
          "adwords",
          "duomeng",
          "guanggao"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "proxy",
        "domain" : [
          "geosite:google",
          "geosite:google-cn",
          "geosite:telegram",
          "geosite:netflix",
          "geosite:geolocation-!cn",
          "geosite:github",
          "geosite:twitter",
          "geosite:amp",
          "geosite:category-ai-chat-!cn",
          "geosite:instagram",
          "domain:assets-cdn.github.com",
          "domain:emby.wtf",
          "domain:g.whatsapp.net",
          "domain:us-west-2.amazonaws.com",
          "domain:ytimg.com",
          "domain:ggpht.com",
          "domain:humblebundle.com",
          "domain:steamcommunity-a.akamaihd.net",
          "domain:steamstore-a.akamaihd.net",
          "domain:fanatical.com",
          "domain:humblebundle.com",
          "domain:playartifact.com",
          "domain:steam-chat.com",
          "domain:steamcommunity.com",
          "domain:underlords.com",
          "v2ex"
        ],
        "type" : "field"
      },
      {
        "outboundTag" : "direct",
        "domain" : [
          "geosite:cn",
          "geosite:private",
          "geosite:bilibili",
          "geosite:apple-cn",
          "geosite:sina",
          "geosite:alibaba",
          "domain:ip6-localhost",
          "domain:ip6-loopback",
          "domain:local",
          "domain:localhost",
          "domain:cdn.jsdelivr.net",
          "moutai",
          "weixin",
          "announce",
          "torrent",
          "tracker",
          "domain:steamcdn-a.akamaihd.net",
          "domain:cm.steampowered.com",
          "domain:steamserver.net",
          "domain:cdn.mileweb.cs.steampowered.com.8686c.com",
          "domain:cdn-ws.content.steamchina.com",
          "domain:cdn-qc.content.steamchina.com",
          "domain:cdn-ali.content.steamchina.com",
          "domain:epicgames-download1-1251447533.file.myqcloud.com",
          "domain:dl.steam.clngaa.com",
          "domain:dl.steam.ksyna.com",
          "domain:st.dl.bscstorage.net",
          "domain:st.dl.eccdnx.com",
          "domain:st.dl.pinyuncloud.com",
          "domain:steampipe.steamcontent.tnkjmec.com",
          "domain:steampowered.com.8686c.com",
          "domain:steamstatic.com.8686c.com",
          "domain:wmsjsteam.com",
          "domain:xz.pphimalayanrt.com",
          "domain:cm.steampowered.com",
          "domain:steamcontent.com",
          "domain:steamusercontent.com"
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
          "205.185.194.0/24",
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