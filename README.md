# chn-iplist

数据来源 [ APNIC Delegated List](http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest)，将其转化为 txt 文件以在路由器上使用，并以此制作 Shadowrocket、Quantumult、Kitsunebi、acl、BifrostV、v2rayNG、clash、pac 、Qv2ray 规则和 v2ray 配置内嵌规则，仅包含 chn-ip 列表及部分谷歌和国内常见广告屏蔽规则。每月更新一次。

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

v2ray 配置内嵌规则：将[规则文本](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2ray-config_rule.json)加入配置文件 routing 对应区域。

v2rayNG ：分别将 [proxy](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayNG/proxy.txt)、[direct](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayNG/direct.txt)或[direct-noip](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayNG/direct-noip.txt)、 [block](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayNG/block.txt) 规则复制粘贴至应用内。

clash：https://github.com/PaPerseller/chn-iplist/blob/master/clash/clash.yml 

clash (no chn-ip)：https://github.com/PaPerseller/chn-iplist/blob/master/clash/clash_noIP.yml

Qv2ray：下载[此方案](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Qv2ray.json)或[no-chnip 方案](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Qv2ray-noip.json)后导入。

### PS.

1. v2rayNG 规则与 v2rayN 可通用。 
2. 已加入 ipv6 列表的规则：chnroute.txt、chnroute.pac、chn.acl、clash、v2rayNG、Kitsunebi-android、shadowrocket、Qv2ray
3. 若服务器不支持 ipv6，请于 Kitsunebi android 中设置允许地址类型为仅 IPV4。Shadowrocket (ios) 等有 ipv6 开关的同理。
4. Kitsunebi 相比于 kitsunebi-android，增加 apple 直连并去除 ipv6 规则。
5. clash 配置文件可用性尚待测试。
6. 2020-09-15 版起试用 mos-chinadns 项目 [ip 合并优化脚本](https://github.com/IrineSistiana/mos-chinadns/blob/master/scripts/update_chn_ip_domain.py)生成的列表。
7. v2rayNG(≥1.4.10) 和 Qv2ray 等支持调用 dat 文件资源的，提供无 chnip 规则版，可配合使用 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat/releases) 加强版规则。Linux 用户可用 `bash <(curl https://raw.githubusercontent.com/PaPerseller/fhs-install-v2ray/master/install-dat-release.sh)` 更新此资源。


### Todo & Test:

测试中：  

clash 规则和 clash 策略规则配置文件   

### 路由器本地脚本使用

使用 `chmod +x /etc/sbin/chn-iplist.sh` 赋予其可执行权限。

### 致谢

- [CIDR2PAC](https://github.com/wspl/CIDR2PAC) - A es6 script for coverting CIDRs list to PAC proxy script.
- [ACL4SSR/Clash](https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash) - Clash规则碎片
- [domain-list-community](https://github.com/v2fly/domain-list-community) - Community managed domain list
- [mos-chinadns](https://github.com/IrineSistiana/mos-chinadns)
- [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat) - V2Ray 路由规则文件加强版