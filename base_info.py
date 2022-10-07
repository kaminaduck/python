'''
References: 
https://geeksforgeeks.com/extracting-mac-address-using-python/
'''

# testing imports needed
import ipaddress, os, socket, uuid, platform, re

# pre-define global variables
global hostname, FQDN, IPaddr, MAC, OSenvironment, rhel_environment, win_environment

# set values for global variables
hostname = socket.gethostname()
FQDN = socket.getfqdn(hostname)
IPaddr = socket.gethostbyname(hostname)
MAC = (':'.join(re.findall('..','%012x' % uuid.getnode()))) #still need to understand this
OSenvironment = platform.system()
rhel_environment = str(platform.libc_ver())
win_environment = str(platform.win32_ver())

def HW_Info(): #gathering hardware info for top of report
    print("Host: "+ hostname)
    print("FQDN: "+ FQDN)
    print("IP Address: "+ IPaddr)
    print("OS Type: "+ OSenvironment)
    print("MAC Address: "+ MAC)
    if OSenvironment == "Linux":
        print("RHEL Info: "+ rhel_environment)
    elif OSenvironment == "Windows":
        print("Windows Info: "+ win_environment)
    else:
        print("Info not available")

# Testing functions
HW_Info