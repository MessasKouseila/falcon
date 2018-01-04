from abc import ABCMeta, abstractmethod
from threading import Thread
from vehicle.wheelEnum import WheelEnum

class ActionVehicle(object):
    __metaclass__ = ABCMeta

    def __init__(self,puissance=100):
        Thread.__init__(self)
        self.isStop = True
        self.isCont = False
        self.isFinish = True
        self.puissance = puissance
        self.puissanceActu = 1
    def stop(self):
        print "Stopping"
        self.isCont = False
        while not self.isFinish:
            pass
        WheelEnum.LEFT_UP.disableEngine()
        WheelEnum.LEFT_DOWN.disableEngine()
        WheelEnum.RIGHT_UP.disableEngine()
        WheelEnum.RIGHT_DOWN.disableEngine()
        self.isStop = True
        print "Stopped"
    
    @abstractmethod
    def isAdvance(self):
        pass
    
    @abstractmethod
    def isReverse(self):
        pass

    def setPuissance(puissance):
        self.puissance = puissance
