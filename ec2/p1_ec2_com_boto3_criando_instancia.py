import boto3

sessao = boto3.Session(profile_name="auto-curso")

cliente_ec2 = sessao.client("ec2", region_name='us-east-1')

nome_chave = "curso-aws.pem"
vpc_id = "vpc-0fac89075424bc711"
subnet_id = "subnet-0de1af98fb6684bd8"
ami_id = "ami-0b8b44ec9a8f90422"

try:
    resposta_sg = (cliente_ec2.
                   create_security_group(
                       Description="Novo sg",
                       GroupName="secg_web",
                       VpcId=vpc_id
                    ))
    sg_id = resposta_sg["GroupId"]

    resposta_ingress=(cliente_ec2.authorize_security_group_ingress(  # noqa E225
        GroupId=sg_id,
        IpPermissions=[
            {
                "FromPort": 22,
                "ToPort": 22,
                "IpProtocol": "tcp",
                "IpRanges": [
                    {
                        "CidrIp": "0.0.0.0/0",
                        "Description": "Acess SSH"
                        }]
                },
            {
                "FromPort": 80,
                "ToPort": 80,
                "IpProtocol": "tcp",
                "IpRanges": [
                    {
                        "CidrIp": "0.0.0.0/0",
                        "Description": "Acess HTTP"
                        }]
                }
            ]
    ))

except Exception:
    print("secg_web já existe!")
    resposta_grupos = (cliente_ec2.describe_security_groups(
                       GroupNames=["secg_web"]))
    sg_id = resposta_grupos["SecurityGroups"][0]["GroupId"]


