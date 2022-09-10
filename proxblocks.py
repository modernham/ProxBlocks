"""
Requires Firewall to be enabled host wide, and per VM/CT to be effective.
Very basic python script that updates the proxmox '/etc/pve/firewall/cluster.fw' file with a blacklist of tor addresses.
It will read your current file and replace everything below "[IPSET blacklist]" with a list of tor exit node IPs.
Pretty basic, but will do the trick in keeping some script kiddies out.
"""
from urllib.request import urlopen
from datetime import datetime

__author__ = "ModernHam"
__license__ = "GPLv3"
FILEPATH = "/etc/pve/firewall/cluster.fw"

newfile = []
header = """[IPSET blacklist]
"""

def writeFile():
    data = urlopen('https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-exit-nodes.lst').read()  # bytes
    body = data.decode('utf-8')
    file_data = header + body

    with open(FILEPATH) as file:
        lines = file.readlines()
    for line in lines:
        if line.__contains__("[IPSET blacklist]"):
            break
        else:
            newfile.append(line)

    newfile.append(file_data)


    with open(FILEPATH, "w") as file1:
        file1.writelines(newfile)
    print(str(datetime.now()) + ": " + "Updated cluster.fw with " + str(len(body.split("\n"))) + " entries.")

writeFile()