import psutil


class Ram:
    def __init__(self, threshold = 10, available=None, percentage=None, active=None, inactive=None):
        self.threshold = threshold
        self.available = available if available is not None else self.set_available()
        self.percentage = percentage if percentage is not None else self.set_percentage()
        self.active = active if active is not None else self.set_active()
        self.inactive = inactive if inactive is not None else self.set_inactive()


    def set_threshold(self, value):
        self.threshold = value


    #memoria disponibile ossia la memoria che può essere data istantaneamente ai processi senza che
    #il sistema entri in swap
    def set_available(self):
        ram = psutil.virtual_memory()
        self.available = round(ram.available * 2**(-30), 2)
        return self.available


    #percentuale mem = (tot-available)/tot *100
    def set_percentage(self):
        ram = psutil.virtual_memory()
        self.percentage = ram.percent
        return ram.percent


    #memoria attiva è la memoria attualmente in uso e quindi è in RAM
    def set_active(self):
        ram = psutil.virtual_memory()
        self.active = round(ram.active * 2**(-30), 2)
        return self.active


    #memoria inattiva è la memoria non utilizzata
    def set_inactive(self):
        ram = psutil.virtual_memory()
        self.inactive = round(ram.inactive * 2**(-30), 2)
        return self.inactive


    def get_priority(self):
        if self.set_percentage() <= self.threshold:
            return "🔴"
        else:
            return ""