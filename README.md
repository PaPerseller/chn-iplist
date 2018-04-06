# chn-iplist
Data comes from [ APNIC Delegated List](http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest), I convert it to txt rules file for use on the router. Then I make a shadowrocket config rule based on it.

Subscribe URL: 

chnroute.txt: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/chnroute.txt

shadowrocket config file: https://raw.githubusercontent.com/PaPerseller/chn-iplist/master/Rocket-chnroute.conf

Use `chmod +x /etc/sbin/chn-iplist.sh` to add executable permission.

The chnroute.txt will be updated once a month.
