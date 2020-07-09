from concurrent import futures
import logging

import grpc

import book_pb2
import book_pb2_grpc
from book import Book


class BookShelf(book_pb2_grpc.BookShelfServicer):
    bs = list()


    def addBook(self, request, context):
        b = Book(request.name, request.id)
        self.bs.append(b)
        print("Book added!")
        self.save()
        return book_pb2.Response(message='Book %s added!' % b.getName())

    def getBooks(self, request, context):
        book_list = list()
        for b in self.bs:
            book_list.append(b.getName() + '-' + b.getId())
        response = ','.join([str(e) for e in book_list])
        print("Get book list!")
        return book_pb2.Response(message=response)

    def remove(self, request, context):
        id = request.id
        for b in self.bs:
            if b.getId() == id:
                self.bs.remove(b)
                print("Removed!")
                self.save()
                return book_pb2.Response(message="Removed!")

    def removeAll(self, request, context):
        self.bs.clear()
        print("All removed!")
        self.save()
        return book_pb2.Response(message="All removed!")

    def edit(self, request, context):
        id = request.id
        new_name = request.name
        for b in self.bs:
            if b.getId() == id:
                b.edit(new_name)
                print("Edited!")
                self.save()
                return book_pb2.Response(message="Edited!")

    def find(self, request, context):
        name = request.name
        id = request.id
        result = list()
        for b in self.bs:
            if b.getId() == id or b.getName() == name:
                result.append(b.getName() + "-" + b.getId())
        msg = ",".join([e for e in result])
        print("Search!")
        return book_pb2.Response(message=msg)

    def save(self):
        with open("data.txt", "w") as f:
            for b in self.bs:
                f.write(b.getName() + "," + b.getId() + "\n")

    def loadData(self, request, context):
        with open("data.txt", "r") as f:
            for line in f:
                line = line.strip()
                name = line.split(",")[0]
                id = line.split(",")[1]
                b = Book(name, id)
                self.bs.append(b)
        print("Data loaded!")
        return book_pb2.Response(message="Data loaded!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookShelfServicer_to_server(BookShelf(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
