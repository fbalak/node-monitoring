from tendrl.commons import central_store
from tendrl.commons.utils.time_utils import now as tendrl_now


class NodeMonitoringEtcdCentralStore(central_store.EtcdCentralStore):
    def __init__(self):
        super(NodeMonitoringEtcdCentralStore, self).__init__()

    def save_config(self, config):
        NS.etcd_orm.save(config)

    def save_definition(self, definition):
        NS.etcd_orm.save(definition)

    def update_last_seen_at(self):
        NS.etcd_orm.client.write(
            '/monitoring/nodes/%s/last_seen_at' % NS.node_context.node_id,
            tendrl_now().isoformat()
        )
