from __future__ import print_function
import logging

import grpc

import Student_management_pb2
import Student_management_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Student_management_pb2_grpc.ManagementStub(channel)
        # create student
        stub.create(Student_management_pb2.Request(req='student-Linh-1999-True'))
        stub.create(Student_management_pb2.Request(req='student-Hoang-1999-True'))
        stub.create(Student_management_pb2.Request(req='student-Duy-1999-True'))
        
        # create course
        stub.create(Student_management_pb2.Request(req='course-EDSC-4'))
        stub.create(Student_management_pb2.Request(req='course-DAA-3'))
        stub.create(Student_management_pb2.Request(req='course-CDA-3'))

        #view list all
        # print(stub.ls_all(Student_management_pb2.Request(req='student')).res)
        # print(stub.ls_all(Student_management_pb2.Request(req='course')).res)

        # update
        # stub.update(Student_management_pb2.Request(req='student-2-Zuy-1999-False'))
        # stub.update(Student_management_pb2.Request(req='course-2-CDA-4'))

        # check update 
        # print(stub.ls_all(Student_management_pb2.Request(req='student')).res)
        # print(stub.ls_all(Student_management_pb2.Request(req='course')).res)

        #delete
        stub.delete(Student_management_pb2.Request(req='course-2'))

        # check update 
        # print(stub.ls_all(Student_management_pb2.Request(req='student')).res)
        # print(stub.ls_all(Student_management_pb2.Request(req='course')).res)

        # register
        stub.register(Student_management_pb2.Request(req='0-0'))
        stub.register(Student_management_pb2.Request(req='0-1'))
        stub.register(Student_management_pb2.Request(req='1-1'))
        stub.register(Student_management_pb2.Request(req='2-1'))
        
        # view list student at specific course
        print(stub.list(Student_management_pb2.Request(req='course-1')).res)
        print(stub.list(Student_management_pb2.Request(req='student-0')).res)


if __name__ == '__main__':
    logging.basicConfig()
    run()