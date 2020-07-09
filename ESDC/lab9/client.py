from __future__ import print_function
import logging

import grpc

import student_pb2
import student_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = student_pb2_grpc.HTTTSVStub(channel)

        status = stub.login(student_pb2.Request(message='51703124;password'))
        print(status.message) #if status.message = true then enter index.html


        # view infor, redicrect to profile.html
        infor = stub.view_profile(student_pb2.Request(message='51703124'))
        print(infor) # show infor on web page


if __name__ == '__main__':
    logging.basicConfig()
    run()
