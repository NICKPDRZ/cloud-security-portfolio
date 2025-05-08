# 🛠️ AWS CDK S3 Demo

Este laboratorio demuestra cómo utilizar AWS CDK para definir infraestructura como código (IaC) en Python. En este caso, se crea un bucket de Amazon S3 con permisos abiertos de escritura, lo que representa una mala práctica de seguridad para propósitos educativos.

---

## 🎯 Objetivo

- Usar AWS CDK para definir una política IAM en un recurso.
- Simular una mala práctica (bucket S3 con permisos `s3:PutObject` para todos).
- Validar esta política con `cfn-policy-validator` y detectar el problema de seguridad.

---

## 📁 Estructura del proyecto

```bash
cdk-s3-demo/
├── cdk_s3_demo/
│   ├── __init__.py
│   └── cdk_s3_demo_stack.py  # Define el recurso S3 y su política
├── .venv/                    # Entorno virtual (ignorado por Git)
├── README.md
├── app.py                   # Punto de entrada del CDK
└── cdk.out/                 # Archivos generados por CDK (ignorar)
```
## ⚙️ Pasos para ejecutar

# Instalar dependencias
```bash
 pip install -r requirements.txt
 ```

# Inicializar entorno CDK
```bash
 cdk bootstrap
 ```

# Generar la plantilla CloudFormation
```bash
cdk synth > insecure-role-template.json
 ```

# Validar con cfn-policy-validator
```bash
cfn-policy-validator validate \
  --template-path insecure-role-template.json \
  --region us-east-1
 ```

Deberías ver un mensaje como:
```bash
{
  "BlockingFindings": [
    {
      "findingType": "SECURITY_WARNING",
      "code": "PASS_ROLE_WITH_STAR_IN_ACTION_AND_RESOURCE",
      ...
    }
  ]
}
```

## 🚫 Problema de seguridad detectado
La política permite realizar s3:PutObject con Principal: * y Resource: *, lo cual representa una configuración insegura

## ✅ Buenas prácticas
* Limitar los permisos a cuentas o servicios específicos.

* Evitar el uso de * en Principal, Action y Resource.

* Validar tus plantillas con herramientas como cfn-policy-validator.


##  📌 Requisitos
* AWS CLI configurado

* CDK v2 instalado (npm install -g aws-cdk)

* Python 3.8+

* Acceso a una cuenta AWS para el bootstrap (aunque no desplegamos nada)
