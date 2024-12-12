import psutil
import time


class General_info:
    def __init__(self, threshold=45):
        self.threshold = threshold


    def set_threshold(self, value):
        self.threshold = value


    def temperature(self):
        try:
            temp = psutil.sensors_temperatures(fahrenheit=False)["acpitz"][0].current
            return f"{temp}°C"
        except:
            return "not available"


    def get_priority(self):
        try:
            if self.temperature() >= self.threshold:
                return "🟠"
            else:
                return ""
        except:
            return ""


    def top_processes(self):
        processes = []

        for p in psutil.process_iter(['name', 'cpu_times', "pid"]):
            if p.info["cpu_times"] is not None:
                processes.append({
                    "name": p.info["name"],
                    "cpu_usage": round(p.info["cpu_times"][0] + p.info["cpu_times"][1], 2), # accumulated process time in s
                    "pid": p.info["pid"]
                })

        top = sorted(processes, key=lambda el: el["cpu_usage"])[-5:]
        return top


    def uptime(self):
        uptime = time.time() - psutil.boot_time() # Uptime in secondi
        uptime_hours = uptime // 3600
        uptime_minutes = (uptime % 3600) // 60
        uptime_seconds = uptime - (uptime_hours*3600 + uptime_minutes*60)
        return f"{int(uptime_hours)}h {int(uptime_minutes)}m {int(uptime_seconds)}s"
