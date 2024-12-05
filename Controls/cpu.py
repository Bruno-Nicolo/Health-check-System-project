
import psutil

class Cpu:
    def __init__(self, cpu_threshold):
        self.cpu_threshold = cpu_threshold


    def percentage(self):
        # percentuale di utilizzo della cpu
        return psutil.cpu_percent(interval=1)


    def frequency(self):
        # attuale frequenza di clock della cpu
        return psutil.cpu_freq().current


    def get_priority(self):
        if self.percentage() >= self.cpu_threshold:
            return "🔴"
        else:
            return ""