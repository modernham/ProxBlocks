ProxBlocks

Very simple python script that will download the lastest list of TOR addresses and exit nodes, and add them to the "[IPSET blacklist]" Section of your proxmox firewall file (/etc/pve/firewall/cluster.fw)



## Deployment

You must enable the top level firewall for your Proxmox hypervisor This can typically be done by navigating to: Datacenter -> Firewall -> Options -> Firewall Checked

On top of that, you must enable the firewall for each VM/CT you intend to block TOR connections from.

You can Download/Install the script and run it via cron like so (as root): 
```bash
apt-get install python3
apt-get install wget
mkdir /root/ProxBlocks
cd /root/ProxBlocks
wget https://raw.githubusercontent.com/modernham/ProxBlocks/main/proxblocks.py

```

Now you just need to set a cron task to run it every so often. 

The following below example will run it every 12 hours.

```bash
#Open Cron
crontab -e
#Paste In
0 */12 * * * /usr/bin/python3 /root/ProxBlocks/proxblocks.py >> ~/cron.log 2>&1
```
