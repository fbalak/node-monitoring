from tendrl.commons import central_store
from tendrl.commons.utils.time_utils import now as tendrl_now


# TODO WARNING (anmolB) central_store.EtcdCentralStore will be deprecated,
# please convert methods in this class to utility functions

class NodeMonitoringEtcdCentralStore(central_store.EtcdCentralStore):
    def __init__(self):
        super(NodeMonitoringEtcdCentralStore, self).__init__()

    def update_last_seen_at(self):
        NS._int.wclient.write(
            '/monitoring/nodes/%s/last_seen_at' % NS.node_context.node_id,
            tendrl_now().isoformat()
        )
