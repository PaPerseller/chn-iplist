#!/bin/sh
 
set -e -o pipefail
 
wget -O /tmp/chnip 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
cat /tmp/chnip | grep ipv4 | grep CN | awk -F\| '{printf("%s/%d\n", $4, 32-log($5)/log(2))}' >/tmp/chnroute_ipv4.txt
cat /tmp/chnip | grep ipv6 | grep CN | awk -F\| '{printf("%s/%d\n", $4, $5)}' >/tmp/chnroute_ipv6.txt
cat /tmp/chnroute_ipv4.txt >/tmp/chnroute.txt
cat /tmp/chnroute_ipv6.txt >>/tmp/chnroute.txt
rm -rf /tmp/chnip /tmp/chnroute_ipv4.txt /tmp/chnroute_ipv6.txt

mv /tmp/chnroute.txt /etc/storage/DEADC0DE/chnroute/chnroute.txt
