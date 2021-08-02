#/bin/python3
import Adafruit_DHT.DHT22
import time
from datetime import datetime 
import requests
import os

URL=os.environ['API_URL']
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
Temperatures=[]
Humidities=[]
while True:
    Temperatures.clear()
    Humidities.clear()
    for i in range(6):
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            Temperatures.append(temperature)
            Humidities.append(humidity)
        time.sleep(10)        
    if len(Temperatures) != 6:
        print("{0}error - one or more measurements fail ".format(datetime.now()))
    else:
        mediaTemperature = sum(Temperatures) / 6
        mediaHumidity = sum(Humidities) / 6
        payload = {
            'temperature': mediaTemperature, 
            'humidity': mediaHumidity
            }
        print(payload)
        response = requests.post(URL + "/measurement", json= payload)
        if response.status_code != 201:
            print("http error ", response.status_code, response)
