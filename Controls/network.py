import psutil
from .. import thresholds

network = psutil.net_io_counters(pernic=False, nowrap=True)

pack_sent = network.packets_sent
pack_recv = network.packets_recv

err_in = network.errin
err_out = network.errout

status = psutil.net_connections(kind="inet").status
