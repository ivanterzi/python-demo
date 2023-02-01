"""
создайте класс `Car`, наследник `Vehicle`
"""
import homework_02.engine
from homework_02.base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
