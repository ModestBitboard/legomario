# Imports
import asyncio
from bleak import BleakScanner, BleakClient

# BLE Connection and Event Subscription
LEGO_CHARACTERISTIC_UUID = "00001624-1212-efde-1623-785feabcd123"
SUBSCRIBE_IMU_COMMAND = bytearray([0x0A, 0x00, 0x41, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x01])
SUBSCRIBE_RGB_COMMAND = bytearray([0x0A, 0x00, 0x41, 0x01, 0x00, 0x05, 0x00, 0x00, 0x00, 0x01])


class Mario:

    def __init__(self):
        self._newTileEventHooks = []
        self._tileEventHooks = []
        self._accelerometerEventHooks = []
        self._doLog = False
        self._run = True
        self._doHex = False

    def _signed(self, char):
        return char - 256 if char > 127 else char

    def _hex(self, msg):
        if self._doHex:
            print(str(msg))

    def _log(self, msg):
        if self._doLog:
            print(msg)

    def AddTileHook(self, func):
        self._tileEventHooks.append(func)

    def AddNewTileHook(self, func):
        self._newTileEventHooks.append(func)

    def AddAccelerometerHook(self, func):
        self._accelerometerEventHooks.append(func)

    def _callTileHooks(self, v):
        for func in self._tileEventHooks:
            func(v)

    def _callNewTileHooks(self, v):
        for func in self._newTileEventHooks:
            func(v)

    def _callAccelerometerHooks(self, x, y, z):
        for func in self._accelerometerEventHooks:
            func(x, y, z)

    def _handle_events(self, sender, data):
        self._hex("Hex: " + " ".join(hex(n) for n in data))
        # Camera sensor data
        if data[0] == 8:
            # RGB code
            if data[5] == 0x0:
                self._log("Barcode: " + " ".join(hex(n) for n in data))
                self._callTileHooks(hex(data[4]))
            elif data[5] == 0x1:
                self._log("Barcode (New): " + " ".join(hex(n) for n in data))
                self._callNewTileHooks(hex(data[4]))
        # Accelerometer data
        elif data[0] == 7:
            x = int(self._signed(data[4]))
            y = int(self._signed(data[5]))
            z = int(self._signed(data[6]))
            self._log("X: %i Y: %i Z: %i" % (x, y, z))
            self._callAccelerometerHooks(x, y, z)

    async def Run(self):
        self._run = True
        while self._run:
            self._log("Searching for Mario...")
            devices = await BleakScanner.discover()
            for d in devices:
                if d.name.lower().startswith("lego mario"):
                    try:
                        async with BleakClient(d.address) as client:
                            await client.is_connected()
                            self._log("Mario Connected")
                            await client.start_notify(LEGO_CHARACTERISTIC_UUID, self._handle_events)
                            await asyncio.sleep(0.1)
                            await client.write_gatt_char(LEGO_CHARACTERISTIC_UUID, SUBSCRIBE_IMU_COMMAND)
                            await asyncio.sleep(0.1)
                            await client.write_gatt_char(LEGO_CHARACTERISTIC_UUID, SUBSCRIBE_RGB_COMMAND)
                            while await client.is_connected() and self._run:
                                await asyncio.sleep(0.05)
                    except:
                        pass

    def Stop(self):
        self._run = False
