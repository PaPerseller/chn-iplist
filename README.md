# chn-iplist


### 数据源
IPv4：[17mon/china_ip_list](https://github.com/17mon/china_ip_list) 和 [gaoyifan/china-operator-ip](https://github.com/gaoyifan/china-operator-ip)

IPv6： [ APNIC Delegated List](http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest) 

使用由 mosdns 项目启发的[合并优化脚本](https://github.com/PaPerseller/chn-iplist/blob/master/scripts/update_chnip.py)生成列表文件以在路由器上使用，并以此制作 Shadowrocket、Quantumult、acl、v2rayNG、v2rayN、pac、NekoRay/NekoBox、Loon、RouterOS、v2rayA/dae 规则和 v2ray/xray 配置内嵌规则，包含 chn-ip 列表及少量广告屏蔽规则。每15天自动更新一次。

## 可订阅规则：

| ios                                                                                                                                                                                                                                                                                                                                                                                                                                   | android                                                                                     | 其他                                                                                                                                                                                                                                                                                             |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [Shadowrocket](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Shadowrocket.conf)  | [acl (no ban ads)](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chn.acl) | chnroute [ipv4与ipv6](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.txt) \| [纯ipv4](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute-ipv4.txt) \| [纯ipv6](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute-ipv6.txt) |
| [Quantumult(X) (no chn-ip)](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult(X)_noIP.conf)                                                                                                                                                                                                                                                                                                                  |                                                                                             | [pac](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.pac) （默认走 socks5 localhost:1080）                                                                                                                                                                              |
| [Loon 配置文件](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Loon/Loon.conf)  订阅特殊规则：[direct](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Loon/ruleset/direct-special.list) \| [proxy](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Loon/ruleset/proxy-special.list) \| [reject](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Loon/ruleset/reject-special.list) |                                                                                             | [v2rayN ](https://raw.githubusercontent.com/PaPerseller/chn-iplist/refs/heads/master/v2rayN(G)/routing-ruleset_whitelist)                                                                                                                                                                                 |

## 需手动更新：

#### v2rayN(G)

将 [规则集](https://raw.githubusercontent.com/PaPerseller/chn-iplist/refs/heads/master/v2rayN(G)/routing-ruleset_whitelist) 复制后在应用路由设置内点击“从剪贴板导入规则集”。

#### v2ray/xray 配置内嵌规则

将[规则文本](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2ray-config_rule.json)加入配置文件 routing 对应区域。

#### v2rayA/dae 分流规则

将[规则文本](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/v2rayA.txt)替换入原有规则。


#### ROS 中部署

分别执行以下命令或将其保存为一个 script：
```
/tool fetch url="https://ghp.ci/https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/cn.rsc"
/import file-name=cn.rsc
/file remove [find name="cn.rsc"]
```


## PS.

1. Shadowrocket、Loon  等有 ipv6 开关的，若服务器不支持 ipv6 且连接失败，请设为仅 ipv4。额外提供前缀为 [IP-CIDR](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/ipv6.list) 和 [IP-CIDR6](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Loon/ruleset/ipv6.list) 两种远程 ipv6 规则。
2. Loon 配置文件为简洁配置，适用于使用自建节点。订阅规则以特殊规则为主，需搭配其他更完善的订阅规则。
3. 对于已支持在线更新 geoip 数据的软件，本规则不再内置 cn-ip 列表。
4. 为解决 Shadowrocket 配置在线更新后覆盖掉自定义规则部分，提供一个高度精简的[自定义配置模块](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Shadowrocket-DIY.module)。新建模块后复制本模块内容并自行增删修改后保存，不可通过 URL 添加以防模块被更新重置。此模块仅当有自定义规则需求时添加。
5. ROS 下载 cn.rsc 推荐 [CDN 加速地址](https://ghp.ci/https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/cn.rsc)以提高下载成功率。
6. sing-box 配置基于个人试验和使用以及他人反馈，建议作为参考，**不保证**在有些环境下的可用性。
7. v2raya 若使用 xray-core，建议参考[ v2raya 官方文档](https://v2raya.org/docs/advanced-application/custom-extra-config/) 使用生命周期钩子脚本[ python 版](https://github.com/PaPerseller/r2s-armbian-configure/blob/main/core-hook.py)或[ shell 版](https://github.com/PaPerseller/r2s-armbian-configure/blob/main/hook.sh)将 domainMatcher 的值设为 hybrid，若服务器启用了 tcpMptcp，则脚本中可选启用客户端  tcpMptcp。

## 致谢

- [CIDR2PAC](https://github.com/wspl/CIDR2PAC) - A es6 script for coverting CIDRs list to PAC proxy script.
- [ACL4SSR/Clash](https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash) - Clash规则碎片
- [domain-list-community](https://github.com/v2fly/domain-list-community) - Community managed domain list
- [mosdns](https://github.com/IrineSistiana/mosdns) - 插件化的 DNS 转发/分流器。
- [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat) - V2Ray 路由规则文件加强版
- [Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever)
- [iBug/pac](https://github.com/iBug/pac) - PAC scripts for proxies
- 其他部分规则来源的作者
- AI 辅助实现的自动化更新
