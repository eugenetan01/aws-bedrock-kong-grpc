# Pre-requisites

__1. If having issues with aws cli, delete the contents in `~/.aws/credentials` and go to okta tile "AWS - Kong" -> click "Access Keys" and copy paste "Option 2: Add a profile to your AWS credentials file" into the `~/.aws/credentials` file__

__2. Test if it's working by running `aws s3 ls` - you should see a list of s3 buckets in terminal_

# Setup

__1. run the `pip3 install -r requirements.txt`__

__2. run the below command to generate the necessary protocol buffers__
  `python -m grpc_tools.protoc -I. --python_out=./helloworld --grpc_python_out=./helloworld hello.proto`

__3. change the import statement to `from . import hello_pb2 as hello__pb2` instead of `import hello_pb2 as hello__pb2` in the hello_pb2_grpc.py file__

<<<<<<< HEAD
=======
__4. run the main.py__
  `python3 main.py`

__5. test the client connectivity by connecting to the grpc server and ensuring it connects to localhost:50051 instead of 9080__
  `python3 client.py`

>>>>>>> 50dd75696e335440f94d4f6af5f5c1cafd0064cf
__4. create a docker container for the kong gateway. use the below to spin up the docker image__
  ```
  docker run -d --name kong-gateway \
  --network=kong-net \
  -e "KONG_DATABASE=postgres" \
  -e "KONG_PG_HOST=kong-database" \
  -e "KONG_PG_USER=kong" \
  -e "KONG_PG_PASSWORD=kongpass" \
  -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
  -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
  -e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
  -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
  -e "KONG_ADMIN_LISTEN=0.0.0.0:8001" \
  -e "KONG_ADMIN_GUI_URL=http://localhost:8002" \
  -e "KONG_PROXY_LISTEN=0.0.0.0:9080 http2, 0.0.0.0:9081 http2 ssl" \
  -e KONG_LICENSE_DATA \
  -p 8000:8000 \
  -p 8443:8443 \
  -p 8001:8001 \
  -p 8444:8444 \
  -p 8002:8002 \
  -p 8445:8445 \
  -p 8003:8003 \
  -p 8004:8004 \
  -p 9080:9080 \
  kong/kong-gateway:3.7.1.2
  ```

__5. Create a service and route__
  ```
  curl -XPOST localhost:8001/services \
    --data name=grpc \
    --data protocol=grpc \
    --data host=host.docker.internal \
    --data port=50051
  ```

  ```
  curl -XPOST localhost:8001/services/grpc/routes \
    --data protocols=grpc \
    --data name=catch-all \
    --data paths=/
  ```

<<<<<<< HEAD
__6. In the first step we will launch an OpenSearch cluster using Terraform.__

      ```bash
      cd ./terraform
      terraform init
      terraform apply -auto-approve
      ```

      >>This cluster configuration is for testing proposes only, as it's endpoint is public for simplifying the use of this sample code.

__7. Now that we have a running OpenSearch cluster with vector engine support we will start uploading our data that will help us with prompt engineering. For this sample, we will use a data source from [Hugging Face](https://huggingface.co) [embedding-training-data](https://huggingface.co/datasets/sentence-transformers/embedding-training-data) [gooaq_pairs](https://huggingface.co/datasets/sentence-transformers/embedding-training-data/resolve/main/gooaq_pairs.jsonl.gz), we will download it, and invoke Titan embedding to get a text embedding, that we will store in OpenSearch for next steps.__

    ```bash
    python load-data-to-opensearch.py --recreate 1 --early-stop 1
    ```

    >>Optional arguments:
    >>- `--recreate` for recreating the index in OpenSearch
    >>- `--early-stop` to load only 100 embedded documents into OpenSearch
    >>- `--index` to use a different index than the default **rag**
    >>- `--region` in case you are not using the default **us-east-1**

__8. run the main.py__
  `python3 main.py`

__9. test the client connectivity by connecting to the grpc server and ensuring it connects to localhost:50051 instead of 9080__
  - run `python3 client.py`
  - you should see a response from LLM in console

# Notes

- Bedrock code [sample](https://github.com/aws-samples/rag-using-langchain-amazon-bedrock-and-opensearch)
