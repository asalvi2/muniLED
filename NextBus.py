import urllib
import RPi.GPIO as GPIO
import time

from xml.dom import minidom
#busNum=0 for first bus, 1 for second, 2 for third,..., 4 for fifth
def getBusTime(busNum):
	NextBUSUrl = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&r=N&s=3212&useShortTitles=true"
	#NextBUSUrl = "http://webservices.nextbus.com/service/publicXMLFEED?command=routeConfig&a=sf-muni&r=N"

	nbXML = urllib.urlopen(NextBUSUrl)
	readXML = minidom.parse(nbXML)

	busTimesMinutes = []
	busTimesSeconds = []
	stop = []

	for node in readXML.getElementsByTagName("predictions"):
		stop.append({
			'route': node.getAttribute("routeTag"),
			'stop': node.getAttribute("stopTitle"),
			'stID': node.getAttribute("StopTag")
		}) 

	for node in readXML.getElementsByTagName("prediction"):
		busTimesMinutes.append({
			'min': node.getAttribute('minutes')
		})
		busTimesSeconds.append({
			'sec': node.getAttribute('seconds')
		})		

	nextTime = "temp"
	beginTime = 0
	endTime = 0
	timeStrLen = 0
	fullTime = ""

	for i in range(1): #(len(busTimesMinutes)):
		nextTime = str(busTimesMinutes[i+busNum])
		beginTime = nextTime.find("u'")+2
		endTime = nextTime.find("}")-1
		fullTime = ""
		timeStrLen = endTime-beginTime
		for j in range(endTime-beginTime):
			fullTime = fullTime+nextTime[beginTime+j]

		print fullTime
		#print str(nextTime)[5]
		print str(busTimesMinutes[i+busNum]) + str(busTimesSeconds[i+busNum])
	
	return fullTime

def busLights(time1, pin1R, pin1G, pin1B, time2, pin2R, pin2G, pin2B):
	GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(pin1R, GPIO.OUT)
	#GPIO.setup(pin1G, GPIO.OUT)
	#GPIO.setup(pin1B, GPIO.OUT)
	print "next buses arrive in " + str(time1) + " and " + str(time2) +  " minutes"
	if int(time1) <= 6:
		if int(time1) >= 4:
			GPIO.setup(pin1B, GPIO.OUT)
			GPIO.output(pin1B, GPIO.LOW)
		GPIO.setup(pin1R, GPIO.OUT)
		GPIO.output(pin1R, GPIO.LOW)
	elif	int(time1) > 6 and int(time1) <=11:
		GPIO.setup(pin1G, GPIO.OUT)
		GPIO.output(pin1G, GPIO.LOW)
	else:
		GPIO.setup(pin1B, GPIO.OUT)
		GPIO.output(pin1B, GPIO.LOW)

	if int(time2) <=6:
		GPIO.setup(pin2R,GPIO.OUT)
		GPIO.output(pin2R,GPIO.LOW)
	elif	int(time2) > 6 and int(time2) <=11:
		GPIO.setup(pin2G, GPIO.OUT)
		GPIO.output(pin2G,GPIO.LOW)
	else:
		GPIO.setup(pin2B, GPIO.OUT)
		GPIO.output(pin2B, GPIO.LOW)	
	time.sleep(12)	
	return

for k in range(3):
	firstTime = getBusTime(0)
	secondTime = getBusTime(1)
	busLights(firstTime, 11, 13, 15, secondTime, 16, 22, 18)
	GPIO.cleanup()
