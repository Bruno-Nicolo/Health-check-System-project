import psutil
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import thresholds


def temperature():
    temp = psutil.sensors_temperatures(fahrenheit=False)["acpitz"][0].current
    return temp


def get_priority():
    if temperature() >= thresholds.TEMPERATURE:
        return "⚠️"
    else:
        return ""


def uptime():
    uptime = time.time() - psutil.boot_time() # Uptime in secondi
    uptime_hours = uptime // 3600  # Ore intere
    uptime_minutes = (uptime % 3600) // 60  # Minuti rimanenti
    return f"{uptime_hours}h {uptime_minutes}m"

