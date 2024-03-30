import boto3

# Criando um cliente boto3
sessao = boto3.Session(profile_name="auto-curso")
client_s3 = sessao.client("s3")
lista = client_s3.list_buckets()
print(lista)
