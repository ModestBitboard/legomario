import asyncio
from legomario import Mario


def tile_hook(data):
    print(f"Barcode: {data}")


mario = Mario()
mario.AddTileHook(tile_hook)
print("Turn on Mario and press the Bluetooth button")
loop = asyncio.get_event_loop()
loop.run_until_complete(mario.Run())
