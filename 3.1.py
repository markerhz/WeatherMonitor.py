import time
import RPi.GPIO as GPIO
import random
redled_pin=23
greenled_pin=24
blueled_pin=25
random.seed()
GPIO.setmode(GPIO.BCM)
GPIO.setup(redled_pin,GPIO.OUT)
GPIO.setup(greenled_pin,GPIO.OUT)
GPIO.setup(blueled_pin,GPIO.OUT)
pwm1=GPIO.PWM(redled_pin,50)
pwm2=GPIO.PWM(greenled_pin,50)
pwm3=GPIO.PWM(blueled_pin,50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
try:
	while True:
		r=random.random()*100
		g=int(random.random()*100)
		b=random.randint(0,100)
		print("R = ",r," G = ",g," b = ",b)
		pwm1.ChangeDutyCycle(r)
		pwm2.ChangeDutyCycle(g)
		pwm3.ChangeDutyCycle(b)
		time.sleep(0.2)
except KeyboardInterrupt:
	print("End program\n")
	GPIO.cleanup()
