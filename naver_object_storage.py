# !pip install boto3
# 먼저 api key를 생성하여야 합니다.
# ncloud.com 로그인 후 마이페이지 -> 계정관리 -> 인증키관리
# 인증키 생성 후 아래 access_key, secret_key 입력.
# !pip install boto3
# 오브젝트 스토리지 접속하여서 버킷(클라우드 파일 저장 장치)를 만듭니다.
# https://console.ncloud.com/objectStorage/objectStorageList
import boto3

service_name = 's3'
endpoint_url = 'https://kr.object.ncloudstorage.com'
region_name = 'kr-standard'
access_key = 'ncp_iam_BPASKR1ecadlAFG0xKRw'
secret_key = 'ncp_iam_BPKSKRBIYDibktbY9cEBAaMuElBHhZGzDM'

def bucket_list():
    s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)

    response = s3.list_buckets()

    for bucket in response.get('Buckets', []):
        print (bucket.get('Name'))


def upload_file():
    s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)

    bucket_name = 'opencv'

    # create folder
    object_name = 'opencv/'

    s3.put_object(Bucket=bucket_name, Key=object_name)

    # upload file
    object_name = 'video_2.mp4'
    local_file_path = "C:\\Users\\sys\\Desktop\\openCV\\video_2.mp4"

    s3.upload_file(local_file_path, bucket_name, object_name)

if __name__ == "__main__":
    bucket_list()
    upload_file()