#!/usr/bin/env python3

#check output
import subprocess
import optparse
import re
# `re` - module for regex operations


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()
    # no changes needs to be made so cascade this definition for focus


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    # check_output() from subprocess module
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # re.search(r"..") to specify regex rule ( tested on pythex.org )
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        # group(0) - for more than one occurance, variable takes values in groups and we need the 1st group i.e. group(0)
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read Mac address.")
        # to execute programm without errors, `lo` interface doesn't have MAC adress


(options, arguments) = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
# str() because for `lo` current_mac is assigned null_character which can't be printed using print()
change_mac(options.interface, options.new_mac)

# [ function inputs ]
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")
