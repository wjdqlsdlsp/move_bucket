import os
import boto3

# 사전에 .aws/credentials 에서 정의
os.environ['AWS_PROFILE'] = "Profile2"

bucket_region = 'ap-northeast-2'
bucket_name = 'new_bucket'
object_download_folder = 'object_folder'

s3 = boto3.client('s3', region_name = bucket_region)

file_list = os.listdir(object_download_folder)
for i in file_list:
    s3.upload_file(Bucket=bucket_name,
                    Filename=f'{object_download_folder}/{i}',
                    Key=i,
                    ExtraArgs={'ACL':'public-read'}) # 조건에 맞게 ACL조건 맞추기