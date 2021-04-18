import time
import subprocess

from kazoo.client import KazooClient
from kazoo.protocol.states import WatchedEvent, EventType

zk = KazooClient(hosts = '127.0.0.1:2181')
zk.start(timeout = 60)
app = None


def handle_update(event):
    register_watch(event.path)
    if zk.exists("/z"):
        count = print_children("/z")
        print("Children count = ", count-1)

def print_children(path):
    print(path)
    children = zk.get_children(path)
    count = 1
    for child in children:
        count += print_children(path + "/" + child)
    return count

def register_watch(path):
    if zk.exists(path):
        update_handler = lambda event: handle_update(event)
        children = zk.get_children(path, watch = update_handler)
        for child in children:
            register_watch(path + "/" + child)

@zk.DataWatch("/zk")
def handle_exist(data, stat, event: WatchedEvent):
    update_handler = lambda event: handle_update(event)
    if event:
        print(event)
        if event.type == EventType.CREATED:
            print_children("/zk")
            zk.get_children("/zk", watch = update_handler)
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
        count = print_children("/z")
        print("Children count = ", count - 1)
        register_watch("/z")

while True:
    time.sleep(5)
