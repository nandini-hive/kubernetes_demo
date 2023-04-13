# Kubernetes Demo: 

Deploying a simple Flask api application on a minikube cluster
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

# #Prerequisites:

1. Docker Installed in your system
2. Up and running Minikube cluster

- To install minikube: brew install minikube
- To start the minikube cluster with docker as a driver: minikube start –driver docker
- To check minikube cluster status: minikube status

# # Lets get started

# # Creating Python virtual environment
- python3 -m venv ./venv
- source ./venv/bin/activate

# # PIP installations in virtual environment
- pip install fastapi
- pip install uvicorn

# # # To check all the packages installed
- pip freeze

## Description 

`requirements.txt`:
Latest versions of fastapi and uvicorn

- pip install -r requirements.txt

`app/main.py`:
This FastAPI application file returns the Hostname and Environment variabe set the container pod.

# # # We can test the application locally using the below command

- uvicorn main:app --reload

# #Steps to build and push the container image in Dockerhub

Using 'Dockerfile'

- docker build -t Yourdockerhubrepo/imagename:tagname

- docker push Yourdockerhubrepo/imagename:tagname

# #Kubernetes Configuration files

All the kubernetes configuration files are in the folder ./Kubernetes

`app/deployment.yaml`:
Deployment spec for containers should be updated in case you trying a different container image.


### To create all the components in the configuration files together

- kubectl apply -f .

# # #To check all the resources created 

- kubectl get all

# # #To enter the pod container we can use the below command 

- kubectl exec -it podname bash

# # #To exit the pod container we can use the below command 
- exit

# # #Deleting any resource
kubectl delete resource name

# # #Forward a local port to a port on the Pod
kubectl port-forward allows using resource name, such as a pod name, to select a matching pod to port forward to.
Connections made to local port 8080 are forwarded to port 80 of the Pod

- kubectl port-forward podname 8080:80

# # #Accessing our application

- http://localhost:8080/

