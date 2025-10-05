// Author: iBug <ibug.io>
// Source: https://github.com/iBug/pac
// Time: @@TIME@@

var __PROXY__ = 'SOCKS5 localhost:1080'
var proxy = __PROXY__;
var direct = "DIRECT";

function belongsToSubnet(ip, list) {
  ip = ip >>> 0;

  if (list.length === 0 || ip < list[0][0])
    return false;

  // Binary search
  var x = 0, y = list.length, middle;
  while (y - x > 1) {
    middle = Math.floor((x + y) / 2);
    if (list[middle][0] <= ip)
      x = middle;
    else
      y = middle;
  }

  // Match
  var masked = ip & list[x][1];
  return (masked ^ list[x][0]) === 0;
}

function isCN(ip) {
  return belongsToSubnet(ip, CN);
}

function isLan(ip) {
  return belongsToSubnet(ip, LAN);
}

function FindProxyForURL(url, host) {
  // Fallback to IP whitelist
  var remoteIP = dnsResolve(host);
  if (!remoteIP || remoteIP.indexOf(":") !== -1) {
    // resolution failed or is IPv6 addr
    return proxy;
  }
  var ip = convert_addr(remoteIP);

  if (isLan(ip) || isCN(ip)) {
    return direct;
  }

  return proxy;
}

var LAN = [
  [0x00000000, 0xFFFFFFFF], // 0.0.0.0/32
  [0x0A000000, 0xFF000000], // 10.0.0.0/8
  [0x64400000, 0xFFC00000], // 100.64.0.0/10
  [0x7F000000, 0xFF000000], // 127.0.0.0/8
  [0xA9FE0000, 0xFFFF0000], // 169.254.0.0/16
  [0xAC100000, 0xFFF00000], // 172.16.0.0/12
  [0xC0A80000, 0xFFFF0000]  // 192.168.0.0/16
];
