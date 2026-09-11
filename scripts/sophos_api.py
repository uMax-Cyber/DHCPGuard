#!/usr/bin/env python3
"""Sophos Firewall XML API wrapper.
Usage: sophos_api.py <gw1|gw2> <Module> [Module2...]
Valid modules: DHCP, DHCPServer, Interface, IPHost, FirewallRule, DHCPRelay"""
import os, ssl, sys, urllib.request, urllib.parse as up

def load_env(path):
    for line in open(path):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            v = v.split("#")[0].strip().strip('"').strip("'")
            if k.strip() and v:
                os.environ.setdefault(k.strip(), v)

def main():
    if len(sys.argv) < 3:
        print(__doc__); return 2
    gw = sys.argv[1].upper()
    tag = "SOPHOS1" if gw == "GW1" else "SOPHOS2"
    load_env(os.environ.get("CREDS_FILE", "/etc/sophos.env"))

    ctx = ssl.create_default_context()
    ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    url = os.environ[f"{tag}_URL"].rstrip("/")

    for mod in sys.argv[2:]:
        xml = (f'<Request><Login><Username>{os.environ[f"{tag}_USER"]}</Username>'
               f'<Password>{os.environ[f"{tag}_PASS"]}</Password></Login>'
               f'<Get><{mod}></{mod}></Get></Request>')
        req = urllib.request.Request(url + "/webconsole/APIController",
            data=up.urlencode({"reqxml": xml}).encode(),
            headers={"Content-Type": "application/x-www-form-urlencoded"})
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            out = r.read().decode("utf-8", "replace")
        if "Invalid" in out:
            print(f"== {mod}: INVALID (not supported)"); continue
        body = out[out.find("</Login>")+8:out.rfind("</Response>")]
        print(f"== {gw} / {mod}")
        print(body[:4000])

if __name__ == "__main__":
    sys.exit(main())
