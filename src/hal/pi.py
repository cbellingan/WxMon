from hal import SensorABC, Reading, Result, Units
import time
import os


class RaspberryCPUTemp(SensorABC):
    def start(self) -> bool:
        return True

    def init(self) -> bool:
        return True
    
    def close(self):
        pass

    def latest(self) -> Result:
        ts = time.time()
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
    
