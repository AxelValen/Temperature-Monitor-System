import serial
from datetime import datetime
from collections import deque

class SerialReader_class:
    temp = 0
    serial_port = 0
    
    time_list = deque(maxlen=100)
    temp_list = deque(maxlen=100)

    def setup_serial_port(self,baud_rate:int):
        PORT = input("Selecciona el puerto:\n> ")
        is_port_valid = False

        while(not is_port_valid):
            try:
                self.serial_port = serial.Serial(f'COM{PORT}',baud_rate) #intentar abrir el puerto elegido
            except:
                #Si no se puede, intentar otra vez
                is_port_valid = False 
                print(f"Error abriendo el puerto COM{PORT}, pruebe otro")
                PORT = input("> ")
            else:
                is_port_valid = True  #Si se pudo abrir el puerto setear el flag

    #Lee la entrada serial del arduino y guarda los nuevos datos en las variables
    #time_list, temp_list, humidity_list
    def read_serial_input(self):
        try:
            # Intentamos leer el puerto
            new_line = self.serial_port.readline().decode('utf-8')
            
            if(new_line != "NULL"):
                values = new_line.rstrip().split(',')
                self.temp = float(values[0])
            else:
                self.temp = -99

            time = datetime.now().strftime('%d/%m %H:%M:%S')
            self.time_list.append(time)
            self.temp_list.append(self.temp)

        except serial.SerialException:
            self.temp = -99
            print("ERROR: Conexión serial perdida")
            
            # Forzamos una reconexión intentando abrir el puerto de nuevo
            import time as time_module
            time_module.sleep(2) # Esperar 2 segundos antes de reintentar
            try:
                self.serial_port.close()
                self.serial_port.open()
                print("Conexión restablecida.")
            except:
                pass 

#Crear una unica instancia de la clase, para ser importanda por los demas modulos
SerialReader = SerialReader_class()