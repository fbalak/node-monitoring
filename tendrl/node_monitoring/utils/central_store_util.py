from tendrl.commons.utils.time_utils import now as tendrl_now


def write_etcd(key, value):
    try:
        NS._int.wclient.write(key, value, quorum=True)
    except (AttributeError, EtcdException) as ex:
        NS._int.wreconnect()
        NS._int.wclient.write(key, value, quorum=True)


def update_last_seen_at():
    write_etcd(
        '/monitoring/nodes/%s/last_seen_at' % NS.node_context.node_id,
        tendrl_now().isoformat()
    )
