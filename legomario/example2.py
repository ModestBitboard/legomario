import asyncio
from legomario import Mario
from time import sleep


def tile_hook(data):
    if data == hex(0xb8):
        print("Level Started!")
    elif data == hex(0xb7):
        print("Level Finished!")
        sleep(10)
        mario.Stop()
    else:
        print(f"Barcode: {data}")


mario = Mario()
mario.AddTileHook(tile_hook)
mario._doLog = False
print("Turn on Mario and press the Bluetooth button")
loop = asyncio.get_event_loop()
loop.run_until_complete(mario.Run())
print("Thanks for playing!")
