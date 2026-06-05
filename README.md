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

## ⚙️ Instalación y Configuración

1.  **Instalar dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` en la raíz del proyecto y agrega tus credenciales:
    ```env
    TWILIO_ACCOUNT_SID=tu_sid
    TWILIO_AUTH_TOKEN=tu_token
    TWILIO_PHONE_NUMBER=whatsapp:+14155238886
    EMAIL_SENDER=tu_correo@gmail.com
    EMAIL_PASSWORD=tu_contraseña_de_aplicacion
    ```

3.  **Cargar el Firmware:**
    Sube el archivo `Sensor_Arduino.ino` a tu placa utilizando el Arduino IDE.

## 💻 Uso del Sistema

* Ejecuta el script principal (main.py). El sistema te pedirá ingresar tus números de contacto, correos y los umbrales de temperatura

* Para detener el monitoreo y visualizar la gráfica de temperatura acumulada, presiona `Ctrl + C` en la terminal.
