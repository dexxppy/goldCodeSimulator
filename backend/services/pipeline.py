import numpy as np

from typing import List
from goldCodeSimulator.backend.services.ber_detector import calculate_ber, get_error_count
from goldCodeSimulator.backend.utils.converting_utils import list_of_bits_to_string, binary_poly_to_superscript
from goldCodeSimulator.backend.services.gold_generator import lfsrs_generator, gold_code_generator
from goldCodeSimulator.backend.services.Coder import Coder
from goldCodeSimulator.backend.services.error_generator import get_error_rate_data, simulate_errors, generate_error_rate

simulation_coder = Coder()


def run_transmission_simulation(coded_sentence: List[int], error_rate_lower_limit: int, error_rate_upper_limit: int):
    error_rate = generate_error_rate(error_rate_lower_limit, error_rate_upper_limit)

    noisy_data = simulate_errors(coded_sentence=coded_sentence, error_rate=error_rate)
    noisy_data_in_list = noisy_data["noisy_data_in_list"]
    noisy_data_in_str = noisy_data["noisy_data_in_str"]

    decode_data = simulation_coder.decode(noisy_data_in_str)
    decoded_sentence_in_ascii = decode_data["result_in_ascii"]
    decoded_sentence_in_bit_list = decode_data["result_in_bit_list"]
    decoded_sentence_in_bit_str = decode_data["result_in_bit_str"]

    return {
        "noisy_data_in_str": noisy_data_in_str, "noisy_data_in_list": noisy_data_in_list,
        "decoded_sentence_in_ascii": decoded_sentence_in_ascii,
        "decoded_sentence_in_list": decoded_sentence_in_bit_list,
        "decoded_sentence_in_bit_str": decoded_sentence_in_bit_str
    }


def run_full_simulation(runs: int, sent_to_transmit: str, error_rate_id: int, n=None, seed1=None, seed2=None):
    generated_values = lfsrs_generator(n=n, seed1=seed1, seed2=seed2)

    n = generated_values["n"]
    poly1 = generated_values["poly1"]
    poly1_str = binary_poly_to_superscript(poly1)
    poly2 = generated_values["poly2"]
    poly2_str = binary_poly_to_superscript(poly2)
    seed1 = generated_values["seed1"]
    seed1_str = list_of_bits_to_string(seed1)
    seed2 = generated_values["seed2"]
    seed2_str = list_of_bits_to_string(seed2)
    lfsr1 = generated_values["lfsr1"]
    lfsr1_str = list_of_bits_to_string(lfsr1)
    lfsr2 = generated_values["lfsr2"]
    lfsr2_str = list_of_bits_to_string(lfsr2)

    gold_code = gold_code_generator(lfsr1=lfsr1, lfsr2=lfsr2)
    gold_code_str = list_of_bits_to_string(gold_code)
    simulation_coder.gold_code = gold_code

    code_data = simulation_coder.code(sentence_to_code=sent_to_transmit)
    binary_sentence_to_transmit = code_data["sentence_in_bit_list"]
    coded_sentence_in_str = code_data["result_in_str"]
    coded_sentence_in_list = code_data["result_in_list"]

    error_rate_data = get_error_rate_data(error_id=error_rate_id)
    error_rate_name = error_rate_data["rate_name"]
    error_rate_lower_limit = error_rate_data["lower_limit"]
    error_rate_upper_limit = error_rate_data["upper_limit"]

    transmission_data = []
    error_sum = 0

    for i in range(runs):
        transmite = run_transmission_simulation(coded_sentence=coded_sentence_in_list,
                                                error_rate_lower_limit=error_rate_lower_limit,
                                                error_rate_upper_limit=error_rate_upper_limit)

        error_sum += get_error_count(sentence_sent=binary_sentence_to_transmit,
                                     sentence_received=transmite["decoded_sentence_in_list"])
        transmission_data.append(transmite)

    ber_rate = calculate_ber(error_sum, len(binary_sentence_to_transmit) * runs)
    ber_percentage = np.round(ber_rate, 4) * 100

    return {"runs": runs, "sentence_to_transmit": sent_to_transmit,
            "n": str(n), "poly1": poly1_str, "poly2": poly2_str, "seed1": seed1_str, "seed2": seed2_str,
            "lfsr1": lfsr1_str, "lfsr2": lfsr2_str, "gold_code": gold_code_str,
            "coded_sentence": coded_sentence_in_str, "coded_sentence_len": len(coded_sentence_in_str),
            "transmission_data": transmission_data, "error_rate_name": error_rate_name,
            "ber_rate": ber_rate, "ber_percentage": ber_percentage
            }
