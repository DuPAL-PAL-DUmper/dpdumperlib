"""This class contains code to extract an IC definition from a properly formatted TOML file"""

from typing import Any, final

import tomllib

from dpdumperlib.ic.ic_definition import ICDefinition
from dpdumperlib.ic.ic_types import ICType


@final
class ICLoader:
    """
    Class with utility code to load TOML IC definitions
    """

    _KEY_NAME: str = 'name'
    _KEY_TYPE: str = 'type'
    _KEY_PINOUT: str = 'pinout'
    _KEY_PINOUT_ZIFMAP:str = 'ZIF_map'
    _KEY_PINOUT_ADDRESS:str = 'address'
    _KEY_PINOUT_DATA:str = 'data'
    _KEY_PINOUT_H_ENABLE: str = 'H_enable'
    _KEY_PINOUT_L_ENABLE: str = 'L_enable'
    _KEY_PINOUT_H_WRITE: str = 'H_write'
    _KEY_PINOUT_L_WRITE: str = 'L_write'
    _KEY_ADAPTER: str = 'adapter'
    _KEY_ADAPTER_HI_PINS: str = 'hi_pins'
    _KEY_ADAPTER_NOTES: str = 'notes'
    _KEY_REQUIREMENTS: str = 'requirements'
    _KEY_REQUIREMENTS_HARDWARE: str = 'hardware'

    @classmethod
    def extract_definition_from_file(cls, filepath: str) -> ICDefinition:
        """Reads a TOML file with a definition and generates an ICDefinition from it

        Args:
            filepath (str): Path to the IC definition TOML file

        Returns:
            ICDefinition: IC definition generated from the TOML file
        """

        with open(filepath, "rb") as f:
            toml_data: dict[str, Any] = tomllib.load(f)

            ic_type: ICType = ICType(toml_data[cls._KEY_TYPE])
            return ICDefinition(name=toml_data[cls._KEY_NAME],
                                ic_type=ic_type,
                                zif_map=toml_data[cls._KEY_PINOUT][cls._KEY_PINOUT_ZIFMAP],
                                address=toml_data[cls._KEY_PINOUT][cls._KEY_PINOUT_ADDRESS],
                                data=toml_data[cls._KEY_PINOUT][cls._KEY_PINOUT_DATA],
                                act_h_enable=toml_data[cls._KEY_PINOUT][cls._KEY_PINOUT_H_ENABLE],
                                act_l_enable=toml_data[cls._KEY_PINOUT][cls._KEY_PINOUT_L_ENABLE],
                                act_h_write=toml_data[cls._KEY_PINOUT][cls._KEY_PINOUT_H_WRITE],
                                act_l_write=toml_data[cls._KEY_PINOUT][cls._KEY_PINOUT_L_WRITE],
                                adapter_hi_pins=toml_data[cls._KEY_ADAPTER][cls._KEY_ADAPTER_HI_PINS],
                                hw_model=toml_data[cls._KEY_REQUIREMENTS][cls._KEY_REQUIREMENTS_HARDWARE],
                                adapter_notes=toml_data[cls._KEY_ADAPTER].get(cls._KEY_ADAPTER_NOTES, None))

