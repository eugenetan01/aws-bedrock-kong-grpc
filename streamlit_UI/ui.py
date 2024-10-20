import grpc
import streamlit as st
from ragservice import rag_pb2, rag_pb2_grpc

def run(prompt, data_plane_node):
    with grpc.insecure_channel(data_plane_node) as channel:
        stub = rag_pb2_grpc.RagServiceStub(channel)
        response = stub.RagTemplate(rag_pb2.RagRequest(prompt=prompt, data_plane_node=data_plane_node))
    return response.message

def main():

    if "data_plane_node" not in st.session_state:
        st.session_state["data_plane_node"] = ""

    st.title("gRPC Client with Kong Proxy")

    data_plane_node = st.text_input("Enter data plane hostname:")

    prompt = st.text_input("Enter your prompt:", "How will AI change our every day lives?")

    if st.button("Send Request"):
        st.session_state["data_plane_node"] = data_plane_node
        with st.spinner("Waiting for the server response..."):
            response = run(prompt, data_plane_node)
        st.write("Client received: " + response)

if __name__ == '__main__':
    main()
