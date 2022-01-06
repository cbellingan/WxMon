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


@dataclass
class Persistor():
    def __init__(self, writer: DbBase) -> None:
        pass

    def init(self):
        pass

    def start(self):
        pass    