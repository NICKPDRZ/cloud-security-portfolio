import boto3

# Crea una sesión con perfil y región especificados (más seguro)
session = boto3.Session(profile_name="default", region_name="us-east-2")
ec2 = session.client('ec2')

# Obtener las instancias
response = ec2.describe_instances()

# Recorrer las instancias
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"ID: {instance['InstanceId']}")
        print(f"Estado: {instance['State']['Name']}")
        print(f"Tipo: {instance['InstanceType']}")
        print(f"Zona: {instance['Placement']['AvailabilityZone']}")
        print("-" * 30)
# Agrega script EC2 audit con Python y Boto3
