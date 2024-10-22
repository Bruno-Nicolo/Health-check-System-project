import psutil, thresholds

# percentuale di utilizzo della cpu
cpu_percentage = psutil.cpu_percent(interval=1)

# attuale frequenza di clock della cpu
cpu_frequency = psutil.cpu_freq().current


def get_cpu_priority_level():
    cpu_percentage = psutil.cpu_percent(interval=1)

    if cpu_percentage >= thresholds.CPU_PERCENTAGE_THRESHOLD:
        return 1 # priorità livello 1
    else:
        return 3 # priorità livello 3
