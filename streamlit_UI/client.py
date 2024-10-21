import grpc
from ragservice import rag_pb2, rag_pb2_grpc

def run():
    # Point to Kong instead of the gRPC server directly
    with grpc.insecure_channel('ec2-54-174-168-39.compute-1.amazonaws.com:50051') as channel:
        stub = rag_pb2_grpc.RagServiceStub(channel)
        response = stub.RagTemplate(rag_pb2.RagRequest(prompt='How will AI change our every day lives?',data_plane_node="ec2-54-174-168-39.compute-1.amazonaws.com:8000"))
    print("Client received: " + response.message)

if __name__ == '__main__':
    run()
