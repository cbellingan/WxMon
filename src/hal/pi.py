from hal import SensorABC, Reading, Result, Units
import time
import os


class RaspberryCPUTemp(SensorABC):
    """
    Temperature sensor for the raspberry pi's internal temperature
    """
    def __init__(self, config):
        super(RaspberryCPUTemp, self).__init__(config)

    def start_sensor(self) -> bool:
        return True

    def init_sensor(self) -> bool:
        self._enabled = True
        return self.enabled
    
    def close(self):
        pass

    @staticmethod
    def cap_fn() -> Result:
        ts = time.time()
        # https://github.com/raspberrypi/linux/blob/7fb9d006d3ff3baf2e205e0c85c4e4fd0a64fcd0/Documentation/driver-api/thermal/sysfs-api.rst
        temperature =  float(
            open('/sys/class/thermal/thermal_zone0/temp', 'r').read()
        )
        temperature = temperature/1000
        return Result(
            timestamp=ts,
            readings=[Reading(
                unit=Units.DegC, 
                value=temperature,
                name='cpu_temp'
                )]
            )
    
