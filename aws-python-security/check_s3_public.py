import boto3

# Crear la sesión con el perfil configurado
session = boto3.Session(profile_name='default', region_name='us-east-2')
s3 = session.client('s3')

def is_bucket_public(bucket_name):
    try:
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl['Grants']:
            grantee = grant['Grantee']
            if 'URI' in grantee and 'AllUsers' in grantee['URI']:
                return True
    except Exception as e:
        print(f"Error revisando {bucket_name}: {e}")
    return False

def check_buckets():
    response = s3.list_buckets()
    print("📦 Buckets detectados:")
    for bucket in response['Buckets']:
        name = bucket['Name']
        print(f"🔍 Revisando: {name}")
        if is_bucket_public(name):
            print(f"⚠️  {name} ES PÚBLICO ❗")
        else:
            print(f"✅ {name} es privado.")

if __name__ == "__main__":
    check_buckets()