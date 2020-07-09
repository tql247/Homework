from concurrent import futures
import logging

import grpc

import book_pb2
import book_pb2_grpc
from book import Book
import psycopg2


# define connection
database = "BookShelf"
user = "postgres"
password = "password"
host = "localhost"
port = "5432"


class BookShelf(book_pb2_grpc.BookShelfServicer):

    def addBook(self, request, context):
        # Set up a connection to the BookShelf server
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor()
        
        # Get current book id
        cur.execute("SELECT COUNT(id) FROM book")
        book_id = cur.fetchone()[0] + 1
        name = request.name
        
        # Query
        query = "INSERT INTO book(id, name) VALUES ({},'{}')".format(book_id, name)
        cur.execute(query);

        # Commit the current transaction
        con.commit()
        # Close server
        con.close()
        
        print('Book %s added!' % request.name)
        return book_pb2.Response(message='Book %s added!' % request.name)

        # Set up a connection to the BookShelf server
 

    def getBooks(self, request, context):
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor() 
        cur.execute("SELECT * from book")
        response = cur.fetchall()
        # Commit the current transaction
        con.commit()
        # Close server
        con.close()
        
        
        result_string = ""
        for i in response:
            result_string += "[id={}, name={}]".format(i[0], i[1])
        
        return book_pb2.Response(message=result_string)

   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookShelfServicer_to_server(BookShelf(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
