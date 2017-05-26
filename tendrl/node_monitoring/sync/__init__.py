from tendrl.commons.sds_sync import StateSyncThread
import tendrl.node_monitoring.utils.central_store_util as central_store_util
import gevent


class NodeMonitoringSyncStateThread(StateSyncThread):
    def __init__(self):
        super(NodeMonitoringSyncStateThread, self).__init__()

    def _run(self):
        while not self._complete.is_set():
            central_store_util.update_last_seen_at()
            gevent.sleep(3)
