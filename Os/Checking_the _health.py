#!/usr/bin/env python3
import shutil as s 
import psutil as ps 

def check_disk_usage (disk):
    du = s.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cou_usage ():
    usage = ps.cpu_percent()
    return usage < 75

if not check_disk_usage ("/") or not check_cou_usage():
    print("ERROR")
else:
    print("Everything is OK !")