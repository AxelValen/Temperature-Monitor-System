from read_data import SerialReader
import sensor_plot as plt
import email_sender as es
import dm_sender as dm
from datetime import datetime

rs = SerialReader
rs.setup_serial_port(9600)

#obteniendo los limites de temperatura del usuario
def get_user_limits():
    while True:
        try:
            max_temp = float(input("Ingrese el límite superior de temperatura: "))
            min_temp = float(input("Ingrese el límite inferior de temperatura: "))
            if min_temp < max_temp:
                return max_temp, min_temp
            else:
                print("El límite inferior debe ser menor que el superior. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
        
def main():
    
    max_temp, min_temp = get_user_limits() 
    last_alert_state = "normal"  #define el estado inical de alerta
    
    try:
        while True:
            rs.read_serial_input()
            
            #Muestra en la consola la informacion recogida por el sensor.
            if rs.temp != None:
                tiempo = datetime.now().strftime('%d/%m %H:%M:%S')
                print(f"{tiempo}: {rs.temp}°C")
                
            # Verificar límites y enviar alertas
            current_state = "normal"
            if rs.temp < min_temp:
                current_state = "low"
            elif rs.temp > max_temp:
                current_state = "high"
                
            if current_state != last_alert_state:
                if current_state == "low":
                    dm.send_whatsapp_alert(f"¡Alerta! La temperatura ha bajado a {rs.temp}°C, por debajo del límite de {min_temp}°C")
                    es.send_email()
                elif current_state == "high":
                    dm.send_whatsapp_alert(f"¡Alerta! La temperatura ha subido a {rs.temp}°C, por encima del límite de {max_temp}°C")
                    es.send_email()
                elif current_state == "normal" and last_alert_state != "normal":
                    dm.send_whatsapp_alert(f"La temperatura ha vuelto al rango normal: {rs.temp}°C")
                    es.send_email()
                    
                last_alert_state = current_state
    except KeyboardInterrupt:
        plt.graph()
        
main()

    