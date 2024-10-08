"""Tests for file utils"""

# pylint: disable=wrong-import-position,wrong-import-order

import sys
from typing import List
sys.path.insert(0, './src') # Make VSCode happy...

import pytest

import dpdumperlib.io.file_utils as FileUtils

def test_loading_1K(filename_randomdata_1k):
    data_1B: List[int] = FileUtils.load_file_data(filename_randomdata_1k, 1)
    assert(len(data_1B) == 1024)
    
    data_2B: List[int] = FileUtils.load_file_data(filename_randomdata_1k, 2)
    assert(len(data_2B) == 512)

    data_4B: List[int] = FileUtils.load_file_data(filename_randomdata_1k, 4)
    assert(len(data_4B) == 256)

    data_8B: List[int] = FileUtils.load_file_data(filename_randomdata_1k, 8)
    assert(len(data_8B) == 128)
    assert(data_8B[0].to_bytes(length=8, byteorder='big', signed=False) == b'\xB2\x20\xA5\x60\x35\x3B\x63\x6D')
    
    data_8BLE: List[int] = FileUtils.load_file_data(filename_randomdata_1k, 8, reverse_byte_order=True)
    assert(len(data_8BLE) == 128)
    assert(data_8BLE[0].to_bytes(length=8, byteorder='little', signed=False) == b'\xB2\x20\xA5\x60\x35\x3B\x63\x6D')

    # Size of file is not divisible by 3
    with pytest.raises(Exception):
       FileUtils.load_file_data(filename_randomdata_1k, 3)

def test_loading_1_5K(filename_randomdata_1_5k):
    data_1_5B: List[int] = FileUtils.load_file_data(filename_randomdata_1_5k, 3)
    assert(len(data_1_5B) == 512)
