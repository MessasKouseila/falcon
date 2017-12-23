from vehicle.Command import Command

class Agent(object):
    """docstring for Agent."""
    def __init__(self, vehicle):
        self.vehicle = vehicle
    
    def advance():
        self.vehicle.update(Command.ADVANCE)
    def advance_left():
        self.vehicle.update(Command.ADVANCE_LEFT)

    def advance_right():
        self.vehicle.update(Command.ADVANCE_RIGHT)
    
    def reverse():
        self.vehicle.update(Command.REVERSE)
    
    def reverse_left():
        self.vehicle.update(Command.REVERSE_LEFT)
    def reverse_right():
        self.vehicle.update(Command.REVERSE_LEFT)
        