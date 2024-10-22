import psutil

ram = psutil.virtual_memory()
print (ram)
#memoria disponibile ossia la memoria che può essere data istantaneamente ai processi senza che
#il sistema entri in swap
ram_available = ram.available
#percentuale mem = (tot-available)/tot *100
ram_percentage = ram.percent
#memoria attiva è la memoria attualmente in uso e quindi è in RAM
ram_active = ram.active
#memoria inattiva è la memoria non utilizzata
ram_inactive = ram.inactive

RAM_THRESHOLD = 2 * 1024 * 1024 * 1024  #2GB limite RAM
def get_ram_priority_level():
    ram_available =ram.available
    if ram_available >= RAM_THRESHOLD:
        return(1)  #livello di priorità 1 ossia alto
    else:
        return(3)  #livello di priorità 3 ossia bassa