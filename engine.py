import RPi.GPIO as GPIO

class Engine:
	
	def __init__(self, high, mid, low ):
		self.high = high
		self.mid = mid 
		self.low = low
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
		self.makeOut(self.low)
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
	def accelerate(self):
		self.enableOutHigh()
		self.enableOutLow()
		self.disableOutMid()
	def reverse(self):
		self.enableOutHigh()
		self.enableOutMid()
		self.disableOutLow()
	def brake(self):
		self.enableOutHigh()
		self.enableOutMid()
		self.enableOutLow()
        def disableEngine(self):
                self.disableOutHigh()
                self.disableOutMid()
                self.disableOutLow()
