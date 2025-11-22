import boto3

try:
    bucket_name = "c0943861-ab-nyc-dataset-2025"
    local_file_path = "data/AB_NYC_2019.csv"
    s3_path = "data/AB_NYC_2019.csv"

    s3_client = boto3.client("s3")
    s3_client.upload_file(local_file_path, bucket_name, s3_path)
except:
    print("An error occurred while uploading the file to S3.")
