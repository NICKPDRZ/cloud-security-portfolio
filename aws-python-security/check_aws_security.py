import boto3

# 🔐 Conexión a AWS
session = boto3.Session(profile_name='default', region_name='us-east-2')
ec2 = session.client('ec2')
s3 = session.client('s3')
iam = session.client('iam')

# 🖥️ Revisar instancias EC2
def check_ec2_instances():
    print("\n🖥️ EC2 Instances:")
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']
            az = instance['Placement']['AvailabilityZone']
            print(f"🔹 {instance_id} - {instance_type} - {state} - {az}")

# 📦 Revisar buckets públicos
def check_s3_public_buckets():
    print("\n📦 S3 Buckets:")
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        name = bucket['Name']
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            public = False
            for grant in acl['Grants']:
                grantee = grant['Grantee']
                if 'URI' in grantee and 'AllUsers' in grantee['URI']:
                    public = True
            if public:
                print(f"⚠️  {name} ES PÚBLICO ❗")
            else:
                print(f"✅ {name} es privado.")
        except Exception as e:
            print(f"❌ No se pudo revisar {name}: {e}")

# 👤 Revisar usuarios IAM sin MFA
def check_iam_mfa():
    print("\n👤 IAM Users sin MFA:")
    response = iam.list_users()
    for user in response['Users']:
        username = user['UserName']
        mfa = iam.list_mfa_devices(UserName=username)
        if not mfa['MFADevices']:
            print(f"⚠️  {username} NO tiene MFA ❌")
        else:
            print(f"✅ {username} tiene MFA")

# ▶️ Ejecutar todo
if __name__ == "__main__":
    print("🔎 Iniciando auditoría de seguridad en AWS...\n")
    check_ec2_instances()
    check_s3_public_buckets()
    check_iam_mfa()
