import boto3
from botocore.exceptions import ClientError

# Initialize a boto3 client
s3 = boto3.client('s3')

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region"""
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        print(e)
        return False
    return True

def list_buckets():
    """List all S3 buckets"""
    try:
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            print(f'{bucket["Name"]}')
    except ClientError as e:
        print(e)

def upload_file(bucket_name, file_name, object_name=None):
    """Upload a file to an S3 bucket"""
    if object_name is None:
        object_name = file_name
    try:
        response = s3.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        print(e)
        return False
    return True

def list_objects(bucket_name):
    """List objects within an S3 bucket"""
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        for obj in response.get('Contents', []):
            print(f'{obj["Key"]}')
    except ClientError as e:
        print(e)

def delete_object(bucket_name, object_name):
    """Delete an object from an S3 bucket"""
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        print(f'{object_name} deleted from {bucket_name}')
    except ClientError as e:
        print(e)

def delete_bucket(bucket_name):
    """Delete an S3 bucket"""
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f'Bucket {bucket_name} deleted')
    except ClientError as e:
        print(e)

# Example usage
if __name__ == "__main__":
    # Set your bucket name and region
    bucket_name = 'your-bucket-name'
    region = 'us-east-1'
    
    # Create a new bucket
    create_bucket(bucket_name, region)
    
    # List all buckets
    list_buckets()
    
    # Upload a file
    upload_file(bucket_name, 'path/to/your/file', 'file-in-s3.txt')
    
    # List all objects in a bucket
    list_objects(bucket_name)
    
    # Delete an object from a bucket
    delete_object(bucket_name, 'file-in-s3.txt')
    
    # Delete a bucket
    delete_bucket(bucket_name)
