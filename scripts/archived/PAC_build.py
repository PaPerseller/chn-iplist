import os
from datetime import datetime, UTC
import ipaddress

OUT_DIR = "./"

def fetch_and_convert(src):
    with open(src, "r") as f:
        template = "var CN = [\n{}\n];\n"
        lines = []
        for iprange in f.readlines():
            iprange = iprange.strip()
            if not iprange:
                continue
            ipnet = ipaddress.IPv4Network(iprange)
            netaddr = int(ipnet.network_address)
            netmask = int(ipnet.netmask)
            s = f"  [0x{netaddr:08X}, 0x{netmask:08X}], // {iprange}"
            lines.append(s)
        lines.append("  [0xFFFFFFFF, 0xFFFFFFFF]  // 255.255.255.255/32")  # use broadcast as a placeholder
        return template.format("\n".join(lines))


def main():
    now = datetime.now(UTC)
    date = now.strftime("%Y%m%d")
    with open("./scripts/generate/code.js", "r") as f:
        code = f.read()
    code = code.replace("@@TIME@@", now.strftime("%Y-%m-%d"))

    os.makedirs(OUT_DIR, mode=0o755, exist_ok=True)
    
    data = fetch_and_convert(os.path.join(OUT_DIR, "chnroute-ipv4.txt"))

    filename = "chnroute.pac"
    with open(os.path.join(OUT_DIR, filename), "w") as f:
        f.write(code)
        f.write(data)
        f.write("\n")


if __name__ == '__main__':
    main() 
