import json
import os
import random


def get_all_polynoms():
    """
        Get all polynom pairs from JSON file

        Returns:
            dict: {
                - n (int): highest power of poly
                - poly1, poly2 (string): polynomial in binary form (ex. "101" for x^2+1)
            }

        Raises:
            Error: If problems occurred while reading from file
    """
    json_path = os.path.join(os.path.dirname(__file__), "..", "..", "static", "data", "polynom_pairs.json")
    json_path = os.path.abspath(json_path)

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            pairs = json.load(f)["polynom_pairs"]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {json_path}")
    except json.JSONDecodeError:
        raise ValueError(f"File {json_path} contains invalid JSON")
    except IOError as e:
        raise IOError(f"Error occurred while reading from {json_path}: {e}")

    return pairs


def handle_n(n=None):
    if n is None:
        n = random.choice([i for i in range(5, 11) if i not in [8]])

    if type(n) is not int:
        n = int(n)

    if n not in [5, 6, 7, 9, 10, 11]:
        raise TypeError("Value n must be a value from [5,6,7,9,10,11]")

    return n


def handle_seed(n=None, seed=None):
    if seed is not None:
        if n is None:
            raise AttributeError("Seed cannot be validated without provided n")

    n = handle_n(n=n)

    if seed is None:
        seed = "1"
        for i in range(1, n):
            bit = random.randint(0, 1)
            seed += str(bit)

    if type(seed) is not list:
        seed = [int(bit) for bit in seed]

    for bit in seed:
        if bit not in [0, 1]:
            raise ValueError("Seed must be in binary form")

    if len(seed) != n:
        raise ValueError("Seed must be of n length")

    if 1 not in seed:
        raise ValueError("Seed cannot be zero")

    return {"seed": seed, "n": n}


def handle_polynom(n, poly):
    if poly is not None:
        if n is None:
            raise AttributeError("Polynomials cannot be validated without provided n")

    n = handle_n(n=n)

    if type(poly) is not list:
        poly = [int(bit) for bit in poly]

    for bit in poly:
        if int(bit) not in [0, 1]:
            raise ValueError("Polynomial must be in binary form")

    if len(poly) == n + 1:
        poly.pop(-1)
    elif len(poly) != n:
        raise ValueError("Polynomial is of inproper length")

    return {"n": n, "poly": poly}


def generate_polynoms(n=None):
    """
        returns: dict{
                - n (int)
                - poly1 (list of ints)
                - poly2 (list of ints)
        }

    """

    n = handle_n(n=n)
    all_pairs = get_all_polynoms()

    all_matching_pairs = [pair for pair in all_pairs if pair["n"] == n]
    pair_index = random.randint(0, len(all_matching_pairs) - 1)
    pair = all_matching_pairs[pair_index]

    poly1 = handle_polynom(n=n, poly=pair["poly1"])["poly"]
    poly2 = handle_polynom(n=n, poly=pair["poly2"])["poly"]

    pair["poly1"] = poly1
    pair["poly2"] = poly2

    return pair



# def handle_multiple_polynoms(n=None, polys=None):
#     if polys is not None:
#         if n is None:
#             raise AttributeError("Polynomials cannot be validated without provided n")
#         if len(polys) < 2:
#             raise ValueError("Given list of polynomials must contain at least 2 polynomials")
#
#     n = handle_n(n)
#     all_pairs = get_all_polynoms()
#
#     if polys is None or (polys["poly1"] is None and polys["poly2"] is None):
#         all_matching_pairs = [pair for pair in all_pairs if pair["n"] == n]
#         pair = all_matching_pairs[random.randint(0, len(all_matching_pairs) - 1)]
#
#         poly1 = handle_polynom(n, pair["poly1"])["poly"]
#         poly2 = handle_polynom(n, pair["poly2"])["poly"]
#
#         pair["poly1"] = poly1
#         pair["poly2"] = poly2
#     else:
#         poly1 = polys["poly1"]
#         poly2 = polys["poly2"]
#
#         if len(poly1) != len(poly2) != n + 1:
#             raise ValueError("Given polynomials must be the same, n+1 length")
#
#         if type(poly1) is not list:
#             poly1 = [int(bit) for bit in poly1]
#
#         if type(poly2) is not list:
#             poly2 = [int(bit) for bit in poly2]
#
#         n = len(poly1) - 1
#
#         if poly1[0] != poly2[0] != 1:
#             raise ValueError("Polynomials must start with 1")
#
#         counters_of_1 = {"poly1": 0, "poly2": 0}
#         for i in range(1, n):
#             if poly1[i] not in [0, 1] or poly2[i] not in [0, 1]:
#                 raise ValueError("Polynomials must be in binary form")
#
#             if poly1[i] == 1:
#                 counters_of_1["poly1"] += 1
#
#             if poly2[i] == 1:
#                 counters_of_1["poly2"] += 1
#
#         if counters_of_1["poly1"] == 0 or counters_of_1["poly2"] == 0:
#             raise ValueError("Polynomial must consist of at least two powers")
#
#         pair = {"n": n, "poly1": poly1, "poly2": poly2}
#
#     return pair
