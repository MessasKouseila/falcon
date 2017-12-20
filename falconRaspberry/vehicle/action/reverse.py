from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
import time

class Reverse(ActionVehicle):
    def __init__(self):
        ActionVehicle.__init__(self)
    def run(self):
        self.isFinish = False
        WheelEnum.LEFT_UP.reverse()
        WheelEnum.LEFT_DOWN.reverse()
        WheelEnum.RIGHT_DOWN.reverse()
        WheelEnum.RIGHT_UP.reverse()
        i = 60
        while i <= 100 and (not self.isStop):
            WheelEnum.LEFT_UP.reverse(i)
            WheelEnum.LEFT_DOWN.reverse(i)
            WheelEnum.RIGHT_DOWN.reverse(i)
            WheelEnum.RIGHT_UP.reverse(i)
            i = i + 10
            time.sleep(0.1)
        self.isFinish = True
    
    def isAdvance(self):
        return False
    
    def isReverse(self):
        return True
    