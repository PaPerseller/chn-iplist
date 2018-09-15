#荒野无灯固件使用
#开启ss命令：1. nvram set google_fu_mode=0xDEADBEEF 2. nvram commit

set -e -o pipefail
 
wget -O- 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest' | \
    awk -F\| '/CN\|ipv4/ { printf("%s/%d\n", $4, 32-log($5)/log(2)) }' > \
    /tmp/chn-iplist.txt
 
mv /tmp/chn-iplist.txt /etc/storage/DEADC0DE/chnroute/chnroute.txt
