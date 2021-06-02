
from __future__ import print_function
import logging

import grpc
import threading

import helloworld_pb2 as helloworld_pb2
import helloworld_pb2_grpc as helloworld_pb2_grpc





def run():

    subscription = helloworld_pb2.Subscription(name="Bob")

    try:
        while True:
            with grpc.insecure_channel('0.0.0.0:50051') as channel:
                stub = helloworld_pb2_grpc.NotificatorStub(channel)

                try:
                    iterator = stub.subscribe(subscription)
                    for notification in iterator:
                        print(notification)

                    print('Server disconnected gracefully')

                except grpc.RpcError as e:
                    status_code = e.code()

                    if e.details() == 'Stream removed':
                        print('Server disconnected, trying to reconnect...')

                    elif status_code == grpc.StatusCode.UNAVAILABLE:
                        print('Server unavailable')

                    else:
                        print(e)
                        raise SystemExit

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()

# def subscribe(stub):
#     print("SUBSCRIBE")
#     pack = helloworld_pb2.Subscription()
#     result = stub.subscribe(pack, wait_for_ready = True)
#     print(result)
#     listen(stub)



# def listen(stub):
#     print("LISTEN")
#     thread = threading.Thread(target = callback, args=(stub))
#     thread.start()


# def callback(stub):
#     try:
#         print("CALLBACK")
#         result = stub.listen(helloworld_pb2.SubscriptionRequest())

#         for notification in result:
#             print(notification)
#             print("lol")
#     except:
#         print("Error in callback")


# if __name__ == '__main__':
#     logging.basicConfig()
#     run()
