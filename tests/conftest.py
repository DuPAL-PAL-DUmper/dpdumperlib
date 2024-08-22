"""Fixtures for testing"""

# pylint: disable=wrong-import-position

import sys
sys.path.insert(1, '.') # Make VSCode happy...

import pytest

from dpdumperlib.ic.ic_definition import ICDefinition
from dpdumperlib.ic.ic_loader import ICLoader

@pytest.fixture
def ic_definition_27C2001() -> ICDefinition:
    return ICLoader.extract_definition_from_file('examples/27C2001.toml')

@pytest.fixture
def ic_definition_PAL12x6() -> ICDefinition:
    return ICLoader.extract_definition_from_file('examples/PAL12x6.toml')

@pytest.fixture
def filename_randomdata_1k() -> str:
    return 'tests/data/random_1K.bin'

@pytest.fixture
def filename_randomdata_1_5k() -> str:
    return 'tests/data/random_1.5K.bin'