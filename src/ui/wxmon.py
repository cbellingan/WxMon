# import config

# from dao.mysql import DB
from dao import Persistor
from hal.bme280 import BME820Sensor
from hal.pi import RaspberryCPUTemp
from hal import SensorManager, SensorConfig
import logging
import time


logging.basicConfig(level=logging.DEBUG)

def main():
    logging.info('Entered main.')
    sensors = SensorManager()
    sensors.register(cls=BME820Sensor, config=SensorConfig('BME820', 0.2))
    sensors.register(cls=RaspberryCPUTemp, config=SensorConfig('CPUTemp', 1))
    sensors.init()
    sensors.start()
    time.sleep(5)
    sensors.stop()
    # persistor = Persistor(writer=DB(config=config.MySqlDb))
    # persistor.init()
    # persistor.start()
    # logging.info('Fin...')

if __name__ == '__main__':
    logging.debug('Starting')
    main()