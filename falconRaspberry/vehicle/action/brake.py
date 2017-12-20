from vehicle.wheelEnum import WheelEnum
from actionVehicle import ActionVehicle
import time

class Brake(ActionVehicle):
    def __init__(self):
        ActionVehicle.__init__(self)
    def run(self):
        self.isFinish = False
        WheelEnum.LEFT_UP.brake()
        WheelEnum.LEFT_DOWN.brake()
        WheelEnum.RIGHT_DOWN.brake()
        WheelEnum.RIGHT_UP.brake()
        self.isFinish = True
    
    def isAdvance(self):
        return False
    
    def isReverse(self):
        return False