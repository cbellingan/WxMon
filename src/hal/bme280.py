from dataclasses import dataclass
import board
from adafruit_bme280 import basic as adafruit_bme280
import logging

from hal import SensorABC, Reading, Result, Units



class BME820Sensor(SensorABC):
    def __init__(self, config):
        logging.info('register bme')
        super(BME820Sensor, self).__init__(config)
        self._enabled = True

    @staticmethod
    def cap_fn() -> Result:
        ts = SensorABC.now()
        i2c = board.I2C()  # uses board.SCL and board.SDA which is a singleton class
        # https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/
        bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
        temp = bme280.temperature
        pres = bme280.pressure
        humi = bme280.relative_humidity
        alti = bme280.altitude
        return Result(
            timestamp=ts,
            readings=[
                Reading(
                    unit=Units.DegC, 
                    value=temp,
                    name='temperature'
                ),
                Reading(
                    unit=Units.hPa,
                    value=pres,
                    name='pressure'
                ),
                Reading(
                    unit=Units.Pct, 
                    value=humi,
                    name='humidity'
                ),
                Reading(
                    unit=Units.m,
                    value=alti,
                    name='altitude'
                ),
                ]
            )
    
        