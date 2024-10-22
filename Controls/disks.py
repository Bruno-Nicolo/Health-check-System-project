import psutil
from .. import thresholds

disks = psutil.disk_usage('/')

used = disks.used * 10**(-9) #da byte a gigabyte
free = disks.total * 10**(-9) #da byte a gigabyte
percent = disks.percent * 10**(-9) #da byte a gigabyte

def get_disks_priority_level():
    free = disks.free
    if free <= thresholds.DISKS:
        return (1) #livello di priorità 1 ossia alto
    elif free <= thresholds.DISKS +5 and disks >= thresholds.DISKS:
        return (2) #livello di priorità 2 ossia medio
    else:
        return(3) #livello di priorità 3 ossia bassa
