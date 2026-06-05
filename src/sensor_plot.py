import matplotlib.pyplot as plt
from read_data import SerialReader
import matplotlib.dates as mdates
from datetime import datetime
rs = SerialReader

def graph():
    plt.figure(figsize=(10, 5))
    plt.plot(rs.time_list, rs.temp_list, label='Temperatura')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Temperatura (°C)')
    plt.title('Variación de la temperatura con respecto al tiempo')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()