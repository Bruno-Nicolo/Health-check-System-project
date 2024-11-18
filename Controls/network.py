import psutil
import time


#status = psutil.net_connections(kind="inet").status

DELAY = 5 # in second


def upload_speed():
    try:
        network = psutil.net_io_counters(pernic=False, nowrap=True)
        bytes_sent = network.bytes_sent

        time.sleep(DELAY)

        network_2 = psutil.net_io_counters(pernic=False, nowrap=True)
        byte_sent_2 = network_2.bytes_sent

        up_speed = round((byte_sent_2 - bytes_sent) / 1024 / DELAY, 2)

        return up_speed # in KB/s
    except:
        return "Not Available"


def download_speed():
    try:
        network = psutil.net_io_counters(pernic=False, nowrap=True)
        bytes_recv = network.bytes_recv

        time.sleep(DELAY)

        network_2 = psutil.net_io_counters(pernic=False, nowrap=True)
        bytes_recv_2 = network_2.bytes_recv

        down_speed = round((bytes_recv_2 - bytes_recv) / 1024 / DELAY, 2)

        return down_speed # in KB/s
    except:
        return "Not Available"