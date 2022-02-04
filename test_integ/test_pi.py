import imp
import unittest
from hal.pi import RaspberryCPUTemp
from hal import SensorConfig
import time


class TestRasbberryCPUTemp(unittest.TestCase):
    def test_sane_temp(self):
        config = SensorConfig('foo', 2)
        temp = RaspberryCPUTemp(config).latest()
        self.assertAlmostEqual(temp.timestamp, time.time(), 1)
        for reading in temp.readings:
            self.assertGreaterEqual(reading, 10)
            self.assertLessEqual(reading, 100)



