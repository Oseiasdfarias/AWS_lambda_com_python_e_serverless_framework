import boto3

sessao = boto3.Session(profile_name="auto-curso")
cliente_ec2 = sessao.client("ec2")
resposta_instancia = (cliente_ec2.describe_instances(
    Filters=[
        {
            "Name": "instance-state-name",
            "Values": [
                "running",
                "stopped"
            ]
        },
    ],)
)

# print(resposta_instancia)
id_instancias = (resposta_instancia
                 ['Reservations']
                 [0]['Instances']
                 [0]['InstanceId'])

print(id_instancias)

# Parando/Desligando a instância
# cliente_ec2.stop_instances(InstanceIds=[id_instancias])

# Linga/Inicia a instância
cliente_ec2.start_instances(InstanceIds=[id_instancias])
