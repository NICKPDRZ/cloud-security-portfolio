# 📊 Seguridad y Monitoreo con CloudWatch en AWS

Este laboratorio implementa un sistema de monitoreo de seguridad utilizando Amazon CloudWatch. A través de una instancia EC2 y un NAT Gateway, se configuran logs, alarmas y notificaciones para detectar intentos de acceso fallidos y analizar tráfico saliente.

---

## 🎯 Objetivos del proyecto

- Configurar una instancia Amazon Linux 2 para enviar logs a CloudWatch Logs.
- Crear una alarma en CloudWatch para detectar múltiples intentos fallidos de login.
- Configurar una alarma para monitorear el tráfico saliente a través de un NAT Gateway.
- Enviar notificaciones usando Amazon SNS.

---

## 🛠️ Servicios utilizados

- Amazon EC2
- Amazon CloudWatch (Logs, Metrics y Alarms)
- AWS Systems Manager Session Manager
- Amazon SNS

---

## ⚙️ Proceso resumido

1. ✅ Conectarse a la instancia EC2 con Session Manager.
2. 📥 Instalar e iniciar el agente de CloudWatch Logs.
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```
3. 🧠 Configurar el archivo de logs para que se envíen a CloudWatch.
4. 🔔 Crear una alarma de login fallido (SSH).
5. 🌐 Configurar monitoreo de tráfico saliente desde un NAT Gateway.
6. 📩 Integrar una notificación con SNS (correo).

---

## 🧠 Lo que aprendí

- Cómo centralizar logs en AWS con CloudWatch.
- Crear alarmas automatizadas para detectar posibles ataques.
- Supervisar el tráfico saliente de forma granular.
- Usar SNS para notificar eventos de seguridad relevantes.

---

## 📸 Capturas (opcional)
![image](https://github.com/user-attachments/assets/8c08393d-3fca-4433-ae4a-845a30f62094)
![image](https://github.com/user-attachments/assets/8f2be639-ca60-4e90-9adf-3937741be115)

> Agregá screenshots del gráfico de CloudWatch o del log si lo tenés.

---
