from __future__ import print_function
import logging

import grpc

import book_pb2
import book_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookShelfStub(channel)
        # load data
        stub.loadData(book_pb2.Request(name='', id=''))
        # add books
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 1', id='TV1'))
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 2', id='TV2'))
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 3', id='TV3'))
        # get book list 
        book_list = stub.getBooks(book_pb2.Request(name='', id=''))
        print(book_list.message)
        # remove
        stub.remove(book_pb2.Request(name='', id='TV1'))
        # get book list 
        book_list = stub.getBooks(book_pb2.Request(name='', id=''))
        print(book_list.message)
        # remove all
        stub.removeAll(book_pb2.Request(name='', id=''))
        # get book list 
        book_list = stub.getBooks(book_pb2.Request(name='', id=''))
        print(book_list.message)
        # add other books
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 4', id='TV4'))
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 5', id='TV5'))
        stub.addBook(book_pb2.Request(name='Tieng Viet tap 7', id='TV6'))
        # edit
        stub.edit(book_pb2.Request(name='Tieng Viet tap 6', id='TV6'))
        # get book list 
        book_list = stub.getBooks(book_pb2.Request(name='', id=''))
        print(book_list.message)
        # find
        book_list = stub.find(book_pb2.Request(name='', id='TV4'))
        print(book_list.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
