'''
References: 
https://www.geeksforgeeks.org/extracting-mac-address-using-python/
https://www.geeksforgeeks.org/get-your-system-information-using-python-script/
'''

# testing imports needed
import ipaddress, os, socket, uuid, platform, re

# pre-define global variables
global hostname, FQDN, IPaddr, MAC, OS_environment, OS_version, my_system

# set values for global variables
my_system = platform.uname()
hostname = my_system.node
FQDN = socket.getfqdn(hostname)
IPaddr = socket.gethostbyname(hostname)
MAC = (':'.join(re.findall('..','%012x' % uuid.getnode()))) #still need to understand this
OS_environment = my_system.system
OS_version = my_system.version

def HW_Info(): #gathering hardware info for top of report
    print("Host: "+ hostname)
    print("FQDN: "+ FQDN)
    print("IP Address: "+ IPaddr)
    print("OS Environment: "+ OS_environment)
    print("MAC Address: "+ MAC)
    if OS_environment != "Linux" and OS_environment != "Windows":
        print("OS version not available; OS Environment not found")
    else:
        print(OS_environment + " Version: " + OS_version)
# Testing functions
HW_Info()