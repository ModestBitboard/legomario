"""
Package for connecting and receiving inputs from Lego Mario or Luigi.
The original script was written by Bruno Hautzenberger and you can
find it here: https://github.com/salendron/pyLegoMario.git
"""

import os
from .mario import *

# fmt: off
__project__ = 'legomario'
__version__ = '0.2.0'
# fmt: on

VERSION = __project__ + "-" + __version__

script_dir = os.path.dirname(__file__)
