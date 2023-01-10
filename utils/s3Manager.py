import boto3
from django.core.files.base import ContentFile
from utils.keyManager import get_secret

# Connect to S3
s3 = boto3.client('s3',
    aws_access_key_id=get_secret("S3_ACCESS_KEY"),
    aws_secret_access_key=get_secret("S3_SECRET_KEY"),
)

# # Open the file you want to upload
# with open('path/to/file', 'rb') as data:
#     # Upload the file to S3
def upload_files_to_S3(data, file_name):
    uri = []
    for d in data:
        uri.append(s3.upload_fileobj(d, 'purry0', file_name))
    return uri
