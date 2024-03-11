from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Initialize Azure Storage Blob client
connection_string = "YourAzureStorageConnectionString"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def create_container(container_name):
    """Create a container in Azure Blob Storage"""
    try:
        container_client = blob_service_client.create_container(container_name)
        print(f"Container '{container_name}' created successfully.")
    except Exception as e:
        print(e)

def upload_blob(container_name, blob_name, file_path):
    """Upload a file to a container in Azure Blob Storage"""
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"Blob '{blob_name}' uploaded to container '{container_name}'.")
    except Exception as e:
        print(e)

def list_blobs(container_name):
    """List all blobs in a container"""
    try:
        container_client = blob_service_client.get_container_client(container_name)
        blobs = container_client.list_blobs()
        for blob in blobs:
            print(blob.name)
    except Exception as e:
        print(e)

def delete_blob(container_name, blob_name):
    """Delete a blob from a container"""
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.delete_blob()
        print(f"Blob '{blob_name}' deleted from container '{container_name}'.")
    except Exception as e:
        print(e)

def delete_container(container_name):
    """Delete a container"""
    try:
        container_client = blob_service_client.get_container_client(container_name)
        container_client.delete_container()
        print(f"Container '{container_name}' deleted.")
    except Exception as e:
        print(e)

# Example usage
if __name__ == "__main__":
    container_name = 'your-container-name'
    blob_name = 'your-blob-name'
    file_path = '/path/to/your/file'

    # Create a container
    create_container(container_name)
    
    # Upload a blob
    upload_blob(container_name, blob_name, file_path)
    
    # List blobs in a container
    list_blobs(container_name)
    
    # Delete a blob
    delete_blob(container_name, blob_name)
    
    # Delete a container
    delete_container(container_name)
