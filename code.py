#import board support libraries, including HID.
import board
import digitalio
import rotaryio
import usb_hid

from time import sleep

#library for communicating as a gamepad
from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

enc1 = rotaryio.IncrementalEncoder(board.GP0, board.GP1)
enc1_last_position = enc1.position
enc1_current_position = enc1.position

enc2 = rotaryio.IncrementalEncoder(board.GP3, board.GP4)
enc2_last_position = enc2.position
enc2_current_position = enc2.position

enc3 = rotaryio.IncrementalEncoder(board.GP6, board.GP7)
enc3_last_position = enc3.position
enc3_current_position = enc3.position

# Create a collection of GPIO pins that represent the buttons
# The six GP-Pins (22-27) are not really used, it's just a hacky solution
# to get some buttons on the gamecontroller for the rotary encoders
button_pins = (board.GP11, board.GP10,
               board.GP12, board.GP13,
               board.GP14, board.GP15,
               board.GP19, board.GP20, board.GP21,
               board.GP16, board.GP17, board.GP18,
               board.GP2, board.GP5, board.GP8,
               board.GP22, board.GP23,
               board.GP24, board.GP25,
               board.GP26, board.GP27)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
gamepad_buttons = (1, 2, 3 ,4 ,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]

debounce_delay = 0.05

#Initialize The Buttons
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
      
while True:
    enc1_current_position = enc1.position
    if enc1_current_position > enc1_last_position:
        enc1_position_change = abs(enc1_current_position - enc1_last_position)
        for _ in range(enc1_position_change):
            gp.press_buttons(17)
            sleep(debounce_delay)
            gp.release_buttons(17)
            sleep(debounce_delay)
    elif enc1_current_position < enc1_last_position:
        enc1_position_change = abs(enc1_current_position - enc1_last_position)
        for _ in range(enc1_position_change):
            gp.press_buttons(16)
            sleep(debounce_delay)
            gp.release_buttons(16)
            sleep(debounce_delay)
    enc1_last_position = enc1_current_position
 
    enc2_current_position = enc2.position
    if enc2_current_position > enc2_last_position:
        enc2_position_change = abs(enc2_current_position - enc2_last_position)
        for _ in range(enc2_position_change):
            gp.press_buttons(19)
            sleep(debounce_delay)
            gp.release_buttons(19)
            sleep(debounce_delay)
    elif enc2_current_position < enc2_last_position:
        enc2_position_change = abs(enc2_current_position - enc2_last_position)
        for _ in range(enc2_position_change):
            gp.press_buttons(18)
            sleep(debounce_delay)
            gp.release_buttons(18)
            sleep(debounce_delay)
    enc2_last_position = enc2_current_position
    
    enc3_current_position = enc3.position
    if enc3_current_position > enc3_last_position:
        enc3_position_change = abs(enc3_current_position - enc3_last_position)
        for _ in range(enc3_position_change):
            gp.press_buttons(21)
            sleep(debounce_delay)
            gp.release_buttons(21)
            sleep(debounce_delay)
    elif enc3_current_position < enc3_last_position:
        enc3_position_change = abs(enc3_current_position - enc3_last_position)
        for _ in range(enc3_position_change):
            gp.press_buttons(20)
            sleep(debounce_delay)
            gp.release_buttons(20)
            sleep(debounce_delay)
    enc3_last_position = enc3_current_position
 
    for i in range(15):
        if buttons[i].value:
            gp.release_buttons(i+1)
        else:
            gp.press_buttons(i+1)
