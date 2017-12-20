from abc import ABCMeta, abstractmethod
from threading import Thread
from vehicle.wheelEnum import WheelEnum

class ActionVehicle(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        Thread.__init__(self)
        self.isStop = False
    def stop(self):
        self.isStop = True
        while not self.isFinish:
            pass
        WheelEnum.LEFT_UP.disableEngine()
        WheelEnum.LEFT_DOWN.disableEngine()
        WheelEnum.RIGHT_UP.disableEngine()
        WheelEnum.RIGHT_DOWN.disableEngine()
    
    @abstractmethod
    def isAdvance(self):
        pass
    
    @abstractmethod
    def isReverse(self):
        pass
