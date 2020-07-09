import grpc
import logging
import psycopg2
import student_pb2
import student_pb2_grpc
from concurrent import futures



# define connection
database = "HTTTSV"
user = "postgres"
password = "password"
host = "localhost"
port = "5432"
status = "false"

print("Server is running!")

class server_HTTTSV(student_pb2_grpc.HTTTSVServicer):

    def login(self, request, context):
        global status

        cmd = request.message.split(";")

        # Set up a connection to the BookShelf server
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor()
        
        # Create parameter
        username = cmd[0]
        pwd = cmd[1]

        # Query
        query = '''SELECT count(*) FROM account WHERE "ID" = '{}' AND "Password" = '{}' '''.format(username, pwd)
        cur.execute(query);


        if cur.fetchone()[0] == 1:
            status = "true"
        else:
            status = 'false'

        # Commit the current transaction
        con.commit()
        # Close server
        con.close()
        
        print('Login request!')
        return student_pb2.Response(message=status)

 

    def view_profile(self, request, context):

        if status != "true":
            return student_pb2.Response(message='Fail!')


        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor()

        query = '''SELECT * FROM student WHERE "ID" = '{}' '''.format(request.message)
        cur.execute(query)
        
        
        res = cur.fetchall()
        response = ",".join(res[0])


        # Commit the current transaction
        con.commit()
        # Close server
        con.close()
        
        return student_pb2.Response(message=response)

   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    student_pb2_grpc.add_HTTTSVServicer_to_server(server_HTTTSV(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
