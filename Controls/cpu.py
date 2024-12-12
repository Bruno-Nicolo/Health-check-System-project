
import psutil

class Cpu:

    def __init__(self, threshold=85, percentage=None, frequency=None):
        self.threshold = threshold
        self.percentage = percentage if percentage is not None else self.set_percentage()
        self.frequency = frequency if frequency is not None else self.set_frequency()


    def set_threshold(self, value):
        self.threshold = value


    def set_percentage(self):
        self.percentage = psutil.cpu_percent(interval=1)
        # percentuale di utilizzo della cpu
        return self.percentage


    def set_frequency(self):
        self.frequency = psutil.cpu_freq().current
        # attuale frequenza di clock della cpu
        return self.frequency


    def get_priority(self):
        if self.set_percentage() >= self.threshold:
            return "🔴"
        else:
            return ""
