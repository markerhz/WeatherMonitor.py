import RPi.GPIO as GPIO
import time
from datetime import datetime  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
blink=GPIO.PWM(24,500)
blink.start(0)
GPIO.setup(21,GPIO.IN)
St=0
while (1):
	da=datetime.now()
	microsec=da.microsecond
	if microsec> 700000:
		blink.ChangeDutyCycle(st)
	else:
		blink.ChangeDutyCycle(0)
		state=GPIO.input(21)
	if (state==1):
				st=50
	else:
				st=0
