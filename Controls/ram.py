import psutil


class Ram:
    def __init__(self, ram_threshold):
        self.ram_threshold = ram_threshold


    #memoria disponibile ossia la memoria che può essere data istantaneamente ai processi senza che
    #il sistema entri in swap
    def available(self):
        ram = psutil.virtual_memory()
        return round(ram.available * 2**(-30), 2)


    #percentuale mem = (tot-available)/tot *100
    def percentage(self):
        ram = psutil.virtual_memory()
        return ram.percent


    #memoria attiva è la memoria attualmente in uso e quindi è in RAM
    def active(self):
        ram = psutil.virtual_memory()
        return round(ram.active * 2**(-30), 2)


    #memoria inattiva è la memoria non utilizzata
    def inactive(self):
        ram = psutil.virtual_memory()
        return round(ram.inactive * 2**(-30), 2)


    def get_priority(self):
        if self.percentage() <= self.ram_threshold:
            #return "⚠️"
            return "🔴"
        else:
            return ""