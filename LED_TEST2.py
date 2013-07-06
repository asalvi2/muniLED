import RPi.GPIO as GPIO
import time
import os

def blink(pin1,pin2,pin3,sleep_time):
	
	GPIO.setup(pin1,GPIO.OUT)
	GPIO.output(pin1,GPIO.HIGH)
	
	#time.sleep(sleep_time)
	#time.sleep(sleep_time)
	GPIO.output(pin1,GPIO.LOW)
	#GPIO.cleanup()
	time.sleep(sleep_time)
	
	#GPIO.setup(pin2,GPIO.OUT)
	#GPIO.output(pin2,GPIO.HIGH)
	
	#time.sleep(sleep_time)
	
	#GPIO.output(pin2,GPIO.LOW)
	#GPIO.cleanup()
	#time.sleep(sleep_time)
	
	#GPIO.setup(pin1,GPIO.OUT)
	#GPIO.output(pin1,GPIO.HIGH)
	
	#time.sleep(sleep_time)

	#GPIO.output(pin1,GPIO.LOW)

	#GPIO.cleanup()
	return

def colorTest(pinNum, sleep_time):
	
	GPIO.output(pinNum,GPIO.HIGH)
	time.sleep(sleep_time)
	GPIO.output(pinNum,GPIO.LOW)
	time.sleep(sleep_time)
	#GPIO.cleanup()
	return
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

p1 = 11 #red
p2 = 13 #green
p3 = 15 #blue
#p4 = 11
 	 	
#GPIO.setup(p1,GPIO.OUT)
#GPIO.setup(p2,GPIO.OUT)
#GPIO.setup(p3,GPIO.OUT)
#GPIO.setup(p4,GPIO.IN)

for i in range(0,5):
	blink(p1,p2,p3,1)
	GPIO.cleanup()
	blink(p1,p1,p3,1)
	GPIO.cleanup()
	blink(p1,p3,p2,1)
	GPIO.cleanup()

GPIO.cleanup()
#while True:
#	GPIO.setup(p4,GPIO.IN)
#	if (GPIO.input(p4) == False ):
#		colorTest(p1,3)
		#GPIO.cleanup();
#	GPIO.setup(p4,GPIO.IN)
#	if (GPIO.input(p4) == True):
#		colorTest(p2,2)
		#GPIO.cleanup();

