import boto3


sessao = boto3.Session(profile_name="auto-curso")

cliente_s3 = sessao.client("s3")
cliente_ec2 = sessao.client("ec2")

lista_bucket = cliente_s3.list_buckets()
# print(lista_bucket)

recurso_s3 = sessao.resource("s3")
bucket = recurso_s3.Bucket("oseiasteste")
print(bucket)
