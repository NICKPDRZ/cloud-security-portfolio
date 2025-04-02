# 🚀 VPC segura en AWS con Terraform

Este proyecto crea una red segura en AWS utilizando Terraform como herramienta de infraestructura como código (IaC). Forma parte de mi portafolio de formación como Cloud Security Engineer.

## 🎯 Objetivos

- Crear una VPC personalizada
- Agregar una subnet pública
- Asociar una tabla de rutas con Internet Gateway
- Crear un Security Group con acceso solo por SSH
- Lanzar una instancia EC2 t2.micro en la subnet pública

## 📁 Estructura

```
terraform-vpc/
├── main.tf         # Recursos principales (VPC, Subnet, SG, EC2)
├── outputs.tf      # Salidas del proyecto
├── variables.tf    # Variables del entorno
├── terraform.tfstate*   # Estado (no versionado)
├── .terraform/*         # Proveedores descargados (ignorado)
```
## 🧠 Lo que aprendí
-Principios de Terraform y uso de archivos .tf
-Creación de redes seguras en AWS de forma automática
-Buenas prácticas como el uso de .gitignore para evitar subir archivos sensibles o pesados


##📸 Capturas
![image](https://github.com/user-attachments/assets/d79a789e-4f3f-465f-a43e-af07b359e438)


## 🔐 Seguridad
Este ejercicio permite SSH desde cualquier IP (0.0.0.0/0) solo con fines de prueba. En producción debe limitarse por IP y clave privada protegida.


## 📌 Autor
Nicolás Pedroza
GitHub
Cloud Security Engineer (en formación)

