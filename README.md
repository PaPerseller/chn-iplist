# chn-iplist
数据来源于 [ APNIC Delegated List](http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest)，将它转化为 txt 文件以在路由器上使用，并以此制作 Shadowrocket、Quantumult、Kitsunebi、acl、BifrostV 规则文件，仅包含 chn-ip 列表和部分谷歌和国内常见广告屏蔽规则。每月更新一次。

### Subscribe URL: 

chnroute.txt: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.txt

Shadowrocket: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Shadowrocket.conf

Quantumult (Filter): https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult.conf

Kitsunebi: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Kitsunebi.conf

acl: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chn.acl

BifrostV 规则进入测试，在相关文件夹下按规则类型复制粘贴至应用内。

### 路由器本地脚本使用

使用 `chmod +x /etc/sbin/chn-iplist.sh` 赋予其可执行权限。
