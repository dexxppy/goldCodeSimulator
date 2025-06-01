import json
import os
import random
from typing import List
from backend.utils.coder_utils import list_of_bits_to_string

def generate_error_rate(lower_limit, upper_limit):
    rate = random.randint(a=int(lower_limit), b=int(upper_limit))
    return rate

def get_error_rate_data(error_id: int):
    json_path = os.path.join(os.path.dirname(__file__), "..", "..", "static", "data", "error_rates.json")
    json_path = os.path.abspath(json_path)

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            all_rates = json.load(f)["error_rates"]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {json_path}")
    except json.JSONDecodeError:
        raise ValueError(f"File {json_path} contains invalid JSON")
    except IOError as e:
        raise IOError(f"Error occurred while reading from {json_path}: {e}")

    rate_data = next((entry for entry in all_rates if entry["id"] == error_id), None)

    return {"rate_id": rate_data["id"], "rate_name": rate_data["name"],
            "lower_limit": rate_data["lower_limit"], "upper_limit": rate_data["upper_limit"]}


def simulate_errors(coded_sentence: List[int], error_rate=None, error_rate_id=None):
    if error_rate is None:
        if error_rate_id is None:
            error_rate_id = random.randint(a=0, b=5)
        error_rate = get_error_rate_data(error_id=error_rate_id)["rate"]

    coded_sent_len = len(coded_sentence)
    error_count = int((error_rate/100)*coded_sent_len)
    indices = random.sample(range(coded_sent_len), error_count)
    noisy_data = []

    for i, bit in enumerate(coded_sentence):
        if i in indices:
            bit = 1 - bit

        noisy_data.append(bit)

    noisy_data_in_str = list_of_bits_to_string(noisy_data)
    return {"noisy_data_in_list": noisy_data, "noisy_data_in_str": noisy_data_in_str}