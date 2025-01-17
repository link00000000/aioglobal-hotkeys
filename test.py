import asyncio

import global_hotkeys

is_running = True

def shutdown():
    global is_running
    is_running = False

async def main():
    global_hotkeys.register_hotkeys([
        [["control", "shift", "q"], None, shutdown],
        [["control", "shift", "7"], lambda: print("Key down"), lambda: print("Key up")]
    ])

    global_hotkeys.start_checking_hotkeys()

    while is_running:
        await asyncio.sleep(0.1)

    global_hotkeys.stop_checking_hotkeys()

if __name__ == "__main__":
    asyncio.run(main())
