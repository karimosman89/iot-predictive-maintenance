# cloud/s3_upload.py
import boto3

s3 = boto3.client('s3')

def upload_to_s3(file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_path
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"Uploaded {file_path} to {bucket_name}/{object_name}")

# Example upload
upload_to_s3('data/processed/sensor_data.csv', 'your-bucket-name', 'processed_data/sensor_data.csv')

