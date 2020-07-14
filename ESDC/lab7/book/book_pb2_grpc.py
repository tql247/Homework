# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import book_pb2 as book__pb2


class BookShelfStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addBook = channel.unary_unary(
        '/book.BookShelf/addBook',
        request_serializer=book__pb2.Request.SerializeToString,
        response_deserializer=book__pb2.Response.FromString,
        )
    self.getBooks = channel.unary_unary(
        '/book.BookShelf/getBooks',
        request_serializer=book__pb2.Request.SerializeToString,
        response_deserializer=book__pb2.Response.FromString,
        )


class BookShelfServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addBook(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getBooks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BookShelfServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addBook': grpc.unary_unary_rpc_method_handler(
          servicer.addBook,
          request_deserializer=book__pb2.Request.FromString,
          response_serializer=book__pb2.Response.SerializeToString,
      ),
      'getBooks': grpc.unary_unary_rpc_method_handler(
          servicer.getBooks,
          request_deserializer=book__pb2.Request.FromString,
          response_serializer=book__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'book.BookShelf', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))