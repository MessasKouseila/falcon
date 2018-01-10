from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class ReverseRight(Thread,ActionVehicle):
    def __init__(self,puissance=100):
        Thread.__init__(self)
        ActionVehicle.__init__(self,puissance)
    def run(self):
        print "Run Reverse Right: "+str(self.puissance)
        self.isCont = True
        self.isStop = False
        WheelEnum.RIGHT_UP.reverse()
        WheelEnum.RIGHT_DOWN.reverse()
        WheelEnum.LEFT_UP.disableEngine()
        WheelEnum.LEFT_DOWN.disableEngine()
        while self.puissanceActu != self.puissance and ( self.isCont):
            print "Reverse Right Puissance: "+str(self.puissanceActu)
            WheelEnum.RIGHT_UP.reverse(self.puissanceActu)
            WheelEnum.RIGHT_DOWN.reverse(self.puissanceActu)
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