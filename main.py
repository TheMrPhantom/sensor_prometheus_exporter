import prometheus_client
import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 14)

sensors=dict()
sensors['jroom_temp']=prometheus_client.Gauge(
    'sensor_jroom_temp', 'Temp in jrom')
sensors['jroom_hum']=prometheus_client.Gauge(
    'sensor_jroom_hum', 'Humidity in jrom')

prometheus_client.start_http_server(8002)

while True:

    result = instance.read()

    if result.is_valid():
        sensors['jroom_temp'].set(result.temperature)
        sensors['jroom_hum'].set(result.humidity)
    else:
        print("Error: %d" % result.error_code)
    
    time.sleep(10)


