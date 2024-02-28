#!/usr/bin/env python3

import shutil
import psutil

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

def check_root_full():
   """returns true if the root  partition is fuel"""
   return check_disk_usage(55)

if not check_disk_usage('/') or not check_cpu_usage():
	print(True)
else:
	print("everythin is ok!")


print('new line')
