"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle

class Plane (Vehicle) :

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0
    def load_cargo(self):
        pass

