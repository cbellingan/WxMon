import board
from adafruit_bme280 import basic as adafruit_bme280

#TODO define the interface... 
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

temp = bme280.temperature
pres = bme280.pressure
humi = bme280.relative_humidity
alti = bme280.altitude