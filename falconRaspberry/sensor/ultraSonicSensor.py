import RPi.GPIO as GPIO
import time
from threading import Thread
from observable import Observable


class UltraSonicSensor(Thread, Observable):

	DISTANCE_DEFAULT = 5

	def __init__(self, trig, echo):
		Thread.__init__(self)
		self.trig = trig
		self.echo = echo
		self.distance = UltraSonicSensor.DISTANCE_DEFAULT
		Observable.__init__(self)
        self.cont = True

	def run(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.trig, GPIO.OUT)  # Set pin as GPIO out
		GPIO.setup(self.echo, GPIO.IN)
		while self.cont:
			GPIO.output(self.trig, False)  # Set TRIG as LOW
			print "Waitng For Sensor To Settle"
			time.sleep(2)  # Delay of 2 seconds

			GPIO.output(self.trig, True)  # Set TRIG as HIGH
			time.sleep(0.00001)  # Delay of 0.00001 seconds
			GPIO.output(self.trig, False)  # Set TRIG as LOW

			while GPIO.input(self.echo) == 0:  # Check whether the ECHO is LOW
                                pulse_start = time.time()  # Saves the last known time of LOW pulse

			while GPIO.input(self.echo) == 1:  # Check whether the ECHO is HIGH
                                pulse_end = time.time()  # Saves the last known time of HIGH pulse

			pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable

			# Multiply pulse duration by 17150 to get distance
			distance = pulse_duration * 17150
			distance = round(distance, 2)  # Round to two decimal points
			self.setDistance(distance)
			self.update_observers(distance)

	def setDistance(self,distance):
	        self.distance = distance

	def getDistance(self):
		return self.distance
	def clearDistance(self):
		self.distance = UltraSonicSensor.DISTANCE_DEFAULT
	def stop(self):
		self.cont = False
