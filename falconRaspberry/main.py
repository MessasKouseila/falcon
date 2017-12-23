#from api.server import *
#app.run(host=getIp(), port=5000)
from vehicle.vehicleFactory import VehicleFactory
from agent.agent import Agent
import time
vehi = vehicleFactory.createVehicle()
agent = Agent(vehi)
agent.advance()
time.sleep(40)
agent.advance_left()
time.sleep(40)
agent.advance_right()
time.sleep(40)
agent.reverse()
time.sleep(40)
agent.reverse_left()
time.sleep(40)
agent.reverse_right()
time.sleep(40)