import psutil

import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module from the parent directory
import thresholds


ram = psutil.virtual_memory()

#memoria disponibile ossia la memoria che può essere data istantaneamente ai processi senza che
#il sistema entri in swap
available = ram.available
#percentuale mem = (tot-available)/tot *100
percentage = ram.percent
#memoria attiva è la memoria attualmente in uso e quindi è in RAM
active = ram.active
#memoria inattiva è la memoria non utilizzata
inactive = ram.inactive


def get_ram_priority_level():
    ram = psutil.virtual_memory()

    available = ram.available

    if available >= thresholds.RAM:
        return(1)  #livello di priorità 1 ossia alto
    else:
        return(3)  #livello di priorità 3 ossia bassa