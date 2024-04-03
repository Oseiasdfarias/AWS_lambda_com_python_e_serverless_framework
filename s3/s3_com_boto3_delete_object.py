import boto3

# Inicializando uma sessão
sessao = boto3.Session(profile_name="auto-curso")

# instanciando um cliente s3
cliente_s3 = sessao.client("s3")

# variáveis com o nome do bucket que desejo acessar
bucket_name = "bucket-boto3-curso"

# response = cliente_s3.delete_object(
#     Bucket=bucket_name,
#     Key="imagens/logo_aws.svg"
# )
# print(response)


# Deletando arquivo com outro método
resource_s3 = sessao.resource("s3")
bucket = resource_s3.Bucket(bucket_name)
# response = bucket.delete_objects(
#     Delete={
#         "Objects": [
#             {
#                 "Key": "planilha.xls"
#             },
#             {
#                 "Key": "imagens/logo_aws.svg"
#             }
#         ]
#     }
# )
# print(response)

# Outra forma de excluir todos os objetos de um Backet
objetos = bucket.objects.all()  # Listando os objetos do bucket
# for obj in objetos:
#     print(obj)
resultado = objetos.delete()
print(resultado)
