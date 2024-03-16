#!/usr/bin/env python3 
# That's she-bang or has-bang for python at line 1 incase you forgot !
import os

if (os.path.exists("/run/reboot-required")==True):
    print("The system has to be rebooted ! ")
print("The system has no painding reboot !")
