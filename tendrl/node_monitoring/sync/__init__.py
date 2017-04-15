from tendrl.commons.sds_sync import StateSyncThread
import gevent


class NodeMonitoringSyncStateThread(StateSyncThread):
    def __init__(self):
        super(NodeMonitoringSyncStateThread, self).__init__()

    def _run(self):
        while not self._complete.is_set():
            NS.central_store_thread.update_last_seen_at()
            gevent.sleep(3)
