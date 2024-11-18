
# Add the parent directory to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import thresholds
import psutil


def used():
    disks = psutil.disk_usage('/')
    return round(disks.used * 2**(-30), 2) #da byte a gigabyte


def total():
    disks = psutil.disk_usage('/')
    return round(disks.total * 2**(-30), 2) #da byte a gigabyte


def percent():
    disks = psutil.disk_usage('/')
    return disks.percent


def get_priority():
    free = psutil.disk_usage('/').free * 2 ** (-30)
    if free <= thresholds.DISKS:
        return "⚠️"
    else:
        return ""

