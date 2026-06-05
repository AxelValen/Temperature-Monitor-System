import os
from dotenv import load_dotenv
from email.message import EmailMessage #es la que crea objetos
from read_data import SerialReader
import ssl 
import smtplib

rs = SerialReader

email = input("Escribe tu correo:\n> ")

def send_email():
    #configuracion y datos
    sender_email = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver_email = f"{email}"
    
    #formato
    subject = "ALERTA DE TEMPERATURA!!"
    body = f"La temperatura ha superado el umbral: Temperatura en: {rs.temp} C"

    #objeto
    em = EmailMessage()

    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)
    
    #coneccion con el server
    context = ssl.create_default_context()
    
    #Envio del correo
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)
    smtp.login(sender_email,password)
    err = smtp.sendmail(sender_email,receiver_email,em.as_string())

    print(err)