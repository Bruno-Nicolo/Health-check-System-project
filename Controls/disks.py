
# Add the parent directory to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import thresholds
import psutil


disks = psutil.disk_usage('/')

used = disks.used * 2**(-30) #da byte a gigabyte
total = disks.total * 2**(-30) #da byte a gigabyte
percent = disks.percent

def get_priority():
    free = psutil.disk_usage('/').free * 2 ** (-30)
    if free <= thresholds.DISKS:
        return 1 # livello di priorità 1 ossia alto
    elif free <= thresholds.DISKS + 5 and disks >= thresholds.DISKS:
        return 2 # livello di priorità 2 ossia medio
    else:
        return 3 # livello di priorità 3 ossia bassa