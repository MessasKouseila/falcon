from vehicle.command import Command

class Agent(object):
    """docstring for Agent."""
    def __init__(self, vehicle):
        self.vehicle = vehicle
    
    def advance(self,puissane=100):
        self.vehicle.update(Command.ADVANCE,puissane)
    def advance_left(self,puissane=100):
        self.vehicle.update(Command.ADVANCE_LEFT,puissane)

    def advance_right(self,puissane=100):
        self.vehicle.update(Command.ADVANCE_RIGHT,puissane)
    
    def reverse(self,puissane=100):
        self.vehicle.update(Command.REVERSE,puissane)
    
    def reverse_left(self,puissane=100):
        self.vehicle.update(Command.REVERSE_LEFT,puissane)
    def reverse_right(self,puissane=100):
        self.vehicle.update(Command.REVERSE_RIGHT,puissane)
    def brake(self,puissane=100):
        self.vehicle.update(Command.BRAKE,puissane)
    def disableMoter(self,puissane=100):
        self.vehicle.update(Command.DISABLE_MOTER,puissane)
        
