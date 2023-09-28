import win32api
import win32con
import time

ROTATIONS = [win32con.DMDO_DEFAULT, win32con.DMDO_90, win32con.DMDO_180, win32con.DMDO_270]


def rotate_screen(rotation):
    device = win32api.EnumDisplayDevices(None, 0)

    # Debugging information
    print(f"Device Name: {device.DeviceName}")
    print(f"Device String: {device.DeviceString}")
    print(f"State Flags: {device.StateFlags}")

    dm = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)

    # More debugging information
    print(f"Current Rotation: {dm.DisplayOrientation}")

    dm.DisplayOrientation = rotation
    win32api.ChangeDisplaySettingsEx(device.DeviceName, dm)


while True:
    for rotation in ROTATIONS:
        rotate_screen(rotation)
        time.sleep(20)
