import RPi.GPIO as GPIO
redled_pin=23
greenled_pin=24
blueled_pin=25
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
		r=int(input("Enter red value :"))
		g=int(input("Enter green value:"))
		b=int(input("Enter red value :"))
		pwm1.ChangeDutyCycle(r)
		pwm2.ChangeDutyCycle(g)
		pwm3.ChangeDutyCycle(b)
except KeyboardInterrupt:
	print("End program\n")
	GPIO.cleanup()
