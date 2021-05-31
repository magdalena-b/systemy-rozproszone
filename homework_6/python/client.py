
from __future__ import print_function
import logging

import grpc

import helloworld_pb2 as helloworld_pb2
import helloworld_pb2_grpc as helloworld_pb2_grpc


def subscribe():
    pack = helloworld_pb2.Subscription()
    result = stub.subscribe(pack, wait_for_ready = True)

def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = helloworld_pb2_grpc.SubProviderStub(channel)
        subscribe()


if __name__ == '__main__':
    logging.basicConfig()
    run()
