from wheelEnum import WheelEnum
from vehicle.command import Command
from vehicle.action.actionVehicle import ActionVehicle
from vehicle.action.advance import Advance
from vehicle.action.advanceLeft import AdvanceLeft
from vehicle.action.advanceRight import AdvanceRight
from vehicle.action.reverse import Reverse
from vehicle.action.reverseLeft import ReverseLeft
from vehicle.action.reverseRight import ReverseRight
from vehicle.action.brake import Brake
import threading

def synchronized_method(method):
    
    outer_lock = threading.Lock()
    lock_name = "__"+method.__name__+"_lock"+"__"
    
    def sync_method(self, *args, **kws):
        with outer_lock:
            if not hasattr(self, lock_name): setattr(self, lock_name, threading.Lock())
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kws)  

    return sync_method
class VehicleCommand(object):

    def __init__(self):
        self.canAdvance = False
        self.canReverse = False
        self.action = {
        Command.ADVANCE :Advance,
        Command.ADVANCE_LEFT: AdvanceLeft,
        Command.ADVANCE_RIGHT: AdvanceRight,
        Command.REVERSE: Reverse,
        Command.REVERSE_LEFT: ReverseLeft,
        Command.REVERSE_RIGHT: ReverseRight,
        Command.OBSTACLE_FRONT: self.__obstacleUp,
        Command.OBSTACLE_BOTTOM: self.__obstacleDown,
        Command.NONE_OBSTACLE_FRONT: self.__noneObstacleUp,
        Command.NONE_OBSTACLE_BOTTOM: self.__noneObstacleDown,
        Command.BRAKE: Brake
        } 
        self.actionRunning = None       
    def __accelerate(self):
        WheelEnum.LEFT_UP.accelerate()
        WheelEnum.LEFT_DOWN.accelerate()
        WheelEnum.RIGHT_DOWN.accelerate()
        WheelEnum.RIGHT_UP.accelerate()
   
    def __obstacleUp(self):
        print "Obstacle Up"
        if self.actionRunning != None and self.actionRunning.isAdvance() and not self.actionRunning.isStop:
            self.actionRunning.stop()
            action = self.actionRunning
            self.actionRunning = type(action)()
            del(action)
        self.canAdvance = False
   
    def __noneObstacleUp(self):
        self.canAdvance = True
        print "none obstacle Up"
    def __obstacleDown(self):
        print "ObstacleDown"
        if self.actionRunning != None and isinstance(self.actionRunning,ActionVehicle) and self.actionRunning.isReverse() and not self.actionRunning.isStop:
               self.actionRunning.stop()
               action = self.actionRunning
               self.actionRunning = type(action)()
               del(action)
        self.canReverse =  False
    def __noneObstacleDown(self):
        self.canReverse = True
        print "none obstacle Down"
    
    @synchronized_method
    def update(self,command,puissance=None):
        if puissance == None:
            action = self.action[command]()
        else:
            action = self.action[command](puissance)
        if isinstance(action,ActionVehicle) and ((self.canAdvance and action.isAdvance()) or (self.canReverse and action.isReverse())) : 
            if type(action) == type(self.actionRunning):
                if not self.actionRunning.setPuissance(puissance):
                    self.actionRunning.stop()
                    action.puissanceActu = self.actionRunning.puissanceActu
                    del(self.actionRunning)
                    self.actionRunning = action    
            else:
                if self.actionRunning != None and not self.actionRunning.isStop:
                    self.actionRunning.stop()
                    del(self.actionRunning)
                self.actionRunning = action
            
        if isinstance(self.actionRunning,ActionVehicle) and  self.actionRunning.isStop and ((self.canAdvance and self.actionRunning.isAdvance()) or (self.canReverse and self.actionRunning.isReverse())):
            self.actionRunning.start()
            while self.actionRunning.isStop:
                pass
	    print str(command) + ":running" 
            
