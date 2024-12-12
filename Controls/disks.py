
import psutil


class Disk:
    def __init__(self, threshold=10, used=None, total=None, percent=None):
        self.threshold = threshold
        self.used = used if used is not None else self.set_used()
        self.total = total if total is not None else self.set_total()
        self.percent = percent if percent is not None else self.set_percent()

    def to_dict(self):
        return {
            "used": self.used,
            "total": self.total,
            "percent": self.percent,
            "get_priority": self.get_priority()
        }

    def set_threshold(self, value):
        self.threshold = value


    def set_used(self):
        disks = psutil.disk_usage('/').used
        self.used = round(disks * 10**(-9), 2) #da byte a gigabyte
        return self.used 


    def set_total(self):
        disks = psutil.disk_usage('/')
        self.total = round(disks.total * 10**(-9), 2) #da byte a gigabyte
        return self.total

    def set_percent(self):
        self.percent = psutil.disk_usage('/').percent
        return self.percent


    def get_priority(self):
        free = psutil.disk_usage('/').free * 2 ** (-30)
        if free <= self.threshold:
            return "🟠"
        else:
            return ""
