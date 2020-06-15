# chn-iplist

数据来源 [ APNIC Delegated List](http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest)，将其转化为 txt 文件以在路由器上使用，并以此制作 Shadowrocket、Quantumult、Kitsunebi、acl、BifrostV、v2rayNG、clash、pac 规则和 v2ray 配置内嵌规则，仅包含 chn-ip 列表及部分谷歌和国内常见广告屏蔽规则。每月更新一次。

### Subscribe URL:

chnroute.txt: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.txt

Shadowrocket: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Shadowrocket.conf

Quantumult: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult.conf

Quantumult(X) (no chn-ip) : https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult(X)_noIP.conf

Kitsunebi: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Kitsunebi.conf

Kitsunebi-android: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Kitsunebi-android.conf

acl (no ban ads) : https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chn.acl

acl (ban ads) : https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chn_banad.acl

pac: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.pac  （默认非 chn-ip 网站走 socks5 localhost:1080 代理）

clash 远程配置(test): https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/clash/pref.ini

### 需手动更新：

BifrostV：在[相关文件夹](https://github.com/PaPerseller/chn-iplist/tree/master/BifrostV)下按规则类型复制粘贴至应用内。

v2ray 配置内嵌规则，将[规则文本](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2ray-config_rule.txt)加入配置文件 routing 对应区域。域名解析策略自行选择。

v2rayNG ：分别将[proxy](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayNG/proxy.txt)、[direct](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayNG/direct.txt)、 [block](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayNG/block.txt) 规则复制粘贴至应用内。

clash：https://github.com/PaPerseller/chn-iplist/blob/master/clash/clash.yml 

clash (no chn-ip)：https://github.com/PaPerseller/chn-iplist/blob/master/clash/clash_noIP.yml

### PS.

1. v2rayNG 规则可与 pc 客户端 v2rayN 通用。 
2. 已加入 ipv6 列表的规则：chnroute.txt、chnroute.pac、chn.acl、clash、v2rayNG、Kitsunebi-android、shadowrocket
3. Kitsunebi android 用户若服务器不支持 ipv6，请于设置中允许地址类型设为仅IPV4。Shadowrocket (ios) 等有ipv6开关的同理。
4. Kitsunebi 相比于 kitsunebi-android，增加 apple 直连并去除 ipv6 规则，更适用于 ios ，也可用于 android。
5. clash 策略规则开始测试，规则文件则已被验证可用，然其配置文件可用性尚待测试。clash for windows 可通过 Geolite2 token 更新 ip 库。本人技术有限，目前通过替换 subconverter 内 acl4ssr 配置文件实现自有规则导入。此策略规则也可用于 surfboard 等其他应用。（需去除 v6 规则才可用于 surfboard ）
6. kitsunebi-android 已长期停更，其规则将于下月起暂停更新。
7.  v2ray 配置内嵌规则中错误地将直连 ip 规则 outboundTag 设为 proxy，请使用 2020-06-15 版之前的进行更新。


### Todo & Test:

测试中：  

chn-iplist.sh+ipv6 版  
clash 规则  
clash 策略规则 

### 路由器本地脚本使用

使用 `chmod +x /etc/sbin/chn-iplist.sh` 赋予其可执行权限。

### 致谢

- [CIDR2PAC](https://github.com/wspl/CIDR2PAC) - A es6 script for coverting CIDRs list to PAC proxy script.
- [ACL4SSR/Clash](https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash) - Clash规则碎片