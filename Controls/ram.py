import psutil

import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module from the parent directory
import thresholds


#memoria disponibile ossia la memoria che può essere data istantaneamente ai processi senza che
#il sistema entri in swap
def available():
    ram = psutil.virtual_memory()
    return round(ram.available * 2**(-30), 2)

#percentuale mem = (tot-available)/tot *100
def percentage():
    ram = psutil.virtual_memory()
    return ram.percent

#memoria attiva è la memoria attualmente in uso e quindi è in RAM
def active():
    ram = psutil.virtual_memory()
    return round(ram.active * 2**(-30), 2)

#memoria inattiva è la memoria non utilizzata
def inactive():
    ram = psutil.virtual_memory()
    return round(ram.inactive * 2**(-30), 2)



def get_priority():
    if percentage() <= thresholds.RAM:
        return "⚠️"
    else:
        return ""

