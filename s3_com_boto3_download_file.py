import boto3

sessao = boto3.Session(profile_name="auto-curso")

cliente_s3 = sessao.client("s3")

nome_bucket = "bucket-boto3-curso"

cliente_s3.download_file(
    Bucket=nome_bucket,
    Key="imagens/logo_aws.svg",
    Filename="arquivos/download_img_aws_logo.svg"
)

# Segunda forma de fazer Download do s3 da AWS
nome_arquivo = "arquivos/download_img_aws_log.svg"
with open(nome_arquivo, "wb") as data:
    cliente_s3.download_fileobj(
        Bucket=nome_bucket,
        Key="imagens/logo_aws.svg",
        Fileobj=data
    )


# Terceira forma de obter um arquivo do s3
planilha_s3 = cliente_s3.get_object(
    Bucket=nome_bucket,
    Key="planilha.xls"
)
planilha_body = planilha_s3["Body"]
planilha = planilha_body.read()
print(type(planilha))
print(planilha)
print(planilha.decode("utf8"))
