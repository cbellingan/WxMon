[ ] Python installer
- [ ] research python installer
- [x] build env
[-] Ansible deps setup- nope using make
[ ] Hash out rough design

## Use cases
1. A thread for each sensor runs and captures data at a given rate.
1. Each thread returns the latest data so results are sent as a batch.
1. The PI serial number is used as board ident so we don't care about the sending interface
1. Sensor data is persisted to disk with timestamp to individual log files. 
1. Sensor log files are pushed in batches as part of a transaction and deleted once inserted.
1. Camera images are captured via a Camera sensor and it's filename persisted to an images table with timestamp.
1. A flat


## References
[aidafruit](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test)

