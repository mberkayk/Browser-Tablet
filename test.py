from evdev import UInput, ecodes, AbsInfo
import evdev


file = open("file", 'w')

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
  file.write(device.path + " " +  device.name + " " + device.phys + "\n")

file.close()