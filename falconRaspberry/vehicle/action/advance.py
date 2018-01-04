from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class Advance(Thread,ActionVehicle):
    def __init__(self,puissance=100):
        ActionVehicle.__init__(self,puissance)
    def run(self):
        print "Run Advance"
        self.isCont = True
        self.isStop = False
        WheelEnum.LEFT_UP.accelerate()
        WheelEnum.LEFT_DOWN.accelerate()
        WheelEnum.RIGHT_DOWN.accelerate()
        WheelEnum.RIGHT_UP.accelerate()
        while self.puissanceActu != self.puissance and (not self.isCont):
            WheelEnum.LEFT_UP.accelerate(self.puissanceActu)
            WheelEnum.LEFT_DOWN.accelerate(self.puissanceActu)
            WheelEnum.RIGHT_DOWN.accelerate(self.puissanceActu)
            WheelEnum.RIGHT_UP.accelerate(self.puissanceActu)
            if self.puissanceActu < self.puissance:
                self.puissanceActu = self.puissanceActu + 1
            else:
                self.puissanceActu = self.puissanceActu - 1
            time.sleep(0.5)
        self.isFinish = True
    
    def isAdvance(self):
        return True
    
    def isReverse(self):
        return False
    
