import time
import subprocess
import os
import signal

from kazoo.client import KazooClient
from kazoo.protocol.states import WatchedEvent, EventType

zk = KazooClient(hosts = '127.0.0.1:2181')
zk.start(timeout = 60)
app = None

def print_and_count_children(path):
    print(path)
    children = zk.get_children(path)
    count = 1
    for child in children:
        count += print_and_count_children(path + "/" + child)
    return count


def handle_event_in_kids(event):
    print("Event: " + str(event.type))
    # have to reset handler after very trigger
    set_handler_in_children(event.path)
    if zk.exists("/z"):
        count = print_and_count_children("/z")
        print("Children count = ", count-1)


def set_handler_in_children(path):
    if zk.exists(path):
        # watches updates in children set (also if children == [])
        children = zk.get_children(path, watch = handle_event_in_kids)
        for child in children:
            set_handler_in_children(path + "/" + child)

@zk.DataWatch("/z")
def handle_exist(data, stat, event: WatchedEvent):
    global app
    if event:
        if event.type == EventType.CREATED:
            print_and_count_children("/z")
            zk.get_children("/z", watch = handle_event_in_kids)
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


    if zk.exists("/z"):
        count = print_and_count_children("/z")
        print("Children count = ", count - 1)
        set_handler_in_children("/z")

while True:
    time.sleep(5)
