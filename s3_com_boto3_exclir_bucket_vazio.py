import boto3

sessao = boto3.Session(profile_name="auto-curso")
cliente_s3 = sessao.client("s3")

nome_bucket = "bucket-boto3-curso"

# Acessando o Bucket usando o método resource
resource_s3 = sessao.resource("s3")
bucket = resource_s3.Bucket(nome_bucket)

# Deletando o Bucket, ele deve está vazio para isso
# cliente_s3.delete_bucket(Bucket=nome_bucket)
bucket.delete()
