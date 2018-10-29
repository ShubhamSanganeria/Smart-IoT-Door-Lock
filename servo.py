import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
def serv(pin,freq):
	GPIO.setup(26,GPIO.OUT)
	pwm=GPIO.PWM(26,50)
	pwm.start(5)
	sleep(1)
	x=[5,4.5,4,3.5,3,2.5,2,1.5,1]

	for i in x:
		pwm.ChangeDutyCycle(i)
		sleep(0.03)

	sleep(10)
	pwm.ChangeDutyCycle(5)
	sleep(0.5)

 
	pwm.stop()


