"""
создайте класс `Car`, наследник `Vehicle`
"""
import homework_02.engine
from homework_02.base import Vehicle
from engine import Engine


class Car(Vehicle):
    engine: str

    def set_engine(self, engine):
        self.engine = engine
        self.volume = 5
        self.pistons = 5
        self.engine = homework_02.engine.Engine(self.volume, self.pistons)
