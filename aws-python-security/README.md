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




### 🔐 check_s3_public.py

Este script revisa si algún bucket S3 tiene configuraciones públicas (acceso sin autenticar).

✅ Lista todos los buckets  
✅ Analiza sus ACLs  
✅ Informa si hay exposición a internet

```bash
python check_s3_public.py
