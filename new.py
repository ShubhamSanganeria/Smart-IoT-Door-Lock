import sys
import RPi.GPIO as GPIO
from pad4pi import rpi_gpio
import i2c_driver
from time import *
from psswd import pwd
from servo import serv
from mssg import send_mssg as msg
from photo import ph
from em import send_em

def main():
	GPIO.setmode(GPIO.BCM)
lcd=i2c_driver.lcd()
lcd.lcd_clear()
KEYPAD=[[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
Row=[23,14,15,17]
Col=[24,27,22]
fact=rpi_gpio.KeypadFactory()
keypad=fact.create_keypad(keypad=KEYPAD,row_pins=Row,col_pins=Col)
flag=0
s=""
t=0
def touch():
	global flag
	lcd.lcd_clear()
	lcd.lcd_display_string("Touch Sensor",1)
	pin=25
	GPIO.setup(pin,GPIO.IN)
	while True:
		padPressed=GPIO.input(pin)
		if(padPressed):
			flag=1
			lcd.lcd_display_string("Enter Password")
			break
def printKey(key):
	global flag
	global s
	global t
	if(flag==1):
		print("HI")
		print(len(s))
		if(len(s)==4):
			if(key=="#"):
				print("Entered")
				s=""
				f=0
				lcd.lcd_clear()
				lcd.lcd_display_string("Enter Password")
			elif(key=="*"):
				print("Entered")
				if(int(s)==pwd):
					t=0
					flag=0
					lcd.lcd_clear()
					lcd.lcd_display_string("Password Correct",1)
					sleep(0.5)
					serv(26,50)
					sleep(1)
		
				else:
					t=t+1
					lcd.lcd_clear()
					lcd.lcd_display_string("Password Incorrect",1)
					if(t>2):
						lcd.lcd_clear()
						lcd.lcd_display_string("Security Breach")
						msg()
						ph()
						sleep(1)
						send_em()						
						flag=0
						t=0
				s=""
				touch()

		elif(len(s)<4):
			lcd.lcd_display_string("#",2,(len(s)+1))
			s=s+str(key)
			print(s)
		
				
			

		

def proceed():
	try:
	
		keypad.registerKeyPressHandler(printKey)
	except KeyboardInterrupt:
		keypad.cleanup()
		sys.exit()

if __name__=="__main__":
	main()
	try:
		touch()
		proceed()
	except KeyboardInterrupt:
		keypad.cleanup()
		sys.exit()


