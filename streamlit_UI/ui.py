import grpc
import streamlit as st
from ragservice import rag_pb2, rag_pb2_grpc

def run(prompt, data_plane_node):
    with grpc.insecure_channel(data_plane_node) as channel:
        stub = rag_pb2_grpc.RagServiceStub(channel)
        response = stub.RagTemplate(
            rag_pb2.RagRequest(prompt=prompt, data_plane_node=data_plane_node)
        )
    return response.message

def main():
    if "data_plane_node" not in st.session_state:
        st.session_state["data_plane_node"] = ""

    st.title("gRPC Client with Kong Proxy")

    # Capture and validate data_plane_node input
    data_plane_node = st.text_input(
        "Enter data plane hostname:",
        value=st.session_state.get("data_plane_node", "")  # Use default or stored value
    )

    prompt = st.text_input(
        "Enter your prompt:",
        "How will AI change our every day lives?"
    )

    if st.button("Send Request"):
        if not data_plane_node:  # Add validation to prevent empty input
            st.error("Data plane hostname cannot be empty.")
            return

        st.session_state["data_plane_node"] = data_plane_node

        with st.spinner("Waiting for the server response..."):
            try:
                response = run(prompt, data_plane_node)
                st.write("Client received: " + response)
            except grpc.RpcError as e:
                st.error(f"gRPC Error: {e.details()}")

if __name__ == '__main__':
    main()
