from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class ReverseLeft(Thread,ActionVehicle):
    def __init__(self):
        ActionVehicle.__init__(self)
        self.isStop = False
    def run(self):
        self.isFinish = False
        WheelEnum.LEFT_UP.reverse()
        WheelEnum.LEFT_DOWN.reverse()
        WheelEnum.RIGHT_DOWN.disableEngine()
        WheelEnum.RIGHT_UP.disableEngine()
        i = 60
        while i <= 100 and (not self.isStop):
            WheelEnum.LEFT_UP.reverse(i)
            WheelEnum.LEFT_DOWN.reverse(i)
            i = i + 10
            time.sleep(0.1)
        self.isFinish = True

    
    def isAdvance(self):
        return False
    
    def isReverse(self):
        return True