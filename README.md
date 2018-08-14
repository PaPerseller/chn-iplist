# chn-iplist
数据来源于 [ APNIC Delegated List](http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest)，将它转化为 txt 文件以在路由器上使用，并以此制作 Shadowrocket 与 Quantumult 规则文件，仅包含 chn-ip 列表和部分谷歌广告屏蔽规则。每月更新一次。

##Subscribe URL: 

chnroute.txt: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.txt

Shadowrocket: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Shadowrocket.conf

Quantumult (Filter): https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Quantumult.conf

##路由器本地脚本使用

Use `chmod +x /etc/sbin/chn-iplist.sh` to add executable permission.
