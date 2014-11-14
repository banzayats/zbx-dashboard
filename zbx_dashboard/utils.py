from pyzabbix import ZabbixAPI
from django.conf import settings


def zapi_login():
    zapi = ZabbixAPI(settings.ZABBIX_URL)
    zapi.session.auth = (settings.ZABBIX_USER, settings.ZABBIX_PASS)
    zapi.session.verify = False
    zapi.login(settings.ZABBIX_USER, settings.ZABBIX_PASS)
    return zapi


def zbx_get_screen_name(zbx_screen_id):
    if zbx_screen_id:
        zapi = zapi_login()
        screens = zapi.screen.get(
            screenids=zbx_screen_id,
            output='extend',
            selectScreenItems='extend',
        )
        if screens:
            return screens[0]['name']
        else:
            return ''
    else:
        return ''


def zbx_get_graphs(zbx_screen_id):
    if zbx_screen_id:
        zapi = zapi_login()
        screens = zapi.screen.get(
            screenids=zbx_screen_id,
            output='extend',
            selectScreenItems='extend',
        )
        if screens:
            graphs = []
            for item in screens[0]['screenitems']:
                if item['resourcetype'] == '0':
                    graph = zapi.graph.get(
                        graphids=item['resourceid'],
                        output='extend',
                    )
                    graphs.append(
                        {
                            'title': graph[0]['name'],
                            'graph_id': item['resourceid'],
                        }
                    )
            return graphs
        else:
            return []
    else:
        return []
