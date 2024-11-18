import psutil
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import thresholds


def temperature():
    try:
        temp = psutil.sensors_temperatures(fahrenheit=False)["acpitz"][0].current
        return f"{temp}°C"
    except:
        return "not available"


def get_priority():
    try:
        if temperature() >= thresholds.TEMPERATURE:
            return "⚠️"
        else:
            return ""
    except:
        return ""


def uptime():
    uptime = time.time() - psutil.boot_time() # Uptime in secondi
    uptime_hours = uptime // 3600
    uptime_minutes = (uptime % 3600) // 60
    return f"{int(uptime_hours)}h {int(uptime_minutes)}m"