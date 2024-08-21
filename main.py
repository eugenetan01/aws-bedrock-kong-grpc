import uvicorn
from fastapi import FastAPI
from concurrent import futures
import grpc
from ragservice import rag_pb2, rag_pb2_grpc
import rag

class RagService(rag_pb2_grpc.RagServiceServicer):
    def RagTemplate(self, request, context):
        response = rag_pb2.RagReply()
        # response.message = request.prompt
        response.message = rag.rag_flow(request.prompt)
        return response


def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rag_pb2_grpc.add_RagServiceServicer_to_server(RagService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    import threading
    grpc_thread = threading.Thread(target=serve_grpc)
    grpc_thread.start()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1000)
