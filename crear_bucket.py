import boto3
from botocore.exceptions import ClientError
import logging


sessao = boto3.Session(profile_name="auto-curso")
cliente_s3 = sessao.client("s3")

try:
    # Criando o bucket
    resposta_bucket = cliente_s3.create_bucket(
        Bucket="bucket-boto3-curso",
        CreateBucketConfiguration={
            "LocationConstraint": "us-east-2"
        }
    )

    # imprimindo a resposta retornada
    print(resposta_bucket)
except ClientError as e:
    logging.error(e)
