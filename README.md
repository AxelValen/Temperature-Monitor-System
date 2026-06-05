# Sistema de Monitoreo de Temperatura IoT con Alertas Multicanal

Este proyecto implementa un sistema de monitoreo de variables ambientales (temperatura y humedad) utilizando un microcontrolador y un script de Python. El sistema evalúa los datos en tiempo real y, en caso de superar los umbrales definidos por el usuario, dispara alertas automáticas a través de WhatsApp (vía Twilio) y correo electrónico.

## 🚀 Características Principales

* **Monitoreo en Tiempo Real:** Adquisición de datos desde un sensor DHT11 mediante comunicación serial.
* **Alertas Inteligentes:** Notificaciones por WhatsApp y Email basadas en umbrales máximos y mínimos configurables.
* **Tolerancia a Fallos:** Manejo de desconexiones seriales con reconexión automática.
* **Registro de Eventos:** Sistema de logging integrado para auditar lecturas y estados de alerta.
* **Visualización de Datos:** Generación de gráficas de comportamiento térmico usando `matplotlib`.

## 🛠️ Tecnologías y Hardware Utilizado

* **Hardware:** Microcontrolador (ej. Arduino Uno / ESP32), Sensor DHT11 de temperatura y humedad.
* **Lenguajes:** C++ (Firmware), Python 3.12 (Software de control).
* **Librerías de Python:** `pyserial`, `twilio`, `matplotlib`, `python-dotenv`.
* **APIs:** Twilio API (para Sandbox de WhatsApp), Servidor SMTP de Gmail.