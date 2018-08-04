import time
import RPi.GPIO as GPIO
led_pin=25;
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
p=GPIO.PWM(led_pin,50) 
p.start(0) 
while True:
	for duty in range(0,101,10): 
		p.ChangeDutyCycle(duty)
		time.sleep(0.2)
