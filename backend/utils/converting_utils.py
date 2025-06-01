from typing import List


def binary_poly_to_superscript(poly: List[int]) -> str:
    superscript_digits = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }

    def to_superscript(n: int) -> str:
        return ''.join(superscript_digits[d] for d in str(n))

    terms = []
    degree = len(poly) - 1

    for i, bit in enumerate(poly):
        if bit == 1:
            power = degree - i
            if power == 0:
                terms.append("1")
            elif power == 1:
                terms.append("x")
            else:
                terms.append(f"x{to_superscript(power)}")

    return " + ".join(terms)


def string_of_bits_to_list(string: str):
    return [int(bit) for bit in string]


def list_of_bits_to_string(list: List[int]):
    return ''.join(str(bit) for bit in list)


def string_to_ascii_list(string: str) -> List[int]:
    ascii_list = [ord(char) for char in string]
    return ascii_list


def ascii_to_binary_list(chars: List[int]) -> list[str]:
    binary_codes = [format(code, '08b') for code in chars]
    return binary_codes


def binary_list_to_ascii(list: List[int]):
    bits_str = list_of_bits_to_string(list=list)
    dec = int(bits_str, 2)

    return chr(dec)

def flatten_chunks(chunked_list: list[str]):
    return [int(bit) for binary in chunked_list for bit in binary]