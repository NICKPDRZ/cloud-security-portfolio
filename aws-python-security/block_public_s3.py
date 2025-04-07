import boto3
from botocore.exceptions import ClientError

# 🔐 Crear sesión con AWS (usa el perfil y la región que corresponda)
session = boto3.Session(profile_name='default', region_name='us-east-2')
s3 = session.client('s3')

def get_bucket_public_status(bucket_name):
    """
    Revisa el ACL del bucket para determinar si está público.
    Devuelve True si detecta que el bucket es público, False en caso contrario.
    """
    try:
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl.get('Grants', []):
            grantee = grant.get('Grantee', {})
            # Si hay algún grant para 'AllUsers' o 'AuthenticatedUsers'
            if 'URI' in grantee and ('AllUsers' in grantee['URI'] or 'AuthenticatedUsers' in grantee['URI']):
                return True
    except ClientError as e:
        print(f"❌ Error al obtener ACL para {bucket_name}: {e}")
    return False

def block_bucket_public_access(bucket_name):
    """
    Configura el bloque de acceso público para el bucket.
    Esto evita que el bucket pueda ser configurado para acceso público.
    """
    try:
        response = s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        print(f"✅ Bloqueo de acceso público aplicado para: {bucket_name}")
    except ClientError as e:
        print(f"❌ Error al bloquear acceso público para {bucket_name}: {e}")

def main():
    print("🔎 Iniciando revisión y bloqueo de buckets S3 públicos...\n")
    try:
        response = s3.list_buckets()
        for bucket in response.get('Buckets', []):
            bucket_name = bucket['Name']
            print(f"🔍 Revisando bucket: {bucket_name}")
            # Verificar si el bucket es público por ACL
            if get_bucket_public_status(bucket_name):
                print(f"⚠️  {bucket_name} se detectó como público.")
                block_bucket_public_access(bucket_name)
            else:
                print(f"✅ {bucket_name} ya es privado.")
            print("-" * 40)
    except ClientError as e:
        print(f"❌ Error al listar buckets: {e}")

if __name__ == "__main__":
    main()
