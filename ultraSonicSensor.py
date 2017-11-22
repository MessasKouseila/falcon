import RPi.GPIO as GPIO                    
import time                                
from threading import Thread
from observable import observable

class UltraSonicSensor(Thread):

	DISTANCE_DEFAULT = 25
	TRIG = 18                                  #Associate gpio 24 to TRIG
	ECHO = 16                                  #Associate gpio 23 to ECHO

    """Thread chargé simplement d'afficher une lettre dans la console."""
	def __init__(self,trig,echo):
		Thread.__init__(self)
		self.trig = trig
		self.echo = echo

	def run(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.trig,GPIO.OUT)                  #Set pin as GPIO out
		GPIO.setup(self.echo,GPIO.IN)  
		while True:
			GPIO.output(TRIG, False)                 #Set TRIG as LOW
			print "Waitng For Sensor To Settle"
			time.sleep(2)                            #Delay of 2 seconds

			GPIO.output(self.trig, True)                  #Set TRIG as HIGH
			time.sleep(0.00001)                      #Delay of 0.00001 seconds
			GPIO.output(self.trig, False)                 #Set TRIG as LOW

			while GPIO.input(self.echo)==0:               #Check whether the ECHO is LOW
			pulse_start = time.time()              #Saves the last known time of LOW pulse

			while GPIO.input(self.echo)==1:               #Check whether the ECHO is HIGH
			pulse_end = time.time()                #Saves the last known time of HIGH pulse 

			pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

			distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
			distance = round(distance, 2)            #Round to two decimal points
			self.update_observers(distance)

	def setDistance(self,distance):
	        self.distance = distance

	def getDistance(self):
		return self.distance
	def clearDistance(self):
		self.distance = DISTANCE_DEFAULT



	
        


