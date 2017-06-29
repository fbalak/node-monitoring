from tendrl.commons.utils.time_utils import now as tendrl_now
import tendrl.commons.utils.etcd_utils as etcd_utils


def update_last_seen_at():
    etcd_utils.write_etcd(
        '/monitoring/nodes/%s/last_seen_at' % NS.node_context.node_id,
        tendrl_now().isoformat()
    )
