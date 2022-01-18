from legomario import Mario
import asyncio


def gyro_hook(x, y, z):
    print(f"X: {x} Y: {y} Z: {z}")


mario = Mario()
mario.AddAccelerometerHook(gyro_hook)
print("Turn on Mario and press the Bluetooth button")
loop = asyncio.get_event_loop()
loop.run_until_complete(mario.Run())
