from abc import ABCMeta, abstractmethod
from vehicle.wheelEnum import WheelEnum

class ActionVehicle(object):
    __metaclass__ = ABCMeta

    def __init__(self,puissance=100):
        self.isStop = True
        self.isCont = False
        self.isFinish = True
        self.puissance = int(puissance)
        self.puissanceActu = 1
    def stop(self):
        print "Stopping"
        self.isCont = False
        while not self.isFinish:
            pass
        self.disableMoter()
        self.isStop = True
        print "Stopped"
    
    @abstractmethod
    def isAdvance(self):
        pass
    
    @abstractmethod
    def isReverse(self):
        pass
    def disableMoter(self):
        WheelEnum.LEFT_UP.disableEngine()
        WheelEnum.LEFT_DOWN.disableEngine()
        WheelEnum.RIGHT_UP.disableEngine()
        WheelEnum.RIGHT_DOWN.disableEngine()
    def setPuissance(self,puissance):
        self.puissance = puissance
        if self.isFinish:
            return False
        return True
