#include "DHT.h" //Libreria para manejar el sensor

#define DHTPIN 4 //pin por el que se leerán los datos del sensor
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); //Estableciendo la comunicación con el puerto serial
  dht.begin(); //Iniciando el sensor
}

void loop() {

  delay(5000);

  //Leyendo la humedad
  float h = dht.readHumidity();
  //Leyendo la temperatura
  float t = dht.readTemperature();

  //Revisando que no hayan lecturas erroneas
  if (isnan(h) || isnan(t)) {
    Serial.println(F("NULL"));
    return;
  }

  //Imprimiendo las lecturas:
  Serial.print(t);
  Serial.print(",");
  Serial.println(h);  
}
