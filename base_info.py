#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a script that grabs basic info of the system.

References:
https://www.geeksforgeeks.org/extracting-mac-address-using-python/
https://www.geeksforgeeks.org/get-your-system-information-using-python-script/
https://www.geeksforgeeks.org/getting-the-time-since-os-startup-using-python/
"""

# built-in module imports here
import os, socket, uuid, platform, re, ctypes

# third-party module imports

# path changes and personal modules

# authors are the writers of the code
__author__ = "Charlie Rogers"
__contact__ = "charlie.rogers@fearnworks.com"
__copyright__ = "Copyright 2022"
# credits go to those who offered suggestions, reported big fixes, but did not write code
__credits__ = ["Charlie Rogers", "Kate Libby", "Dade Murphy",
                    "Paul Cook", "Joey Pardella", 
                    "Phantom Phreak","Razor and Blade"]
__date__ = "2022/10/17"
__deprecated__ = False
__email__ = "charlie.rogers@fearnworks.com"
__license__ = "GPL" # or proprietary
__maintainer__ = "Charlie Rogers"  # person who will fix bugs and make improvements if imported
__status__ = "Prototype"   # "Prototype", "Development" or "Production"
__version__ = "0.0.1"   # Major.minor.patch

# pre-define global variables
global hostname, FQDN, IPaddr, MAC, OS_environment, OS_version, my_system, dash, win_tick_library

# set values for global variables
dash = "----------------------------------------"
my_system = platform.uname()
hostname = my_system.node
FQDN = socket.getfqdn(hostname)
IPaddr = socket.gethostbyname(hostname)
MAC = (':'.join(re.findall('..','%012x' % uuid.getnode()))) #still need to understand this
OS_environment = my_system.system
OS_version = my_system.version
win_tick_library = ctypes.windll.kernel32 # getting the library in which GetTickCount64() resides

# define classes and functions


def Win_Info(): #more specific data for Windows environments
    print(OS_environment + " Version: " + OS_version)
    
    uptime = win_tick_library.GetTickCount64() # calling the function and storing the return value
    uptime = int(str(uptime)[:-3]) # time is in milliseconds i.e. 1000 * seconds, therefore truncating the value
    
    # extracting hours, minutes, seconds & days from t
    # variable (which stores total time in seconds)
    mins, sec = divmod(uptime, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)

    # formatting the time in readable form
    # (format = x days, HH:MM:SS)
    print(f"Uptime: {days} days, {hour:02}:{mins:02}:{sec:02}")

def Linux_Info(): #more specific data for Linux environments
    print(OS_environment + " Version: " + OS_version)
    
    # sending the uptime command as an argument to popen()
    # and saving the returned result (after truncating the trailing \n)
    uptime = os.popen('uptime -p').read()[:-1]
    print(uptime)

def HW_Info(): #gathering hardware info for top of report
    print("Host: "+ hostname)
    print("FQDN: "+ FQDN)
    print("IP Address: "+ IPaddr)
    print("OS Environment: "+ OS_environment)
    print("MAC Address: "+ MAC)
    if OS_environment == "Linux":
        Linux_Info()
    elif OS_environment == "Windows":
        Win_Info()
    else:
        print("OS version not available; OS Environment not found")

# main code goes here
print(dash)
HW_Info()
print(dash)

