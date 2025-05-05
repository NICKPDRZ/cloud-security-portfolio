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
    aws configure
3. Ejecuta el script:
    python validate_policy.py

## 📌 Extras
Este análisis también puede realizarse desde la CLI:
 
 aws accessanalyzer validate-policy \
  --policy-document file://policy-insegura.json \
  --policy-type IDENTITY_POLICY



