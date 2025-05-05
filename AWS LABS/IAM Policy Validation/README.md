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



