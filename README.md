# buttonbox
SimRacing buttonbox with Raspberry Pico 2040, circuit-python, adafruit_hid<br>
![buttonbox](https://raw.githubusercontent.com/hmiefert/buttonbox/6171ab1391504d43c9cc06a5e86e17c3a5892e63/img/buttonbox.jpg?raw=true)


## recovery mode
Execute to get access to the mounted drive again, as Storage is disabled via boot.py
```python
import microcontroller
microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
microcontroller.reset()
```
