import evdev
from evdev import ecodes as e
from evdev import AbsInfo, UInput
import time
from random import randint


# devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
# device = devices[10]#huion tablet
# ui = UInput.from_device(device, name="virtual tablet")


cap = {
e.EV_KEY : [e.BTN_DIGI, e.BTN_TOOL_PEN, e.BTN_TOUCH, e.BTN_STYLUS, e.BTN_STYLUS2],
e.EV_ABS : [(e.ABS_X, AbsInfo(value=0, min=0, max=8340, fuzz=0, flat=0, resolution=79)),
            (e.ABS_Y, AbsInfo(value=0, min=0, max=4680, fuzz=0, flat=0, resolution=79)),
            (e.ABS_PRESSURE, AbsInfo(value=0, min=0, max=2047, fuzz=0, flat=0, resolution=0))],
e.EV_MSC : [e.MSC_SCAN]
}


ui = UInput(cap, name="my tablet")
# print(ui.capabilities(verbose=True))


while True:
  inp = input()
    
  ui.write(e.EV_ABS, e.ABS_X, randint(1000,2000))
  ui.write(e.EV_ABS, e.ABS_Y, randint(1000,2000))
  ui.write(e.EV_KEY, e.BTN_DIGI, 1)
  ui.write(e.EV_KEY, e.BTN_TOOL_PEN, 1)
  ui.write(e.EV_KEY, e.BTN_TOUCH, 1)
  ui.write(e.EV_ABS, e.ABS_PRESSURE, 2000)
  ui.syn()
  ui.write(e.EV_ABS, e.ABS_X, randint(1000,2000))
  ui.write(e.EV_ABS, e.ABS_Y, randint(1000,2000))
  ui.syn()  
  ui.write(e.EV_KEY, e.BTN_DIGI, 0)
  ui.write(e.EV_KEY, e.BTN_TOOL_PEN, 0)
  ui.write(e.EV_KEY, e.BTN_TOUCH, 0)
  ui.syn()