import psutil
from .. import thresholds

disks = psutil.disk_usage('/')

disks_used = disks.used * 10**(-9) #da byte a gigabyte
disks_free = disks.total * 10**(-9) #da byte a gigabyte
disks_percent = disks.percent * 10**(-9) #da byte a gigabyte

def get_disks_priority_level()
    disks_free = disks.free
    if disks_free <= thresholds.DISKS_THRESHOLD:
        return (1) #livello di priorità 1 ossia alto
    elif disks_free <= thresholds.DISKS_THRESHOLD +5 and disks_free >= thresholds.DISKS_THRESHOLD:
        return (2) #livello di priorità 2 ossia medio
    else:
        return(3) #livello di priorità 3 ossia bassa
