from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

children = zk.get_children("/z")
@zk.ChildrenWatch("/my/example/testing")
def watch_children(children):
    # print(len(children))
    print(children)

@zk.DataWatch("/z")
def watch_node(data, stat):
    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))