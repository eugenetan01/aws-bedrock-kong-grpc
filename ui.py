import grpc
import streamlit as st
from ragservice import rag_pb2, rag_pb2_grpc

def run(prompt):
    with grpc.insecure_channel('localhost:9080') as channel:
        stub = rag_pb2_grpc.RagServiceStub(channel)
        response = stub.RagTemplate(rag_pb2.RagRequest(prompt=prompt))
    return response.message

def main():
    st.title("gRPC Client with Kong Proxy")

    prompt = st.text_input("Enter your prompt:", "How will AI change our every day lives?")

    if st.button("Send Request"):
        with st.spinner("Waiting for the server response..."):
            response = run(prompt)
        st.write("Client received: " + response)

if __name__ == '__main__':
    main()
