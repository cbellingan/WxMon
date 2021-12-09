from abc import abstractclassmethod
from dataclasses import dataclass
import logging


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