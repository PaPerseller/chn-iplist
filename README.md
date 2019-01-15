# chn-iplist
数据来源于 [ APNIC Delegated List](http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest)，将其转化为 txt 文件以在路由器上使用，并以此制作 Shadowrocket、Quantumult、Kitsunebi、acl、BifrostV、v2rayNG 规则和 V2ray 配置文件内嵌规则，仅包含 chn-ip 列表及部分谷歌和国内常见广告屏蔽规则。每月更新一次。

### Subscribe URL: 

chnroute.txt: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.txt

Shadowrocket: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Shadowrocket.conf

Quantumult (Filter): https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult.conf

Quantumult (no chn-ip) : https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult_noIP.conf

Kitsunebi: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Kitsunebi.conf

acl（暂无广告屏蔽规则）: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chn.acl

BifrostV 规则进入测试，在[相关文件夹](https://github.com/PaPerseller/chn-iplist/tree/master/BifrostV)下按规则类型复制粘贴至应用内。

V2ray 配置文件内嵌规则进入测试，将[规则文本](https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/V2ray-config_rule.txt)添加入配置文件 routing 对应区域。域名解析策略 IPIfNonMatch/IPOnDemand 按选择调整下面各 RuleObject 顺序。

v2rayNG（version≥0.6.9）规则进入测试，在[相关文件夹](https://github.com/PaPerseller/chn-iplist/tree/master/v2rayNG)下按规则类型复制粘贴至应用内。

### TODO:

- [ ] Kitsunebi 规则格式调整完善

### 路由器本地脚本使用

使用 `chmod +x /etc/sbin/chn-iplist.sh` 赋予其可执行权限。