from scapy.all import * 
import sys



conf.verb = 0


ip = "192.168.0."

for i in range (1,254):
    ipadres = ip + str(i)
    ans=srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ipadres),timeout=1,retry=1)
    if ans:
        print("IP adres: " + ans.psrc + " MAC : " + ans.hwsrc) 
