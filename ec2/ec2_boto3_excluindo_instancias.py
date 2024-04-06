import boto3

sessao = boto3.Session(profile_name="auto-curso")
cliente_ec2 = sessao.client("ec2")

id_instancia = "i-036ab88007ee31baf"

cliente_ec2.terminate_instances(
    InstanceIds=[id_instancia]
)
