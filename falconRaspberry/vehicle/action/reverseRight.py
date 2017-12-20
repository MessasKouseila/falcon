from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class ReverseRight(Thread,ActionVehicle):
    def __init__(self):
        ActionVehicle.__init__(self)
        self.isStop = False
    def run(self):
        self.isFinish = False
        WheelEnum.RIGHT_UP.reverse()
        WheelEnum.RIGHT_DOWN.reverse()
        WheelEnum.LEFT_UP.disableEngine()
        WheelEnum.LEFT_DOWN.disableEngine()
        i = 60
        while i <= 100 and (not self.isStop):
            WheelEnum.RIGHT_UP.reverse(i)
            WheelEnum.RIGHT_DOWN.reverse(i)
            i = i + 10
            time.sleep(0.1)
        self.isFinish = True

    def isAdvance(self):
        return False
    
    def isReverse(self):
        return True