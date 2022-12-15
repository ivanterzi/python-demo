from abc import ABC

class Vehicle(ABC):

    def __int__(self, weight=1000, fuel=60, fuel_consumption=20, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started





#def test_cannot_start_low_fuel(vehicle):
 #   assert vehicle.started is False
  #  vehicle.fuel = 0
   # with pytest.raises(exceptions):
    #    vehicle.start()
     #   assert vehicle.started is False