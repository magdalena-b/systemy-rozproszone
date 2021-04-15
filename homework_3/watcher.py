import time

from kazoo.client import KazooClient
from kazoo.protocol.states import WatchedEvent, EventType


zk = KazooClient(hosts = '127.0.0.1:2181')
zk.start(timeout = 60)

# children = zk.get_children("/z")
@zk.ChildrenWatch("/z")
def watch_children(children):
    # print(len(children))
    print(children)


@zk.DataWatch("/z")
def handle_node(data, stat, event: WatchedEvent):
   if event:
        if event.type == EventType.CREATED:
            print("odpal apke:")
            app = input()
            print("odpalamyy " + app)

        if event.type == EventType.DELETED:
            print("z deleted")
            print("zatrzymajj " + app)

while True:
    time.sleep(5)
        