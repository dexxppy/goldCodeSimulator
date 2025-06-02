from typing import List

from goldCodeSimulator.backend.utils.converting_utils import list_of_bits_to_string, binary_list_to_ascii


def negate_code(code: List[int]) -> List[int]:
    return [1 - bit for bit in code]


def replace_zeros_with_negative_ones(code: List[int]) -> List[int]:
    return [-1 if bit == 0 else 1 for bit in code]


def chunk_string(string, chunk_size):
    chunks = [[int(bit) for bit in string[i:i + chunk_size]] for i in range(0, len(string), chunk_size)]
    return chunks


def get_correlated_bit(n, correlation):
    if abs(correlation + n) >= abs(correlation - n):
        return 1
    else:
        return 0


def bits_list_to_ascii(list: List[int]):
    ascii_list = []
    bits_in_string = list_of_bits_to_string(list=list)
    chunks = chunk_string(string=bits_in_string, chunk_size=8)

    for chunk in chunks:
        ascii_list.append(binary_list_to_ascii(list=chunk))

    return ascii_list
