from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class AdvanceLeft(Thread,ActionVehicle):
    def __init__(self):
        ActionVehicle.__init__(self)
        self.isStop = False
    def run(self):
        self.isFinish = False
        WheelEnum.LEFT_UP.accelerate()
        WheelEnum.LEFT_DOWN.accelerate()
        WheelEnum.RIGHT_DOWN.disableEngine()
        WheelEnum.RIGHT_UP.disableEngine()
        i = 60
        while i <= 100 and (not self.isStop):
            WheelEnum.LEFT_UP.accelerate(i)
            WheelEnum.LEFT_DOWN.accelerate(i)
            i = i + 10
            time.sleep(0.1)
        self.isFinish = True

    
    def isAdvance(self):
        return True
    
    def isReverse(self):
        return False