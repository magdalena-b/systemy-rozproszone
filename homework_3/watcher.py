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
nodes_counter = 0
# zk.get_children("/z", watch = kids_handler)

# # children = zk.get_children("/z")
# @zk.ChildrenWatch("/z")
# def watch_children(children):
#     # for child in children:
#     #     grandkids = zk.get_children("/z/" + child)
#     #     print(grandkids)
#     print(len(children))
#     # print(children)

# @zk.DataWatch(path)
# def handler(data, stat, event: WatchedEvent):
#     if event:
#         if event.type == EventType.CREATED:
#             print("grandkid")



# def handle_child_node(path):
#     print(path)
#     zk.get_children(path, watch = handler)


def watch_children_2(path: str):
    print("in watch children 2: " + path)
    # children = zk.get_children(path)
    @zk.ChildrenWatch
    def children_watcher(path):
        children = zk.get_children(path)
        print("Loooool")
        global nodes_counter
        for child in children:
            nodes_counter += 1
            child_path = path + "/" + child
            print(child_path)
            watch_children(child_path)
            


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
        print("exists")
        # if zk.get_children("/z") != []:
            # print(zk.get_children("z"))
            # watch_children_2("/z")
        kids = zk.get_children("/z")
        if kids != []:
            path = "/z"
            @zk.ChildrenWatch("/z")
            def watch_children(path: str):
                print(path)
                children = zk.get_children("z/" + path)
                print(children)
                print(len(children))
                for child in children:
                    path = path + "/" + child
                    watch_children(path)






            
while True:
    time.sleep(5)
        