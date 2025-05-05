import boto3
import json
import os

# Cliente de Access Analyzer
client = boto3.client('accessanalyzer')

# Listar todos los archivos JSON en la carpeta actual
policy_files = [f for f in os.listdir() if f.endswith('.json')]

if not policy_files:
    print("❌ No se encontraron archivos .json en esta carpeta.")
    exit()

for file_name in policy_files:
    print(f"\n🔍 Analizando: {file_name}")

    try:
        with open(file_name, 'r') as f:
            policy = json.load(f)

        response = client.validate_policy(
    policyType='IDENTITY_POLICY',
    policyDocument=json.dumps(policy)
)


        findings = response.get('findings', [])

        if not findings:
            print("✅ La política es válida.")
        else:
            for finding in findings:
                tipo = finding.get('findingType')
                detalle = finding.get('findingDetails')
                codigo = finding.get('issueCode')
                print(f"⚠️ [{tipo}] {codigo}: {detalle}")

    except Exception as e:
        print(f"❌ Error analizando {file_name}: {e}")
