import psutil
import time


#status = psutil.net_connections(kind="inet").status

DELAY = 1 # in second


def upload_speed():
    network = psutil.net_io_counters(pernic=False, nowrap=True)
    bytes_sent = network.bytes_sent

    time.sleep(DELAY)

    network_2 = psutil.net_io_counters(pernic=False, nowrap=True)
    byte_sent_2 = network_2.bytes_sent

    upload_speed = (byte_sent_2 - bytes_sent) * 2 ** (-20) / DELAY

    return upload_speed # in Mb/s


def download_speed():
    network = psutil.net_io_counters()
    bytes_recv = network.bytes_recv

    time.sleep(DELAY)

    network_2 = psutil.net_io_counters()
    bytes_recv_2 = network_2.bytes_recv

    download_speed = (bytes_recv_2 - bytes_recv) * 2 ** (-20) / DELAY

    return download_speed # in Mb/s

print(upload_speed())