import urllib
import RPi.GPIO as GPIO
import time

from xml.dom import minidom


#busNum=0 for first bus, 1 for second, 2 for third,..., 4 for fifth
def getBusTime():
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
	#print busTimesMinutes

	for i in range(len(busTimesMinutes)):
		nextTime = str(busTimesMinutes[i-1])
		beginTime = nextTime.find("u'")+2
		endTime = nextTime.find("}")-1
		busTimesMinutes[i-1] = int(nextTime[beginTime:endTime])
		
	busTimesMinutes.sort()
	print busTimesMinutes
#	busTimesSeconds.sort()
	return busTimesMinutes

def busLights(time1, pin1R, pin1G, pin1B, time2, pin2R, pin2G, pin2B):
	
	GPIO.setmode(GPIO.BOARD)
	
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


##Example code to run check 3 times.
for k in range(1):
	busTimes = getBusTime()
	busLights(busTimes[0], 11, 13, 15, busTimes[1], 16, 22, 18)
	GPIO.cleanup()
