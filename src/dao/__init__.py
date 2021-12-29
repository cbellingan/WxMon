from abc import abstractclassmethod
from dataclasses import dataclass


@dataclass
class DbBase():
    @abstractclassmethod
    def init(self, config):
        pass

    @abstractclassmethod
    def connect(self):
        pass

    @abstractclassmethod
    def execute(self, sql_string: str):
        pass