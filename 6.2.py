import RPi.GPIO as GPIO
import dht11
import time
import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
dht11 = dht11.DHT11(pin=4)
while True:
	result = dht11.read()
	if result.is_valid():
		print("Last valid input: " + str(datetime.datetime.now()))
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)
	time.sleep(1)		
