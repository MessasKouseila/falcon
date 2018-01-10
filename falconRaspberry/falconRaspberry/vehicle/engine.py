import RPi.GPIO as GPIO

class Engine:
	FREQUENCY = 100
	BOOT_FREQUENCY = 10
	def __init__(self, high, mid, low ):
		self.high = high
		self.mid = mid 
		self.low = low
		self.enableOutHigh()
		self.pwmHigh = GPIO.PWM(high,Engine.FREQUENCY)
		self.pwmHigh.start(0)
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
	def disableOutPin(self,pin):
		GPIO.setmode(GPIO.BOARD)
		self.makeOut(pin)
		GPIO.output(pin, GPIO.LOW)
	
	def enableOutHigh(self):
		self.enableOutPin(self.high)
	def enableOutMid(self):
		self.enableOutPin(self.mid)
	def enableOutLow(self):
		self.enableOutPin(self.low)
	def disableOutHigh(self):
		self.disableOutPin(self.high)
	def disableOutMid(self):
		self.disableOutPin(self.mid)
	def disableOutLow(self):
		self.disableOutPin(self.low)
		
	def accelerate(self,frequency=None):
		if frequency != None:
			self.pwmHigh.ChangeDutyCycle(frequency)
		else:
			self.enableOutHigh()
			self.enableOutLow()
			self.disableOutMid()
			self.pwmHigh.ChangeDutyCycle(Engine.BOOT_FREQUENCY)
	def reverse(self,frequency=None):
		if frequency != None:
			self.pwmHigh.ChangeDutyCycle(frequency)
		else:
			self.enableOutHigh()
			self.enableOutMid()
			self.disableOutLow()
			self.pwmHigh.ChangeDutyCycle(Engine.BOOT_FREQUENCY)
    	
	def brake(self):
		self.enableOutMid()
		self.enableOutLow()
		self.pwmHigh.ChangeDutyCycle(Engine.FREQUENCY)
		
	def disableEngine(self):
		self.disableOutHigh()
		self.disableOutMid()
		self.disableOutLow()
