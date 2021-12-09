from dao import mysql
from hal.bme280 import BME820Sensor
from hal import SensorManager
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    logging.info('Entered main.')
    sensors = SensorManager()
    config = dict(
        sample_period=60,
        output_period=300,
        aggregation='avg'
    )
    sensors.register(BME820Sensor, config)
    sensors.init()
    sensors.start()

    writer = mysql.MySqlDBWriter()
    writer.init()
    writer.start()
    logging.info('Fin...')

if __name__ == '__main__':
    logging.debug('Starting')
    main()