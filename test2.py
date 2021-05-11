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

    await global_hotkeys.listen()

if __name__ == "__main__":
    asyncio.run(main())
