from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class DisableMoter(Thread,ActionVehicle):
    def __init__(self,puissance=100):
        Thread.__init__(self)
        ActionVehicle.__init__(self,puissance)
    def run(self):
        print "Run Disable Moter: "+str(self.puissance)
        self.isCont = True
        self.isStop = False
        self.disableMoter()
        self.isFinish = True
    
    def isAdvance(self):
        return False
    
    def isReverse(self):
        return False