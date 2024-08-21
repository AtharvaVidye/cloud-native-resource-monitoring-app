import boto3

# Specify the region
ecr_client = boto3.client('ecr', region_name='us-east-1')

repository_name = "my_monitoring_app_image"

try:
    response = ecr_client.create_repository(repositoryName=repository_name)
    repository_uri = response['repository']['repositoryUri']
    print(f"Repository URI: {repository_uri}")
except ecr_client.exceptions.RepositoryAlreadyExistsException:
    print(f"The repository '{repository_name}' already exists.")
except Exception as e:
    print(f"An error occurred: {e}")