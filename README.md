# legomario
A Python3 package for receiving inputs from a Lego Mario/Luigi figure
The code is a slight modification of the script written by Bruno Hautzenberger that can be found here (https://github.com/salendron/pyLegoMario.git)

# How to install
to install you will want to type this command into your terminal or command prompt:
`pip install legomario`

# How to use
in your script you will want to start off by importing the modules needed like so:

`from legomario import Mario`

`import asyncio`

and then you will want to create your "hooks". Hooks are functions that are called every time the data they are using gets updated

`def tile_hook(data):`

`print(f"Barcode: {data}")`

the next step is to set up lego mario and add the tile hook like so:

`mario = Mario()`

`mario.AddTileHook(tile_hook)`

and lets add a little message to make it look nice:

`print("Turn on Mario and press the Bluetooth button")`

now to connect lego mario:

`loop = asyncio.get_event_loop()`

`loop.run_until_complete(mario.Run())`

The finished code should look like this:
[example1.py](https://github.com/ShadowFire5650/legomario/blob/main/legomario/example1.py)

# More useful info
I did want to point out that I have no intention of taking credit for the amazing work of Bruno Hautzenberger I just made this because I wanted to dip into 
this kind of coding and just help by patching small holes in the code that make it a bit nicer...
For info on Lego Mario tile data visit https://github.com/bricklife/LEGO-Mario-Reveng
For the Bruno Hautzenberger's original script visit https://github.com/salendron/pyLegoMario
