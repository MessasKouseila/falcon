from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class ReverseLeft(Thread,ActionVehicle):
    def __init__(self,puissance=100):
        Thread.__init__(self)
        ActionVehicle.__init__(self,puissance)
    def run(self):
        print "Run Reverse Left: "+str(self.puissance)
        self.isCont = True
        self.isStop = False
        WheelEnum.LEFT_UP.reverse()
        WheelEnum.LEFT_DOWN.reverse()
        WheelEnum.RIGHT_DOWN.disableEngine()
        WheelEnum.RIGHT_UP.disableEngine()
        while self.puissanceActu != self.puissance and (self.isCont):
            print "Reverse Left Puissance: "+str(self.puissanceActu)
            WheelEnum.LEFT_UP.reverse(self.puissanceActu)
            WheelEnum.LEFT_DOWN.reverse(self.puissanceActu)
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
