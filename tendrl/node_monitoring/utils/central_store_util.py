from tendrl.commons.utils.time_utils import now as tendrl_now


def update_last_seen_at():
    NS._int.wclient.write(
        '/monitoring/nodes/%s/last_seen_at' % NS.node_context.node_id,
        tendrl_now().isoformat()
    )
