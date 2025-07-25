# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
keyboard.col_pins = (board.GP26,board.GP27,board.GP28)
keyboard.row_pins = (board.GP0,board.GP1,board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    value_when_pressed=False
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
OPEN_TERMINAL = KC.MACRO(Tap(KC.LGUI(KC.Q)))
OPEN_SCRATCHPAD = KC.MACRO(Press(KC.LGUI(KC.LSHIFT(KC.S))))

keyboard.keymap = [
    [OPEN_TERMINAL, OPEN_SCRATCHPAD, KC.MUTE, KC.MPRV, KC.MPLY, KC.MNXT,KC.F7,KC.F8,KC.F5]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()