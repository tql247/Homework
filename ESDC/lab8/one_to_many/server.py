import grpc
import logging
import psycopg2
import purchase_pb2
import purchase_pb2_grpc
from datetime import date
from concurrent import futures



# define connection
database = "Purchase"
user = "postgres"
password = "password"
host = "localhost"
port = "5432"

print("Server is running!")

class Manager(purchase_pb2_grpc.MakeOrderServicer):

    def addOrder(self, request, context):
        cmd = request.message.split(";")

        # Set up a connection to the BookShelf server
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor()
        
        # Create parameter
        cur.execute("SELECT COUNT(*) FROM order_catalog")
        order_id = cur.fetchone()[0] + 1
        today = date.today().strftime("%Y-%m-%d")
        cost = int(cmd[0])
        customer_id = int(cmd[1]) 

        # Query
        query = '''INSERT INTO order_catalog("Order_ID", "Order_Date", "Cost", "Customer_ID") VALUES ({}, '{}', {}, {})'''.format(order_id, today, cost, customer_id)
        cur.execute(query);

        # print(query)
        # Commit the current transaction
        con.commit()
        # Close server
        con.close()
        
        print('Order added!')
        return purchase_pb2.Response(message='Order added!')

 

    def getOrder(self, request, context):
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor() 
        cur.execute("SELECT * from order_catalog")
        response = cur.fetchall()
        # Commit the current transaction
        con.commit()
        # Close server
        con.close()
        
        
        result_string = ""
        for i in response:
            result_string += "[id={}, date={}, cost={}, customer={}]".format(i[0], i[1], i[2], i[3])
        
        return purchase_pb2.Response(message=result_string)

   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    purchase_pb2_grpc.add_MakeOrderServicer_to_server(Manager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
