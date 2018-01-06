from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class AdvanceLeft(Thread,ActionVehicle):
    def __init__(self,puissance=100):
        Thread.__init__(self)
        ActionVehicle.__init__(self,puissance)
    def run(self):
        print "Run Advance Left: "+str(self.puissance)
        self.isCont = True
        self.isStop = False
        WheelEnum.LEFT_UP.accelerate()
        WheelEnum.LEFT_DOWN.accelerate()
        WheelEnum.RIGHT_DOWN.disableEngine()
        WheelEnum.RIGHT_UP.disableEngine()
        i = 1
        while self.puissanceActu != self.puissance and ( self.isCont):
            print "Advance Left Puissance: "+str(self.puissanceActu)
            WheelEnum.LEFT_UP.accelerate(self.puissanceActu)
            WheelEnum.LEFT_DOWN.accelerate(self.puissanceActu)
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
