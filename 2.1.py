import time
import RPi.GPIO as GPIO
redled_pin=23
greenled_pin=24 
GPIO.setmode(GPIO.BCM)
GPIO.setup(redled_pin,GPIO.OUT)
GPIO.setup(greenled_pin,GPIO.OUT)
pwm1=GPIO.PWM(redled_pin,50)
pwm2=GPIO.PWM(greenled_pin,50)
pwm1.start(0)
pwm2.start(0)
try:
	while True:
		for duty in range(0,100,5): 
			print("Duty cycle =",duty)
			pwm1.ChangeDutyCycle(duty)
			pwm2.ChangeDutyCycle(100-duty)
			time.sleep(0.2)
except KeyboardInterrupt:
	print("END")
	GPIO.cleanup()
