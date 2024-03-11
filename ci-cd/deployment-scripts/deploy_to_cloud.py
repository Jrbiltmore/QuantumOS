import boto3
import subprocess
import os

# AWS Configuration
aws_profile = 'default'  # The AWS profile to use
ecs_cluster_name = 'YourECSCluster'  # Name of the ECS cluster
service_name = 'YourServiceName'  # Name of the ECS service
image_name = 'your-image-name:latest'  # Docker image name:tag
repository_name = 'your-repository'  # ECR repository name

# Initialize a session using Boto3
session = boto3.Session(profile_name=aws_profile)
ecs_client = session.client('ecs')
ecr_client = session.client('ecr')

def build_and_push_image():
    """
    Build a Docker image from the Dockerfile and push it to ECR.
    """
    # Retrieve an authentication token and authenticate your Docker client to your registry.
    auth_response = ecr_client.get_authorization_token()
    token = auth_response['authorizationData'][0]['authorizationToken']
    registry_url = auth_response['authorizationData'][0]['proxyEndpoint']

    # Login to ECR
    subprocess.run(f"$(aws ecr get-login --no-include-email --region us-east-1)", shell=True, check=True)

    # Build the Docker image
    subprocess.run(f"docker build -t {image_name} .", shell=True, check=True)

    # Tag the image with the full registry path
    full_image_name = f"{registry_url}/{repository_name}:{image_name}"
    subprocess.run(f"docker tag {image_name} {full_image_name}", shell=True, check=True)

    # Push the image to ECR
    subprocess.run(f"docker push {full_image_name}", shell=True, check=True)

    return full_image_name

def deploy_to_ecs(full_image_name):
    """
    Update the ECS service to use the new image.
    """
    ecs_client.update_service(
        cluster=ecs_cluster_name,
        service=service_name,
        taskDefinition=full_image_name
    )

if __name__ == '__main__':
    full_image_name = build_and_push_image()
    deploy_to_ecs(full_image_name)
    print(f"Deployment of {full_image_name} to {ecs_cluster_name} in service {service_name} completed.")
