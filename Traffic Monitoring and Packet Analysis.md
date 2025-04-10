## 🛰️ AWS Traffic Mirroring y Análisis de Paquetes

Este proyecto documenta el laboratorio "AWS Security Traffic Monitoring and Packet Analysis" realizado en AWS Skill Builder. El objetivo fue aprender a capturar, redirigir y analizar el tráfico de red en instancias EC2 usando Traffic Mirroring.

# 🎯 Objetivos del laboratorio

Identificar la interfaz de red (ENI) a monitorear

Configurar un Traffic Mirror Target

Definir un Traffic Mirror Filter con reglas de captura

Crear una Traffic Mirror Session

Verificar que el tráfico se esté enviando correctamente al target

Modificar filtros para analizar tráfico específico

Capturar los paquetes en un archivo para análisis

# 📌 Infraestructura utilizada

2 instancias EC2:

Fuente: genera tráfico de red

Target: recibe el tráfico espejado (con tcpdump o similar)

1 VPC con subredes y grupos de seguridad configurados

# 🛠️ Pasos realizados

1. Identificación de ENI

Se ubicó la instancia fuente y se identificó su interfaz de red primaria (ENI)

2. Creación del Mirror Target

Se seleccionó la instancia destino como receptor del tráfico espejado

3. Configuración del Mirror Filter

Se creó un filtro para capturar todo el tráfico (0.0.0.0/0, todos los puertos)

4. Creación de la sesión de mirroring

Se vinculó la ENI, el filtro y el target

5. Validación

Se generó tráfico desde la instancia fuente (ej: curl, ping)

Se ejecutó tcpdump en la instancia destino para verificar la captura

6. Exportación

Se redireccionó la salida de tcpdump a un archivo .pcap

## 🧠 Aplicaciones reales en seguridad

# 🔍 Análisis forense / investigación

Monitorear el tráfico sin intervenir la instancia afectada

Detectar exfiltración de datos, beaconing o comunicaciones sospechosas

# 🛡️ Detección activa de amenazas

Implementar sensores con herramientas como Zeek o Suricata

Integrar alertas con Amazon EventBridge o AWS Lambda para respuesta automática

# 🧰 SOC en la nube

Este enfoque permite replicar funcionalidades típicas de un NIDS (Network Intrusion Detection System) en entornos cloud, facilitando el cumplimiento de normativas como PCI-DSS o ISO 27001.

## 📁 Archivos importantes

Captura de comandos tcpdump

Capturas de pantalla del entorno y validaciones

Diagrama de arquitectura (pendiente)

## 💡 Lecciones aprendidas

Tráfico entre instancias se puede capturar sin instalar agentes

Las ENIs son elementos críticos en la red de AWS

Traffic Mirroring es ideal para detección de amenazas, forense, IDS/IPS

Puedo automatizar esta configuración más adelante con Terraform

