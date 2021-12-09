from abc import abstractclassmethod
from dataclasses import dataclass


@dataclass
class DbBase():
    @abstractclassmethod
    def init(self):
        pass

    @abstractclassmethod
    def start(self):
        pass