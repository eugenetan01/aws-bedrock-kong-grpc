## Pre-requisites:
- create an EC2 instance
- install docker - [link](https://medium.com/@srijaanaparthy/step-by-step-guide-to-install-docker-on-amazon-linux-machine-in-aws-a690bf44b5fe)

## Setup
`docker buildx create --use`
`docker buildx build --platform linux/amd64 -t grpc-streamlit-app --load .`
`docker image inspect grpc-streamlit-app | grep Architecture`

__Docker:__
`docker tag grpc-streamlit-app:latest eugenetan0/kong-ai-gateway-workshop-grpc-streamlit-app`
`docker push eugenetan0/kong-ai-gateway-workshop-grpc-streamlit-app:latest`

__EC2:__
`docker run -d -p 8080:8501 eugenetan0/kong-ai-gateway-workshop-grpc-streamlit-app:latest`
