import psutil
import time

class Network:
    def __init__(self):
        #self.__DELAY = 5
        self.__DELAY = 10


    def upload_speed(self):
        try:
            network = psutil.net_io_counters(pernic=False, nowrap=True)
            bytes_sent = network.bytes_sent

            time.sleep(self.__DELAY)

            network_2 = psutil.net_io_counters(pernic=False, nowrap=True)
            byte_sent_2 = network_2.bytes_sent

            up_speed = round((byte_sent_2 - bytes_sent) / 125 / self.__DELAY, 2)

            return up_speed # in Kb/s
        except:
            return "Not Available"


    def download_speed(self):
        try:
            network = psutil.net_io_counters(pernic=False, nowrap=True)
            bytes_recv = network.bytes_recv

            time.sleep(self.__DELAY)

            network_2 = psutil.net_io_counters(pernic=False, nowrap=True)
            bytes_recv_2 = network_2.bytes_recv

            down_speed = round((bytes_recv_2 - bytes_recv) / 125 / self.__DELAY, 2)

            return down_speed # in Kb/s
        except:
            return "Not Available"