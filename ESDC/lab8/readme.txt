Run the program by these steps below.
*Note: Make sure you have run script attach to create database server, create some person, and install psycopg2 before do this.


1. Install gRPC and gRPC tools:
	$ python -m pip install grpcio
	$ python -m pip install grpcio-tools

2. Generate python code:
	$ python -m grpc_tools.protoc -I../<folder_name> --python_out=. --grpc_python_out=. ../<folder_name>/<file_name>.proto
	
3. Run
	$ python server.py
	open another cmd
	$ python client.py
	