Run the program by these steps below.
*Note: Make sure you have run script attach to create database server, run server postgesSQL, create some person, open pgsql and install psycopg2, django before do this.



1. Install gRPC and gRPC tools:
	$ python -m pip install grpcio
	$ python -m pip install grpcio-tools
	
2. Run to test call server
	$ python server.py
	open another cmd in web folder 
	$ python client.py

3. Run web app
	open web folder that contain manage.py
	$ python manage.py runserver
	open http://127.0.0.1:8000/ to see result

*Note, try username: '51703124' and password: 'password' to make success login.