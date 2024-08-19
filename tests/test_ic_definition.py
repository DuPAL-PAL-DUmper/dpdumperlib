"""Tests for IC definitions"""

# pylint: disable=wrong-import-position,wrong-import-order

import sys
sys.path.insert(0, './src') # Make VSCode happy...

from dpdumperlib.ic.ic_types import ICType

def test_27C2001_Definition(ic_definition_27C2001):
    assert ic_definition_27C2001.ic_type == ICType.ROM
    assert ic_definition_27C2001.name == '27C2001'
    
    assert len(ic_definition_27C2001.address) == 18 # 18 address lines in this IC
    assert len(ic_definition_27C2001.data) == 8 # and 8 data lines

    # Test the remapping
    assert ic_definition_27C2001.address == [12, 11, 10, 9, 8, 7, 6, 5, 37, 36, 33, 35, 4, 38, 39, 3, 2, 40]
    assert ic_definition_27C2001.data == [13, 14, 15, 27, 28, 29, 30, 31]
    
    assert len(ic_definition_27C2001.act_l_enable) == 2

    assert ic_definition_27C2001.hw_model == 3
