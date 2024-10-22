import psutil
from .. import thresholds

# percentuale di utilizzo della cpu
percentage = psutil.cpu_percent(interval=1)

# attuale frequenza di clock della cpu
frequency = psutil.cpu_freq().current


def get_cpu_priority_level():
    percentage = psutil.cpu_percent(interval=1)

    if percentage >= thresholds.CPU:
        return 1 # priorità livello 1
    else:
        return 3 # priorità livello 3
