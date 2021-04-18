import time
import subprocess
import os
import signal

from kazoo.client import KazooClient
from kazoo.protocol.states import WatchedEvent, EventType



zk = KazooClient(hosts = '127.0.0.1:2181')
zk.start(timeout = 60)
parent_path = "/z"
node_counter = 0

def watch_children(path):
    @zk.ChildrenWatch(parent_path)
    def watcher(path):
        global node_counter
        children = zk.get_children(str(parent_path))
        for child in children:     
            new_path = str(parent_path) + "/" + str(child)
            print(new_path)
            watch_children(new_path)



watch_children("/z")
while True:
    time.sleep(5)