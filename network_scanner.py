#!/usr/bin/env python

import scapy.all as scapy
# send, sniff and dissect and forge network packets

def scan(ip):
    # list clients of the network and MAC addresses
    # scapy.arping(ip) 
    # # this can do the following but it does too much, we will create our own arping()
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.pdst=ip
    # print(arp_request.summary())  # summary() is like info for any snapy function.
    # # pdst is an option of ARP()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # set destination MAC to broadcast
    arp_request_broadcast = broadcast / arp_request
    # arp_request.show()    # show() is more detailed version of summary()
    # combine broadcast & arp_request together because scapy allows to us to do so
    # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    # # timeout=1 - wait 1 sec for response, verbose-False - don't display extra ( no of sent )
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("__________________________________________\nIP\t\t\tMAC Address\n------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        # psrc(ip) & hwsrc(mac) are options in element[1], vied by show()


scan("192.168.1.254/24")
# 192.168.1.77/24 my IP, use `route -n` to see your gateway - 192.168.1.1
# /24 represents all 254 combination of ips for 192.168.1 subnet.
