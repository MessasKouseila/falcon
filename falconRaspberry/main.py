#from api.server import *
#app.run(host=getIp(), port=5000)
from vehicle.vehicleFactory import VehicleFactory
from agent.agent import Agent
import time
vehi = VehicleFactory().createVehicle()
agent = Agent(vehi)
time.sleep(10)
agent.advance_left()

