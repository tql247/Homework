import grpc
import logging
import psycopg2
import reg_pb2
import reg_pb2_grpc
from datetime import date
from concurrent import futures



# define connection
database = "Reg"
user = "postgres"
password = "password"
host = "localhost"
port = "5432"

print("Server is running!")

class Manager(reg_pb2_grpc.RegServicer):

    def create_passport(self, request, context):
        cmd = request.message.split(";")

        # Set up a connection to the BookShelf server
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor()
        
        # Create parameter
        passport_id = int(cmd[0])
        valid_date = cmd[1]
        country = cmd[2]

        # Query
        query = '''INSERT INTO Passport("Passport_ID", "Valid_Date", "Country_of_Issue") VALUES ({}, '{}', '{}')'''.format(passport_id, valid_date, country)
        cur.execute(query);

        # Commit the current transaction
        con.commit()
        # Close server
        con.close()
        
        print('Created!')
        return reg_pb2.Response(message='Created!')

    
    def add_to_person(self, request, context):
        cmd = request.message.split(";")

        # Set up a connection to the BookShelf server
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor()

        # Create parameter
        passport_id = int(cmd[0])
        person_id = int(cmd[1])

        # Query
        query = '''UPDATE Person SET "Passport_ID" = {} WHERE "Person_ID" = {};'''.format(passport_id, person_id)
        cur.execute(query);


        # Commit the current transaction
        con.commit()
        # Close server
        con.close()

        return reg_pb2.Response(message='Added!')

    
 

    def getlist(self, request, context):
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor() 
        cur.execute("SELECT * from person")
        response = cur.fetchall()
        # Commit the current transaction
        con.commit()
        # Close server
        con.close()
        
        
        result_string = ""
        for i in response:
            result_string += "[id={}, First_Name={}, Last_Name={}, DOB={}, country={}, passport_id={}]".format(i[0], i[1], i[2], i[3], i[4], i[5])
        
        return reg_pb2.Response(message=result_string)

   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reg_pb2_grpc.add_RegServicer_to_server(Manager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
