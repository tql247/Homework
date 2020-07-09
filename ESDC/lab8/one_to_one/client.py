from __future__ import print_function
import logging

import grpc

import reg_pb2
import reg_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = reg_pb2_grpc.RegStub(channel)

        # create passport
        stub.create_passport(reg_pb2.Request(message='5121;"20-02-2019";"VN"'))

        # add order
        stub.add_to_person(reg_pb2.Request(message='5121;51703124'))

        # get order list 
        order_list = stub.getlist(reg_pb2.Request(message=''))
        print(order_list.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
