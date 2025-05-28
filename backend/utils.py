import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(BASE_DIR, 'static', 'data', 'polynom_pairs.json')


# returns dictionary in form {'n': X, 'first': 'XXXXX', 'second': 'XXXXX'}
def get_polynoms(n=random.randint(5, 15)):
    with open(json_path, 'r', encoding='utf-8') as f:
        pairs = json.load(f)["polynom_pairs"]

    random_pair = next((pair for pair in pairs if pair["n"] == n), None)
    return random_pair


# returns seed of n length in string
def generate_seed(n):
    if not 5 <= n <= 15:
        return -1

    seed = "1"

    for i in range(1, n):
        bit = random.randint(0, 1)
        seed += str(bit)

    return seed


def string_to_list(string):
    return list(string)


def is_seed_valid(n, seed):
    seed_list = string_to_list(seed)

    if len(seed_list) != n or seed_list[0] == "0":
        return False

    return True
