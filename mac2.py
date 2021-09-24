#!/usr/bin/env python3

import subprocess
import optparse

]
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    # Decision Making : using if elif
    if not options.interface:
        parser.error("[-] Please specify an interface, see --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, see --help for more info.")
    return options
    # return this object if called

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
