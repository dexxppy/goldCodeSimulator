from typing import List
from goldCodeSimulator.backend.utils.coder_utils import (negate_code,
                                       replace_zeros_with_negative_ones,
                                       chunk_string,
                                       list_of_bits_to_string,
                                       get_correlated_bit,
                                       bits_list_to_ascii
                                       )
from goldCodeSimulator.backend.utils.converting_utils import ascii_to_binary_list, string_to_ascii_list, flatten_chunks


class Coder:

    def __init__(self, gold_code=None):
        self._gold_code = None
        self.n = 0
        self.negated_gold_code = None

        if gold_code is not None:
            self.gold_code = gold_code  # tu wywołujemy setter

    @property
    def gold_code(self):
        return self._gold_code

    @gold_code.setter
    def gold_code(self, value):
        if any(bit not in (0, 1) for bit in value):
            raise ValueError("Gold's code must contain only binary values")
        self._gold_code = value
        self.n = len(value)
        self.negated_gold_code = negate_code(code=value)

    def code(self, sentence_to_code: str):
        result = []
        bits_table = ascii_to_binary_list(chars=string_to_ascii_list(string=sentence_to_code))
        sentence_in_bit_list = flatten_chunks(bits_table)

        for bits_sequence in bits_table:
            bits_sequence = [int(bit) for bit in bits_sequence]

            for bit in bits_sequence:
                if bit == 1:
                    result.append(self.gold_code)
                elif bit == 0:
                    result.append(self.negated_gold_code)
                else:
                    raise ValueError("An error occurred while decoding sentence")

        flat = [bit for group in result for bit in group]
        result_in_string = list_of_bits_to_string(list=flat)

        return {"result_in_list": flat, "result_in_str": result_in_string, "sentence_in_bit_list": sentence_in_bit_list}

    def decode(self, sentence_to_decode: str):
        sentence_to_decode_chunked = chunk_string(string=sentence_to_decode, chunk_size=len(self.gold_code))

        decoded_bits = []

        for block in sentence_to_decode_chunked:
            correlation = self.calculate_correlation(data_fragment=block)
            correlated_bit = get_correlated_bit(n=self.n, correlation=correlation)
            decoded_bits.append(correlated_bit)

        decoded_sentence = bits_list_to_ascii(decoded_bits)
        decoded_bits_in_string = ''.join(str(char) for char in decoded_bits)
        result_in_string = ''.join(str(char) for char in decoded_sentence)

        return {"result_in_bit_list": decoded_bits, "result_in_bit_str": decoded_bits_in_string,
                "result_in_ascii": result_in_string}

    def calculate_correlation(self, data_fragment: List[int]):
        if len(data_fragment) != self.n:
            raise ValueError("Data fragment must be same length as the code")

        correlation = 0
        refactored_golds_code = replace_zeros_with_negative_ones(code=self.gold_code)
        refactored_data_fragment = replace_zeros_with_negative_ones(code=data_fragment)

        for i in range(0, len(refactored_golds_code)):
            correlation += refactored_golds_code[i] * refactored_data_fragment[i]

        return correlation
