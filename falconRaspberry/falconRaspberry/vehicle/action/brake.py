from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class Brake(Thread,ActionVehicle):
    def __init__(self,puissance=100):
        Thread.__init__(self)
        ActionVehicle.__init__(self,puissance)
    def run(self):
        print "Run Brake: "+str(self.puissance)
        self.isCont = True
        self.isStop = False
        WheelEnum.LEFT_UP.brake()
        WheelEnum.LEFT_DOWN.brake()
        WheelEnum.RIGHT_DOWN.brake()
        WheelEnum.RIGHT_UP.brake()
        self.isFinish = True
    
    def isAdvance(self):
        return False
    
    def isReverse(self):
        return False