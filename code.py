#import board support libraries, including HID.
import board
import digitalio
import analogio
import usb_hid

from time import sleep

#Libraries for communicating as a Keyboard device
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

#library for communicating as a gamepad
from hid_gamepad import Gamepad

from adafruit_hid.mouse import Mouse
mouse = Mouse(usb_hid.devices)

from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.consumer_control import ConsumerControl

mediacontrol = ConsumerControl(usb_hid.devices)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
gp = Gamepad(usb_hid.devices)

#Create a collection of GPIO pins that represent the buttons
#This includes the digital pins for the Directional Pad.
#They can be used as regular buttons if using the analog inputs instead
button_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP19, board.GP16, board.GP20, board.GP17, board.GP21, board.GP18, board.GP10, board.GP11, board.GP12, board.GP13,board.GP14, board.GP15)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
gamepad_buttons = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

#Keyboard Mode Button Definitions
keyboard_buttons = {0 : Keycode.UP_ARROW, 1 : Keycode.LEFT_ARROW, 2 : Keycode.DOWN_ARROW, 3 : Keycode.RIGHT_ARROW,
                  4 : Keycode.LEFT_CONTROL, 5 : Keycode.SPACE, 6 : Keycode.W, 7 : Keycode.ENTER, 8 : Keycode.LEFT_ALT
                    , 9 : Keycode.ENTER, 10 : Keycode.ENTER, 11 : Keycode.ENTER, 12 : Keycode.ENTER, 13 : Keycode.ENTER
                    , 14 : Keycode.ENTER, 15 : Keycode.ENTER}

#FPS Mode Button Definitions
fps_buttons = {0 : Keycode.W, 1 : Keycode.A, 2 : Keycode.S, 3 : Keycode.D,
                  4 : Keycode.LEFT_CONTROL, 5 : Keycode.SPACE, 6 : Keycode.LEFT_ALT, 7 : Keycode.ENTER,
               8 : Keycode.ENTER, 9 : Keycode.ENTER, 10 : Keycode.ENTER, 11 : Keycode.ENTER, 12 : Keycode.ENTER
               , 13 : Keycode.ENTER, 14 : Keycode.ENTER, 15 : Keycode.ENTER}

#List of defind mode names
mode_names = {1 : 'Gamepad', 2 : 'Keyboard', 3 : 'FPS', 4 : "Mouse", 5 : "Multimedia"}

#Set Default Mode To 1
mode = 1

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]

#Initialize The Buttons
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    
# Setup for Analog Joystick as X and Y
ax = analogio.AnalogIn(board.GP26)
ay = analogio.AnalogIn(board.GP27)

# Equivalent of Arduino's map() function.
def range_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
  
def debounce():
    sleep(0.2)

while True:
    setx = 0
    sety = 0
    #Not keyboard presses for directional
    #So check them seperately first
    if not buttons[0].value:
        sety = -127
    if not buttons[2].value:
        sety = 127
    if not buttons[1].value:
        setx = -127
    if not buttons[3].value:
        setx = 127
    #Set Joystick movements
    gp.move_joysticks(
        x=setx,
        y=sety,
    )
        
    # Go through all the button definitions, and
    # press or release as appropriate
    for i, button in enumerate(buttons):
        if i > 3: #Skip the first 4, since they're the directionals
            gamepad_button_num = gamepad_buttons[i - 4] # Minus 4 to ignore directionals
            if button.value:
                gp.release_buttons(gamepad_button_num)
            else:
                gp.press_buttons(gamepad_button_num)