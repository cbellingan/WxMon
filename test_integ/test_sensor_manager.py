import unittest
from hal import SensorManager, SensorConfig
from hal import SensorABC, Reading, Result, Units
import time
import os


class MockSensor(SensorABC):
    def __init__(self, config):
        super(MockSensor, self).__init__(config)
        self.last_call = None

    def start(self) -> bool:
        super(MockSensor, self).start()
        self.last_call = 'start'
        return True

    def stop(self) -> bool:
        super(MockSensor, self).stop()
        self.last_call = 'stop'
        return True

    def stop_sensor(self) -> bool:
        return 'stopped'

    def init(self) -> bool:
        super(MockSensor, self).init()
        self._enabled = True
        self.last_call = 'init'
        return self.enabled
    
    def close(self):
        pass

    @staticmethod
    def cap_fn() -> Result:
        ts = time.time()
        temperature = ts + 100
        return Result(
            timestamp=ts,
            readings=[Reading(
                unit=Units.DegC, 
                value=temperature,
                name='tsp100'
                )]
            )
    

class TestHAL(unittest.TestCase):
    def test_sensor_initialization(self):
        self.assertTrue(True)
        config = SensorConfig('foo', 2)
        sensors = SensorManager()
        sensors.register(cls=MockSensor, config=config)
        test_sensor = sensors._sensor_list[0]
        self.assertTrue(isinstance(test_sensor, MockSensor))
        self.assertEqual(test_sensor._config, config)
        sensors.init()
        self.assertEqual(test_sensor.last_call, 'init')
        
        sensors.start()
        self.assertEqual(test_sensor.last_call, 'start')
        time.sleep(3)
        sensors.stop()
        self.assertEqual(test_sensor.last_call, 'stop')

    def test_thread_handling(self):
        config = SensorConfig('foo', 2)
        sensors = SensorManager()
        sensors.register(cls=MockSensor, config=config)
        test_sensor = sensors._sensor_list[0]
        sensors.init()
        sensors.start()
        time.sleep(3)
        sensors.stop()
        self.assertEqual(test_sensor.last_call, 'stop')


        

