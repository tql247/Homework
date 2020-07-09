from __future__ import print_function
import logging

import grpc

import book_pb2
import book_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookShelfStub(channel)

        # add books
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 1'))
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 2'))
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 3'))
        # get book list 
        book_list = stub.getBooks(book_pb2.Request(name=''))
        print(book_list.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
