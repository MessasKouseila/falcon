from vehicleCommand import VehicleCommand
from sensorManager import SensorManager
class VehicleFactory(object):
    vehicle = None
    sensorManager = None
    def createVehicle(self):
        if VehicleFactory.vehicle == None:
            VehicleFactory.vehicle = VehicleCommand()
            VehicleFactory.sensorManager = SensorManager(VehicleFactory.vehicle)
        return VehicleFactory.vehicle
        
