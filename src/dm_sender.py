import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

#Las credenciales
sender = os.getenv('TWILIO_PHONE_NUMBER')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

whatsapp = input("Escribe tu numero de Whatsapp\n> ")

def send_whatsapp_alert(cuerpo):
    try:
        message = client.messages.create(
            from_=f'whatsapp:{sender}',  #Número de Twilio
            body=cuerpo,
            to=f'whatsapp:+1{whatsapp}'
        )
        print(f"Alerta enviada: {message.sid}")
    except Exception as e:
        print(f"error al enviar la alerta: {e}")
