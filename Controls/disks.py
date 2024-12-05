
import psutil


class Disk:
    def __init__(self, disk_threshold):
        self.disk_threshold = disk_threshold


    def used(self):
        disks = psutil.disk_usage('/').used
        return round(disks * 10**(-9), 2) #da byte a gigabyte


    def total(self):
        disks = psutil.disk_usage('/')
        return round(disks.total * 10**(-9), 2) #da byte a gigabyte


    def percent(self):
        disks = psutil.disk_usage('/')
        return disks.percent


    def get_priority(self):
        free = psutil.disk_usage('/').free * 2 ** (-30)
        if free <= self.disk_threshold:
            return "🟠"
        else:
            return ""