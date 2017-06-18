import gevent.event
import gevent.greenlet
import signal
from tendrl.commons.event import Event
from tendrl.commons.message import Message
from tendrl.commons import manager as commons_manager
from tendrl.commons import TendrlNS
from tendrl.node_monitoring import NodeMonitoringNS
from tendrl.node_monitoring.sync import NodeMonitoringSyncStateThread


class NodeMonitoringManager(commons_manager.Manager):
    def __init__(self):
        super(
            NodeMonitoringManager,
            self
        ).__init__(
            NS.state_sync_thread,
        )


def main():
    NodeMonitoringNS()
    TendrlNS()
    NS.type = "monitoring"

    complete = gevent.event.Event()

    NS.state_sync_thread = NodeMonitoringSyncStateThread()
    NS.node_monitoring.definitions.save()
    NS.node_monitoring.config.save()
    NS.publisher_id = "node_monitoring"
    
    if NS.config.data.get("with_internal_profiling", False):
        from tendrl.commons import profiler
        profiler.start()
        
    manager = NodeMonitoringManager()
    manager.start()

    def shutdown():
        Event(
            Message(
                priority="debug",
                publisher=NS.publisher_id,
                payload={"message": "Signal handler: stopping"}
            )
        )
        complete.set()

    gevent.signal(signal.SIGTERM, shutdown)
    gevent.signal(signal.SIGINT, shutdown)

    while not complete.is_set():
        complete.wait(timeout=1)


if __name__ == "__main__":
    main()
