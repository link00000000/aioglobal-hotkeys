from time import sleep
import sys

import global_hotkeys

is_running = True

def shutdown():
    global_hotkeys.stop_checking_hotkeys()
    
    global is_running
    is_running = False

global_hotkeys.register_hotkeys([
    [["control", "shift", "7"], lambda: print("Key down"), lambda: print("Key up")],
    [["control", "shift", "Q"], None, shutdown]
])

global_hotkeys.start_checking_hotkeys()

while is_running:
    sleep(0.1)
