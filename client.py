import grpc
from ragservice import rag_pb2, rag_pb2_grpc

def run():
    # Point to Kong instead of the gRPC server directly
    with grpc.insecure_channel('localhost:9080') as channel:
        stub = rag_pb2_grpc.RagServiceStub(channel)
        response = stub.RagTemplate(rag_pb2.RagRequest(prompt='How will AI change our every day lives?'))
    print("Client received: " + response.message)

if __name__ == '__main__':
    run()
