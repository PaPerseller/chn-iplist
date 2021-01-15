# chn-iplist

数据来源 [ APNIC Delegated List](http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest)，将其转化为 txt 文件以在路由器上使用，并以此制作 Shadowrocket、Quantumult、Kitsunebi、acl、BifrostV、v2rayNG、v2rayN、clash、pac、Qv2ray 规则和 v2ray 配置内嵌规则，仅包含 chn-ip 列表及部分谷歌和国内常见广告屏蔽规则。每月更新一次。

## Subscribe URL:

|                             ios                              |                           android                            |                             其他                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| [Shadowrocket](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Shadowrocket.conf) | [Kitsunebi-android](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Kitsunebi-android.conf) | chnroute [ipv4与ipv6合并版](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.txt) \| [纯ipv4版](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute-ipv4.txt) \| [纯ipv6版](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute-ipv6.txt) |
| [Quantumult](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult.conf) \| [Quantumult(X) (no chn-ip)](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult(X)_noIP.conf) | [acl (no ban ads)](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chn.acl) \| [acl (ban ads)](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chn_banad.acl) | [pac](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.pac) （默认非 chn-ip 网站走 socks5 localhost:1080） |
| [Kitsunebi](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Kitsunebi.conf) |                                                              | [clash 远程配置(test)](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/clash/pref.ini) |



## 需手动更新：

#### v2rayN(G)：

分别将 [proxy](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayN(G)/proxy.txt)、[direct](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayN(G)/direct.txt)或[direct-noip](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayN(G)/direct-noip.txt)、[block](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayN(G)/block.txt) 规则复制粘贴至应用内。

#### Qv2ray：

下载[此方案](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Qv2ray.json)或[no-chnip方案](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Qv2ray-noip.json)后导入。

#### clash：

https://github.com/PaPerseller/chn-iplist/blob/master/clash/clash.yml 

#### clash (no chn-ip)：

https://github.com/PaPerseller/chn-iplist/blob/master/clash/clash_noIP.yml

#### v2ray 配置内嵌规则：

将[规则文本](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2ray-config_rule.json)加入配置文件 routing 对应区域。

#### BifrostV：

在[相关文件夹](https://github.com/PaPerseller/chn-iplist/tree/master/BifrostV)下按规则类型复制粘贴至应用内。


## PS.

1. 已加入 ipv6 列表的规则：chnroute.txt、chnroute.pac、chn.acl、clash、v2rayN(G)、Kitsunebi-android、shadowrocket、Qv2ray
2. 若服务器不支持 ipv6，请于 Kitsunebi android 中设置允许地址类型为仅 IPV4。Shadowrocket (ios) 等有 ipv6 开关的同理。
3. Kitsunebi 相比于 kitsunebi-android，增加 apple 直连并去除 ipv6 规则。Kitsunebi 支持将从 2020-12-15 版起季更一年后结束。
4. 2020-09-15 版起列表由 mosdns 项目 [ip 合并优化脚本](https://github.com/IrineSistiana/mosdns/blob/main/scripts/update_chn_ip_domain.py) 生成。
5. v2rayNG(≥1.4.10) 、v2rayN 和 Qv2ray 支持调用 dat 文件资源，提供无 chnip 规则版，可配合使用 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat/releases) 加强版规则。Linux 用户可用 `bash <(curl -L https://raw.githubusercontent.com/PaPerseller/fhs-install-v2ray/master/install-dat-release.sh)` 更新此资源。


## Todo & Test:

测试中：  

clash 规则和 clash 策略规则配置文件   

## 路由器本地脚本使用

使用 `chmod +x /etc/sbin/chn-iplist.sh` 赋予其可执行权限。

## 致谢

- [CIDR2PAC](https://github.com/wspl/CIDR2PAC) - A es6 script for coverting CIDRs list to PAC proxy script.
- [ACL4SSR/Clash](https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash) - Clash规则碎片
- [domain-list-community](https://github.com/v2fly/domain-list-community) - Community managed domain list
- [mosdns](https://github.com/IrineSistiana/mosdns) - 插件化的 DNS 转发/分流器。
- [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat) - V2Ray 路由规则文件加强版