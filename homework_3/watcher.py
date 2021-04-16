import time
import subprocess
import os
import signal

from kazoo.client import KazooClient
from kazoo.protocol.states import WatchedEvent, EventType


# def kids_handler()


zk = KazooClient(hosts = '127.0.0.1:2181')
zk.start(timeout = 60)
app = None
# zk.get_children("/z", watch = kids_handler)

# # children = zk.get_children("/z")
# @zk.ChildrenWatch("/z")
# def watch_children(children):
#     # for child in children:
#     #     grandkids = zk.get_children("/z/" + child)
#     #     print(grandkids)
#     print(len(children))
#     # print(children)


@zk.DataWatch("/z")
def handle_node(data, stat, event: WatchedEvent):
    global app
    if event:
        if event.type == EventType.CREATED:
            print("To launch Discord press 1\nTo launch LOCALHOST game press 2\
                \nTo specify app to launch press 3: \nDismiss press 4")
            option = input()
            if int(option) == 1:
                app = subprocess.Popen(["/home/magdalena/Discord/Discord"])
            if int(option) == 2:
                app = subprocess.Popen(["/home/magdalena/Pulpit/LOCALHOST - Linux (64-bit)/LOCALHOST"])
            if int(option) == 3:
                print("App to launch (with full path): ")
                app_path = input()
                app = subprocess.Popen([app_path])
            if int(option) == 4:
                pass
            else:
                pass


        if event.type == EventType.DELETED:
            print("z deleted")
            if app != None:
                os.kill(app.pid, signal.SIGKILL)

        if event.type == EventType.CHILD:
            print("kidzz")

if zk.exists("/z"):
    kids = zk.get_children("/z")
    if kids != []:
        @zk.ChildrenWatch("z")
        def watch_children(children):
            print(children)

            
while True:
    time.sleep(5)
        