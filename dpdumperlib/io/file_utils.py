"""This file contains functions to aid with common file operations"""

import os
from typing import List

def load_file_data(in_file_path: str, bytes_per_entry: int) -> List[int]:
    data_array: List[int] = []

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
            data_array.append(int.from_bytes(data, byteorder='big', signed=False))

    return data_array