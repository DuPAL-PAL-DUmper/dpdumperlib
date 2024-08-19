"""This file contains the enum with supported IC types"""

from enum import Enum

class ICType(Enum):
    """
    Enum for IC Types supported by the library
    """

    ROM = 'ROM' # ICs assimilable to Read Only Memories
    SRAM = 'SRAM' # ICs assimilable to static memories
