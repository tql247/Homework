Build gRPC Basics

1. Install gRPC and gRPC tools:
	$ python -m pip install grpcio
	$ python -m pip install grpcio-tools

*Note: You can skip step 2,3,4,5 to get a quick start.

2. Create folder "Student_management" (Already have sample) and cd to that.
3. Create Student_management.proto file (Already have sample).
4. Define the service (Already have sample).
5. Define the client (Already have sample).

6. Generate python code:
	$ python -m grpc_tools.protoc -I../Student_management --python_out=. --grpc_python_out=. ../Student_management/Student_management.proto
	
7. Run
	$ python Server.py
	open another cmd
	$ python Client.py
	