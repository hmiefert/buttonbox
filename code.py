#import board support libraries, including HID.
import board
import digitalio
import rotaryio
import usb_hid

#library for communicating as a gamepad
from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

enc1 = rotaryio.IncrementalEncoder(board.GP0, board.GP1)
enc2 = rotaryio.IncrementalEncoder(board.GP3, board.GP4)
enc3 = rotaryio.IncrementalEncoder(board.GP6, board.GP7)

enc1_last_pos = None
enc2_last_pos = None
enc3_last_pos = None
#Create a collection of GPIO pins that represent the buttons
#This includes the digital pins for the Directional Pad.
#They can be used as regular buttons if using the analog inputs instead )
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

#Initialize The Buttons
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
      
while True:
    pos1 = enc1.position
    if enc1_last_pos != None and pos1 > enc1_last_pos:
        gp.click_buttons(17)
    elif enc1_last_pos != None and pos1 < enc1_last_pos:
        gp.click_buttons(16)
    enc1_last_pos = pos1
 
    pos2 = enc2.position
    if enc2_last_pos != None and pos2 > enc2_last_pos:
        gp.click_buttons(19)
    elif enc2_last_pos != None and pos2 < enc2_last_pos:
        gp.click_buttons(18)
    enc2_last_pos = pos2
 
    pos3 = enc3.position
    if enc3_last_pos != None and pos3 > enc3_last_pos:
        gp.click_buttons(21)
    elif enc3_last_pos != None and pos3 < enc3_last_pos:
        gp.click_buttons(20)
    enc3_last_pos = pos3
 
    for btn_id, button in enumerate(buttons):
        if button.value:
            gp.release_buttons(btn_id+1)
        else:
            gp.press_buttons(btn_id+1)