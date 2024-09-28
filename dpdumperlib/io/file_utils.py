"""This file contains functions to aid with common file operations"""

import os
from typing import List, Literal

def load_file_data(in_file_path: str, bytes_per_entry: int, reverse_byte_order: bool = False) -> List[int]:
    data_array: List[int] = []
    endianness: Literal['big', 'little'] = 'little' if reverse_byte_order else 'big' 

    with open(in_file_path, "rb") as f:
        # Read the file size
        f.seek(0, os.SEEK_END)
        file_size: int = f.tell()
        f.seek(0, os.SEEK_SET)

        if file_size % bytes_per_entry:
            raise ValueError(f'File has a size ({file_size}) not divisible by {bytes_per_entry}')

        # Push data in an array
        data: bytes
        while (data := f.read(bytes_per_entry)):
            data_array.append(int.from_bytes(data, byteorder=endianness, signed=False))

    return data_array