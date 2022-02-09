from distutils.command.config import config
import logging
import os
from re import M
import time
from abc import abstractclassmethod
from dataclasses import dataclass, field
from tkinter.messagebox import NO
from typing import Dict, List
from enum import Enum
from multiprocessing import Process
import threading


@dataclass
class SensorConfig():
    name: str
    rate: int


class Units(Enum):
    DegC = 'deg_c'
    DegF = 'deg_f'
    NA = 'None'
    Pct = 'Percent'
    hPa = 'HectoPascal'
    m = 'Meters'


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
        return f'{self.timestamp} -> {str(self.readings)}'


class SensorABC():
    def __init__(self, config: SensorConfig) -> None:
        self._config = config
        self._enabled = False
        self._proc = None

    @staticmethod
    def now():
        return time.time()

    @property
    def enabled(self):
        return self._enabled

    @property
    def name(self):
        return str(self.__class__.__name__)

    @staticmethod
    def cap_fn():
        print('module name:', __name__)
        print('parent process:', os.getppid())
        print('process id:', os.getpid())
        print(f'Time: {time.time()}')
        return time.time()

    @staticmethod
    def _cap_thread(cap_fn, rate: int = 10):
        threading.Timer(
            interval=rate,
            function=SensorABC._cap_thread,
            args=(cap_fn, rate),
            ).start()
        logging.info(f'... {__class__.__name__} capturing at {rate}')
        ts_start = time.time()
        ret = cap_fn()
        fn_duration = time.time() - ts_start
        if fn_duration > rate:
            logging.warn(f'Capture druation {fn_duration} is greater than function rate {rate}')
        print(f'Got: {ret}')
        return ret

    @abstractclassmethod
    def start_sensor(self) -> bool:
        pass

    def start(self) -> bool:
        if self._proc is not None:
            self.start_sensor()
            logging.info(f'Starting capture process for {self.__class__.__name__} with pid: {self._proc.pid}')
            self._proc.start()
        else:
            logging.error(f"Can't start {self.__class__.__name__}, not initialized")

    @abstractclassmethod
    def stop_sensor(self) -> bool:
        pass

    def stop(self) -> bool:
        logging.info(f'Stopping sensor for {self.__class__.__name__}')
        if self._proc is not None:
            self._proc.terminate()
            self._proc = None
        return self.stop_sensor()

    @abstractclassmethod
    def init_sensor(self):
        logging.info(f'Init sensor {self.__class__.__name__}')
        pass

    def init(self) -> bool:
        """
        Perform the sensors initialization, any failures in the sensor should result
        in a sensor being disabled.
        """
        logging.info(f'Sensor init for {self.__class__.__name__}')
        if self._proc is None:
            self.init_sensor()
            proc_args = (self.cap_fn, self._config.rate)
            self._proc = Process(
                target=self._cap_thread,
                args=proc_args
            )
            logging.info(f'Process initialized: {self._proc.name} with {proc_args}')

    @abstractclassmethod
    def close(self):
        pass

    def latest(self) -> Result:
        return self.cap_fn()


class SensorManager():
    def __init__(self):
        self._sensor_list = []

    def register(self, cls, config=None):
        logging.info(f'register sensor: {cls.name}')
        self._sensor_list.append(cls(config=config))

    def init(self):
        logging.info('init sensors')
        for sensor_cls in self._sensor_list:
            sensor_cls.init()

    def start(self):
        logging.info('start sensors')
        for sensor_cls in self._sensor_list:
            if sensor_cls.enabled:
                sensor_cls.start()
                logging.info(f"Started {sensor_cls.name}")
            else:
                logging.info(f"Not starting {sensor_cls.name}")

    def stop(self):
        logging.info('Stopping sensors')
        for sensor_cls in self._sensor_list:
            if sensor_cls.enabled:
                sensor_cls.stop()
            else:
                logging.info(f"Can't stop {sensor_cls.name}")
