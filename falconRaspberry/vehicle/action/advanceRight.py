from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
from threading import Thread
import time

class AdvanceRight(Thread,ActionVehicle):
    def __init__(self):
        ActionVehicle.__init__(self)
        self.isStop = False
    def run(self):
        self.isFinish = False
        WheelEnum.RIGHT_UP.accelerate()
        WheelEnum.RIGHT_DOWN.accelerate()
        WheelEnum.LEFT_UP.disableEngine()
        WheelEnum.LEFT_DOWN.disableEngine()
        i = 60
        while i <= 100 and (not self.isStop):
            WheelEnum.RIGHT_UP.accelerate(i)
            WheelEnum.RIGHT_DOWN.accelerate(i)
            i = i + 10
            time.sleep(0.1)
        self.isFinish = True

    
    def isAdvance(self):
        return True
    
    def isReverse(self):
        return False