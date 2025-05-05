import boto3
import json

# Cliente para Access Analyzer
client = boto3.client('accessanalyzer')

# Cargar el contenido de la política desde el archivo
with open('bad_policy.json') as f:
    policy = json.load(f)

# Validar la política
response = client.validate_policy(
    policyDocument=json.dumps(policy),
    policyType='IDENTITY_POLICY'
)

# Mostrar los resultados
print("Findings:")
for finding in response['findings']:
    print(f"- {finding['findingType']}: {finding['findingDetails']}")
print("Policy is valid.")
# Si la política no es válida, se lanzará una excepción y no se mostrará el mensaje de "Policy is valid."   