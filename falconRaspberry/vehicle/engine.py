import RPi.GPIO as GPIO

class Engine:
	FREQUENCY = 100
	BOOT_FEQUENCY = 10
	def __init__(self, high, mid, low ):
		self.high = high
		self.mid = mid 
		self.low = low
		self.pwmHigh = None
		self.pwmMid = None
		self.pwmLow = None
	def getHigh(self):
		return self.high
	def getMid(self):
		return self.mid
	def getLow(self):
		return self.low
	def makeOut(self, pin):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.OUT)
	def makeHighOut(self):
		 self.makeOut(self.high)
	def makeMidOut(self):
		self.makeOut(self.mid)
	def makeLowOut(self):
		self.pwmLow = self.makeOut(self.low)
	def makeAllOut(self):
		self.makeHighOut()
		self.makeMidOut()
		self.makeLowOut()
	def enableOutPin(self,pin):
		GPIO.setmode(GPIO.BOARD)
		self.makeOut(pin)
		GPIO.output(pin, GPIO.HIGH)
		return GPIO.PWM(pin,Engine.FREQUENCY)
	def disableOutPin(self,pin):
		GPIO.setmode(GPIO.BOARD)
		self.makeOut(pin)
		GPIO.output(pin, GPIO.LOW)
	def stopMid(self):
		if self.pwmMid != None:
			self.pwmMid.stop()
			self.pwmMid = None
	
	def stopHigh(self):
		if self.pwmHigh != None:
			self.pwmHigh.stop()
			self.pwmHigh = None
	def stopLow(self):
		if self.pwmLow != None:
			self.pwmLow.stop()
			self.pwmLow = None
	def enableOutHigh(self):
		self.stopHigh()
		self.pwmHigh = self.enableOutPin(self.high)
	def enableOutMid(self):
		self.stopMid()
		self.pwmMid = self.enableOutPin(self.mid)
	def enableOutLow(self):
		self.stopLow()
		self.pwmLow = self.enableOutPin(self.low)
	def disableOutHigh(self):
		self.stopHigh()
		self.disableOutPin(self.high)
	def disableOutMid(self):
		self.stopMid()
		self.disableOutPin(self.mid)
	def disableOutLow(self):
		self.stopLow()
		self.disableOutPin(self.low)
		
	def accelerate(self,frequency=None):
		if frequency != None:
			self.pwmHigh.ChangeDutyCycle(frequency)
			self.pwmLow.ChangeDutyCycle(frequency)
		else:
			self.enableOutHigh()
			self.enableOutLow()
			self.disableOutMid()
			self.pwmHigh.start(Engine.BOOT_FEQUENCY)
			self.pwmLow.start(Engine.BOOT_FEQUENCY)
	def reverse(self,frequency=None):
		if frequency != None:
			self.pwmHigh.ChangeDutyCycle(frequency)
			self.pwmMid.ChangeDutyCycle(frequency)
		else:
			self.enableOutHigh()
			self.enableOutMid()
			self.disableOutLow()
			self.pwmHigh.start(Engine.BOOT_FEQUENCY)
			self.pwmMid.start(Engine.BOOT_FEQUENCY)
    	
	def brake(self):
		self.enableOutHigh()
		self.enableOutMid()
		self.enableOutLow()
		self.pwmHigh.start(Engine.FREQUENCY)
		self.pwmMid.start(Engine.FREQUENCY)
		self.pwmLow.start(Engine.FREQUENCY)
	def disableEngine(self):
		self.disableOutHigh()
		self.disableOutMid()
		self.disableOutLow()
