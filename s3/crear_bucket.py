import boto3
import logging


sessao = boto3.Session(profile_name="auto-curso")
cliente_s3 = sessao.client("s3")

nome_backet = "bucket-boto3-curso"

try:
    # Criando o bucket
    resposta_bucket = cliente_s3.create_bucket(
        Bucket=nome_backet,
        CreateBucketConfiguration={
            "LocationConstraint": "us-east-2"
        }
    )
    # imprimindo a resposta retornada
    print(resposta_bucket)
except Exception as err: # noqa F841
    logging.error("Este bucket já existe!")

# Enviando uma imagem para o bucket
cliente_s3.upload_file(
    "arquivos/Amazon_Lambda_architecture_logo.svg",
    nome_backet,
    "imagens/logo_aws.svg"
)

# Criando uma documento dentro do próprio bucket
planilha = """
    Nome\tNota
    Ana\t9
    Maria\t9
    Pedro\t7
    Carlos\t8
    Marta\t10
"""

cliente_s3.put_object(
    Body=planilha,
    Bucket=nome_backet,
    Key="planilha.xls"
)
