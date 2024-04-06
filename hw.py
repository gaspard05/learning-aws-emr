import boto3

print('Hello World!')
s3_client = boto3.client('s3')
for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket['Name'])