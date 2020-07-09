Build gRPC Basics

1. Install gRPC and gRPC tools:
	$ python -m pip install grpcio
	$ python -m pip install grpcio-tools

*Note: You can skip step 2,3,4,5 to get a quick start.

2. Create folder "book" (Already have sample) and cd to that.
3. Create book.proto file (Already have sample).
4. Define the service (Already have sample).
5. Define the client (Already have sample).

6. Generate python code:
	$ python -m grpc_tools.protoc -I../book --python_out=. --grpc_python_out=. ../book/book.proto
	
7. Run
	$ python book_server.py
	open another cmd
	$ python book_client.py
	