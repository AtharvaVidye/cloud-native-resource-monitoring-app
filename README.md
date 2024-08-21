# Cloud Native Resource Monitoring Python App on K8s

This project demonstrates how to create a cloud-native resource monitoring application using Python, Flask, and psutil, and deploy it on a Kubernetes (K8s) cluster using Docker and AWS EKS.

## 📚 What You'll Learn
- **Python**: How to create a monitoring application using Flask and psutil.
- **Docker**: How to containerize a Python application, create a Dockerfile, build a Docker image, and push it to AWS ECR.
- **Kubernetes**: How to create an EKS cluster, deploy the Dockerized Flask application, and manage services using Python.

## 🚀 Prerequisites
- **AWS Account** with programmatic access and AWS CLI configured.
- **Python 3** installed.
- **Docker** and **Kubectl** installed.
- **Code Editor** (e.g., VSCode).

## 🛠️ Project Setup

### Part 1: Deploying the Flask Application Locally

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
2. **Install Dependencies:**:
   ```bash
   pip3 install -r requirements.txt
3. **Run the Application:**
   ```bash
   python app.py
The Flask server will start on http://localhost:5000

### Part 2: Dockerizing the Flask Application

**Option 1: Using the Pre-built Docker Image**:
1. **Pull the Docker Image**:

   ```bash
   docker pull atharvav/system_monitoring_app

2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 atharvav/system_monitoring_app
This will start the Flask server in a Docker container on http://localhost:5000.

**Option 2: Building Your Own Docker Image**:

1. **Create a Dockerfile in the root directory**:
   ```bash
    FROM python:3.9-slim-buster
    WORKDIR /app
    COPY requirements.txt .
    RUN pip3 install --no-cache-dir -r requirements.txt
    COPY . .
    ENV FLASK_RUN_HOST=0.0.0.0
    EXPOSE 5000
    CMD ["flask", "run"]
  
2. **Build the Docker Image**:
   ```bash
   docker build -t <image_name> .

2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 <image_name>
This will start the Flask server in a Docker container on http://localhost:5000.




### Part 3: Pushing the Docker Image to ECR
1. **Create an ECR Repository using Python**:
   ```bash
    import boto3
    
    ecr_client = boto3.client('ecr')
    response = ecr_client.create_repository(repositoryName='my-ecr-repo')
    repository_uri = response['repository']['repositoryUri']
    print(repository_uri)

2. **Push the Docker Image to ECR**:
   ```bash
    docker tag <image_name>:latest <ecr_repo_uri>:latest
    docker push <ecr_repo_uri>:latest

### Part 4: Deploying on EKS
1. **Create an EKS Cluster and Node Group**:
2. **Create Deployment and Service using Python**:
   ```bash
    from kubernetes import client, config
    
    config.load_kube_config()
    api_client = client.ApiClient()
    
    deployment = client.V1Deployment(
        metadata=client.V1ObjectMeta(name="my-flask-app"),
        spec=client.V1DeploymentSpec(
            replicas=1,
            selector=client.V1LabelSelector(match_labels={"app": "my-flask-app"}),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "my-flask-app"}),
                spec=client.V1PodSpec(
                    containers=[client.V1Container(
                        name="my-flask-container",
                        image="<your_ecr_repo_uri>:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )]
                )
            )
        )
    )
    
    api_instance = client.AppsV1Api(api_client)
    api_instance.create_namespaced_deployment(namespace="default", body=deployment)
    
    service = client.V1Service(
        metadata=client.V1ObjectMeta(name="my-flask-service"),
        spec=client.V1ServiceSpec(
            selector={"app": "my-flask-app"},
            ports=[client.V1ServicePort(port=5000)]
        )
    )
    
    api_instance.create_namespaced_service(namespace="default", body=service)

3. **Check Deployment and Service:**:
   ```bash
    kubectl get deployment -n default
    kubectl get service -n default
    kubectl get pods -n default
   
3. **Expose the Service**:
   ```bash
    kubectl port-forward service/<service_name> 5000:5000
   
📷 Screenshots

**Docker Hub Image**:
![Alt text](https://github.com/AtharvaVidye/cloud-native-resource-monitoring-app/blob/main/images/Docker%20Hub%20Image.png)

🎥 Video

[![Video Thumbnail](https://img.youtube.com/vi/l7yWwymdy6Y/0.jpg)](https://www.youtube.com/watch?v=l7yWwymdy6Y)

👤 **Author**  
Atharva Vidye  
Email: [atharvavidye2001@gmail.com](mailto:atharvavidye2001@gmail.com)  
LinkedIn: [Atharva Vidye](https://www.linkedin.com/in/atharva-vidye-1771541a4/)
