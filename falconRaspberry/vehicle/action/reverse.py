from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
import time
from threading import Thread

class Reverse(Thread,ActionVehicle):
    def __init__(self,puissance=100):
        ActionVehicle.__init__(self,puissance)
    def run(self):
        print "Run Reverse"
        self.isCont = True
        self.isStop = False
        WheelEnum.LEFT_UP.reverse()
        WheelEnum.LEFT_DOWN.reverse()
        WheelEnum.RIGHT_DOWN.reverse()
        WheelEnum.RIGHT_UP.reverse()
        while self.puissanceActu <= self.puissance and (not self.isCont):
            WheelEnum.LEFT_UP.reverse(self.puissanceActu)
            WheelEnum.LEFT_DOWN.reverse(self.puissanceActu)
            WheelEnum.RIGHT_DOWN.reverse(self.puissanceActu)
            WheelEnum.RIGHT_UP.reverse(self.puissanceActu)
            if self.puissanceActu < self.puissance:
                self.puissanceActu = self.puissanceActu + 1
            else:
                self.puissanceActu = self.puissanceActu - 1
            time.sleep(0.5)
        self.isFinish = True
    
    def isAdvance(self):
        return False
    
    def isReverse(self):
        return True
    
