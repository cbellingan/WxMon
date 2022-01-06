import logging
from abc import abstractclassmethod
from dataclasses import dataclass, field
from typing import List
from enum import Enum


class Units(Enum):
    DegC = 'deg_c'
    DegF = 'deg_f'


@dataclass
class Reading():
    unit: Units
    value: float
    name: str
    
    def __ge__(self, value):
        return self.value > value

    def __le__(self, value):
        return self.value < value

    def __str__(self):
        return f'{self.name}={self.value} [{self.unit}]'


@dataclass
class Result():
    timestamp: int
    readings: List[Reading] = field(default_factory=list)

    def _ge__(self, result):
        return self.readings > result.readings

    def _le__(self, result):
        return self.readings < result.readings

    def get(self, name):
        return [x for x in self.readings if x.name == name]

    def __str__(self):
        return f'{self.timestamp} : {str(self.readings)}'


@dataclass
class SensorABC():
    @abstractclassmethod
    def start(self) -> bool:
        pass

    @abstractclassmethod
    def init(self, rate: int) -> bool:
        pass

    @abstractclassmethod
    def close(self):
        pass

    @abstractclassmethod
    def latest(self) -> Result:
        pass


@dataclass
class SensorManager():

    @abstractclassmethod
    def register(self, cls, config):
        logging.info('register sensor')
        pass

    @abstractclassmethod
    def init(self):
        logging.info('init sensor')
        pass

    @abstractclassmethod
    def start(self):
        logging.info('start sensor')
        pass
