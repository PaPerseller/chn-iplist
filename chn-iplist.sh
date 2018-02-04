et -e -o pipefail
 
wget -O- 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest' | \
    awk -F\| '/CN\|ipv4/ { printf("%s/%d\n", $4, 32-log($5)/log(2)) }' > \
    /tmp/chinadns_chnroute.txt
 
mv /tmp/chinadns_chnroute.txt /etc/storage/DEADC0DE/chnroute/chnroute.txt
