# 🔐 Validación de Políticas IAM con Access Analyzer

Este mini-lab muestra cómo validar una política IAM usando la API `ValidatePolicy` del servicio AWS Access Analyzer para detectar configuraciones inseguras.

---

## 🎯 Objetivo

- Detectar malas prácticas en políticas IAM antes de aplicarlas.
- Identificar riesgos como el uso de comodines (`*`) en `Action` o `Resource`.
- Automatizar auditoría de políticas con `boto3`.

---

## 📁 Archivos

| Archivo               | Descripción                                      |
|------------------------|--------------------------------------------------|
| `policy-insegura.json` | Política de prueba con permisos amplios inseguros |
| `validate_policy.py`  | Script en Python para validar la política         |
| `resultados.txt`      | Salida del análisis con findings detectados       |

---

## 🧪 Cómo probar

1. Asegúrate de tener Python y `boto3` instalados:
   ```bash
   pip install boto3
2. Asegúrate de tener Python y `boto3` instalados:
    ```bash
    aws configure
3. Ejecuta el script:
    ```bash
   python validate_policy.py
## 📌 Extras
Este análisis también puede realizarse desde la CLI:
```bash 
 aws accessanalyzer validate-policy \
  --policy-document file://policy-insegura.json \
  --policy-type IDENTITY_POLICY
```
📌 Se modifico un poco el archivo para que lea todos las policis de donde se ejecute el file y queda esto:

![image](https://github.com/user-attachments/assets/735c1fcf-5b2e-46ca-939d-563df7e8aa49)



## 🔐 Access Analyzer – APIs y Herramientas Usadas
Este módulo contiene prácticas enfocadas en validar políticas IAM, Resource Policies y SCPs usando herramientas oficiales de AWS.
| Comando/API                    | Tipo        | Función Principal                                                                    |
| ------------------------------ | ----------- | ------------------------------------------------------------------------------------ |
| `validate-policy`              | CLI/API     | Valida políticas IAM, Resource Policies y SCP, detectando errores o malas prácticas. |
| `create-analyzer`              | CLI/API     | Crea un "Analyzer" que revisa continuamente configuraciones de acceso externo.       |
| `create-access-preview`        | CLI/API     | Simula el impacto de aplicar una política a un recurso antes de hacerlo realmente.   |
| `get-access-preview`           | CLI/API     | Consulta el estado de una simulación de política (`Access Preview`).                 |
| `list-access-preview-findings` | CLI/API     | Muestra hallazgos detallados de la simulación (`quién tendría acceso y por qué`).    |
| `cfn-policy-validator`         | Herramienta | Valida políticas definidas dentro de plantillas CloudFormation (`.json` o `.yaml`).  |

# 🧪 Scripts utilizados
`validate_policy.py` : valida 1 política IAM desde Python

`validate_all_policies.py`: valida múltiples .json en una carpeta

`validate-identity-policy.sh, validate-resource-policy.sh, validate-scp.sh`: validaciones por tipo

`validate-all-policies.sh`: script unificado que detecta y analiza todos los .json automáticamente
