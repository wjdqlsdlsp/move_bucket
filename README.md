# move_bucket
aws s3 오브젝트 다른계정으로 욺기기 위한 코드들

다른 계정으로 aws S3 오브젝트들 욺기기 위한 코드들 정리입니다.

AWS Docs를 보면 다른 방법이 있지만, 오브젝트 갯수 및 파일 크기가 작을 때 사용하기를 추천드립니다.

Boto3를 이용해서 모든 오브젝트들을 다운받고, 다른 오브젝트로 전송합니다.

#### 준비물

- AWS 2개의 버킷 ( 이전하고자 하는 버킷, 새로운 버킷 ) 
- Python Boto3
