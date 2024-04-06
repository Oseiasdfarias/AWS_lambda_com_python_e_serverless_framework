import boto3

sessao = boto3.Session(profile_name="auto-curso")

cliente_ec2 = sessao.client("ec2", region_name='us-east-1')

nome_chave = "curso-aws"
vpc_id = "vpc-0fac89075424bc711"
subnet_id = "subnet-0de1af98fb6684bd8"
ami_id = "ami-080e1f13689e07408"

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

# Criando UMA instancia EC2 na AWS
arquivo_user_data = open("./wp_user_data.sh", "r")
user_data = arquivo_user_data.read()

resposta_ec2 = cliente_ec2.run_instances(
    BlockDeviceMappings=[
        {
            "DeviceName": "/dev/sda1",
            "Ebs": {
                "VolumeSize": 8,
                "DeleteOnTermination": True,
                "VolumeType": "gp2",
                "Encrypted": False
            }
        }
    ],
    UserData=user_data,
    ImageId=ami_id,
    MaxCount=1,
    MinCount=1,
    InstanceType="t2.micro",
    KeyName=nome_chave,
    Monitoring={
        "Enabled": False
    },
    SecurityGroupIds=[sg_id],
    SubnetId=subnet_id,
    InstanceInitiatedShutdownBehavior="terminate",
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "wp-curso-python"
                },
                {
                    "Key": "Ambiente",
                    "Value": "desenvolvimento"
                },
            ]
        },
    ]
)
print(resposta_ec2)
