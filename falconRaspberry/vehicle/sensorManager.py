from vehicle.sensor.sensorEnum from SensorEnum
from vehicle.sensor.observeObstacle from ObserveObstacle
from command import Command
class SensorManager(ObserveObstacle):

    UP = "up"
    DOWN = "down"
    DISTANCE_MIN_UP = 20
    DISTANCE_MIN_DOWN = 20
    def __init__(vehiculeCommand):
        self.vehiculeCommand = vehiculeCommand
        self.up = ObserverObstacle(SensorEnum.ULTRASONIC_UP,self,SensorManager.UP)
        self.down = ObserverObstacle(SensorEnum.ULTRASONIC_DOWN,self,SensorManager.DOWN)
        self.up.start()
        self.down.start()
    
    def update(self,name,distance)
        if name == SensorManager.UP:
            if distance > SensorManager.DISTANCE_MIN_UP:
                self.vehiculeCommand.update(Command.NONE_OBSTACLE_FRONT)
            else:
                 self.vehiculeCommand.update(Command.OBSTACLE_FRONT)
        elif name == SensorManager.UP:
            if distance > SensorManager.DISTANCE_MIN_DOWN:
                self.vehiculeCommand.update(Command.NONE_OBSTACLE_BOTTOM)
            else:
                 self.vehiculeCommand.update(Command.OBSTACLE_BOTTOM)



class ObserverObstacle(ObserveObstacle):
    def __init__(sensor,sensorManager,name)
        ObserveObstacle.__init__(self)
        self.sensor = sensor
        self.sensorManager = sensorManager
        self.name = self.name
        sensor.register(self)

    def update(self,distance)
        self.sensorManager(name,distance)