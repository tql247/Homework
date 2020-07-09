from __future__ import print_function
import logging

import grpc

import purchase_pb2
import purchase_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = purchase_pb2_grpc.MakeOrderStub(channel)

        # add order
        stub.addOrder(purchase_pb2.Request(message='1000;51703124'))
        stub.addOrder(purchase_pb2.Request(message='1001;51703092'))

        # get order list 
        order_list = stub.getOrder(purchase_pb2.Request(message=''))
        print(order_list.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
