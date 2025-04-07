import boto3

# 🔐 1. Creamos una sesión con AWS
session = boto3.Session(profile_name='default', region_name='us-east-2')
iam = session.client('iam')

# 📋 2. Obtenemos todos los usuarios IAM
response = iam.list_users()

# 📌 3. Recorremos cada usuario
for user in response['Users']:
    username = user['UserName']
    
    # 🔍 4. Buscamos si tiene dispositivos MFA
    mfa_devices = iam.list_mfa_devices(UserName=username)

    if not mfa_devices['MFADevices']:
        print(f"⚠️  {username} NO tiene MFA habilitado ❌")
    else:
        print(f"✅ {username} tiene MFA habilitado")
