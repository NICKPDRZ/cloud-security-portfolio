-------------
### 🖥️ list_ec2_instances.py

Este script lista todas las instancias EC2 activas en la cuenta actual de AWS, incluyendo información como:

- Nombre (tag `Name`)
- ID de instancia
- Tipo de instancia
- Estado actual
- Zona de disponibilidad

📌 Ideal para tareas de monitoreo y auditoría básica.

#### ▶️ Ejecución

```bash
python list_ec2_instances.py
```

------------



### 🔐 check_s3_public.py

Este script revisa si algún bucket S3 tiene configuraciones públicas (acceso sin autenticar).

✅ Lista todos los buckets  
✅ Analiza sus ACLs  
✅ Informa si hay exposición a internet

```bash
python check_s3_public.py
```
## ✅ Prueba ofensiva: detección de bucket S3 público

Como parte del aprendizaje práctico, se creó un bucket en AWS con ACL pública (`AllUsers: READ`) para verificar si el script `check_s3_public.py` podía detectarlo.

📌 Resultado: el script identificó correctamente el bucket como **público**, lo que demuestra que la lógica implementada funciona para auditorías de seguridad real en S3.

Este tipo de detecciones son clave como parte del rol de Cloud Security Engineer.


![image](https://github.com/user-attachments/assets/2ea6dc22-d1fa-47ed-bfa7-667770b8246e)

---

🧹 El bucket fue eliminado después de la prueba.


----

### 🔐 check_iam_mfa.py

Este script revisa todos los usuarios IAM en la cuenta actual y detecta si tienen habilitada la autenticación multifactor (MFA).

✅ Lista usuarios  
✅ Detecta ausencia de MFA  
✅ Muestra alerta si falta configurar seguridad

```bash
python check_iam_mfa.py
```

---

### 🛡️ check_aws_security.py

Este script realiza una auditoría básica de seguridad en tu cuenta de AWS, automatizando las siguientes verificaciones:

- 🖥️ **EC2**: Lista todas las instancias activas
- 📦 **S3**: Detecta buckets con permisos públicos
- 👤 **IAM**: Identifica usuarios que no tienen MFA habilitado

#### ▶️ Ejecución
![image](https://github.com/user-attachments/assets/d4229fd0-1cac-4747-a6e9-969d51189b1d)

```bash
python check_aws_security.py



