# buttonbox
buttonbox with Raspberry Pico 2040, circuit-python, adafruit_hid

## recovery mode
Execute to get access to the mounted drive again, as Storage is disabled via boot.py
```python
import microcontroller
microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
microcontroller.reset()
```
