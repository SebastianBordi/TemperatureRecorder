FROM python:3.7-alpine 
RUN pip3 install Adafruit_DHT 
WORKDIR /app
COPY TemperatureRecorder.py /app/TemperatureRecorder.py
ENV API_URL=https://tra.emconsol.com
CMD ["python3", "TemperatureRecorder.py"]
