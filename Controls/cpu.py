
# Add the parent directory to sys.path
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import thresholds
import psutil


def percentage():
    # percentuale di utilizzo della cpu
    return psutil.cpu_percent(interval=1)


def frequency():
    # attuale frequenza di clock della cpu
    return psutil.cpu_freq().current


def get_priority():
    if percentage() >= thresholds.CPU:
        return "⚠️"
    else:
        return ""