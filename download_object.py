import os
import boto3

# 사전에 .aws/credentials 에서 정의
os.environ['AWS_PROFILE'] = "Profile1"

bucket_region = 'ap-northeast-2'
bucket_name = 'prev_bucket'
object_download_folder = 'object_folder'

s3 = boto3.client('s3', region_name = bucket_region)

response = s3.list_objects(Bucket = bucket_name)
for i in response['Contents']:
    s3.download_file(bucket_name, i['Key'], f'{object_download_folder}/{i["Key"]}')