#!/usr/bin/env python3

import subprocess
# OS commands using python
import optparse
# user input commands from command line

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
# capture arguments and options from user input, "-i" & "--interface" - options, "interface" - variable
(options, arguments) = parser.parse_args()
# options then arguments, contains user input options.new_mac & options.interface
# options - an object containing values for all of your options
# arguments - the list of positional arguments leftover after parsing options
# run command: python3 mac.py --help to understand more
# parser, options, arguments are variables, we can use p, o, a instead as well.

# ctrl+d duplicate current line in pyCharm, cmd+shift+D for sublime
# ctrl+/ comment string in pyCharm, cmd+/ for sublime

# # [variables]:
# interface = "eth0"
# new_mac = "00:00:00:00:00:00"

# variables for input - options, just another way to assing values to variable
interface = options.interface
new_mac = options.new_mac

# # [user input]:
# interface = input("interface > ")
# new_mac = input("new MAC > ")
# # for python2.7 raw_input("")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
# # not checking user input, just string, payload for hijacking: ifconfig; ls; or (;ls;)
# # to execute side commands!

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
# handling user input commands, anti-hijacking

# default: 
# experimental: de:ad:be:ef:ca:fe
