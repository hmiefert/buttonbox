# buttonbox
SimRacing buttonbox with Raspberry Pi Pico / RP2040, [circuit-python](https://circuitpython.org/board/raspberry_pi_pico) and [adafruit_hid](https://docs.circuitpython.org/en/latest/shared-bindings/usb_hid/index.html) from the [circuit-python-libraries](https://circuitpython.org/libraries) <br>
More Information on USB and HID [here](https://www.usb.org/sites/default/files/hid1_12.pdf) <br>
![buttonbox](https://raw.githubusercontent.com/hmiefert/buttonbox/6171ab1391504d43c9cc06a5e86e17c3a5892e63/img/buttonbox.jpg?raw=true)


## recovery mode
Execute to get access to the mounted drive again, as Storage is disabled via boot.py
```python
import microcontroller
microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
microcontroller.reset()
```
