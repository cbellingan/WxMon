import unittest
from hal.pi import RaspberryCPUTemp
import time


class TestRasbberryCPUTemp(unittest.TestCase):
    def test_sane_temp(self):
        temp = RaspberryCPUTemp().latest()
        self.assertAlmostEqual(temp.timestamp, time.time(), 1)
        for reading in temp.readings:
            self.assertGreaterEqual(reading, 10)
            self.assertLessEqual(reading, 100)



