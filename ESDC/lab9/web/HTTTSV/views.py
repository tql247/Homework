from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import psycopg2


database = "HTTTSV"
user = "postgres"
password = "password"
host = "localhost"
port = "5432"
status = "false"


def home(request):
    return render(request, 'home.html')


def login(request):
    username = request.POST['username']
    pwd = request.POST['pwd']



    # Set up a connection to the BookShelf server
    con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    # Create a cursor object
    cur = con.cursor()
    
    # Create parameter

    # Query
    query = '''SELECT count(*) FROM account WHERE "ID" = '{}' AND "Password" = '{}' '''.format(username, pwd)
    cur.execute(query);
    status = cur.fetchone()[0]

    # Commit the current transaction
    con.commit()
    # Close server
    con.close()


    if status != 1:
        return home(request)        
    else:
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        
        # Create a cursor object
        cur = con.cursor()

        query = '''SELECT * FROM student WHERE "ID" = '{}' '''.format(username)
        cur.execute(query)
        
        
        res = cur.fetchall()
        response = ",".join(res[0])


        # Commit the current transaction
        con.commit()
        # Close server
        con.close()


        return render(request, 'result.html', {'response': response})