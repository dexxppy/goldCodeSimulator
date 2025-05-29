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
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(BASE_DIR, 'static', 'data', 'polynom_pairs.json')

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
    """
        Validate n if given or get random n if empty

        Args:
            n (int, optional): value n to be handled

        Returns:
            n (int): validated or generated n
    """

    if n is None:
        n = random.choice([i for i in range(5, 11) if i not in [8]])

    if type(n) is not int:
        return TypeError("Value n must be an integer")

    if n not in [5, 6, 7, 9, 10, 11]:
        return ValueError("Value n must be in [5,6,7,9,10,11]")

    return n


def handle_seed(n=None, seed=None):
    """
        Validate seed if given or generate random seed

           Args:
               n (int, optional): highest power of polynom, must be 5 <= n <= 11 (exc 8), empty or None for random value
               seed (string, optional): seed to validate, must be given along with n

           Returns:
               dict: {
                - n (int): generated/validated highest power of poly, length of seed
                - seed (list of ints): generated/validated seed in a list of bits
            }

            Raises:
                AttributeError: if provided only seed without n
                ValueError: if seed is invalid
       """

    if seed is not None:
        if n is None:
            raise AttributeError("Seed cannot be validated without provided n")

    n = handle_n(n)

    if seed is None:
        seed = "1"
        for i in range(1, n):
            bit = random.randint(0, 1)
            seed += str(bit)

    if type(seed) is not list:
        seed = [int(bit) for bit in seed]

    if len(seed) != n:
        raise ValueError("Seed must be of n length")

    if seed[0] == 0:
        raise ValueError("Seed must start with 1")

    if 1 not in seed[1:]:
        raise ValueError("Seed cannot be zero")

    return {"seed": seed, "n": n}


def handle_polynom(n=None, poly=None):
    """
        Generate new or validate and format given polynomial

        Args:
            n (int, optional):  highest power of polynom, empty for random value
            poly (string, optional): polynomial to validate, must be of n+1 length, empty for random

        Returns:
            dict: {
            - n (int): LFSR single step output
            - poly1 (list of ints): polynomial in binary form (ex. "101" for x^2+1)
        }

        Raises:
            AttributeError if provided polys without n
            ValueError if provided polynomials are not the same length

      """

    if poly is not None:
        if n is None:
            raise AttributeError("Polynomials cannot be validated without provided n")

    n = handle_n(n)

    if poly is None:
        all_pairs = get_all_polynoms()
        all_matching_pairs = [pair for pair in all_pairs if pair["n"] == n]
        poly = all_matching_pairs[random.randint(0, len(all_matching_pairs) - 1)]["poly1"]
    else:
        if type(poly) is str:
            poly = [int(bit) for bit in poly]

    return {"n": n, "poly": poly}


def handle_multiple_polynoms(n=None, polys=None):
    """
        Generate new or validate and format given polynomials

        Args:
            n (int, optional):  highest power of polynom, empty for random value
            polys (dict: {
                - poly1 : first polynom to validate with second
                - poly2:  second polynom to validate with first
                })

        Returns:
           dict: {
            - n (int): LFSR single step output
            - poly1, poly2 (list of ints): polynomial in binary form (ex. "101" for x^2+1)
        }

        Raises:
            AttributeError if provided polys without n
            ValueError if provided polynomials are not the same length

    """
    if polys is not None:
        if n is None:
            raise AttributeError("Polynomials cannot be validated without provided n")
        if len(polys) < 2:
            raise ValueError("Given list of polynomials must contain at least 2 polynomials")

    n = handle_n(n)
    all_pairs = get_all_polynoms()
    print(polys)
    if polys is None or (polys["poly1"] is None and polys["poly2"] is None):
        all_matching_pairs = [pair for pair in all_pairs if pair["n"] == n]
        pair = all_matching_pairs[random.randint(0, len(all_matching_pairs) - 1)]
    else:
        poly1 = polys["poly1"]
        poly2 = polys["poly2"]

        if len(poly1) != len(poly2):
            raise ValueError("Given polynomials must be the same length")

        if type(poly1) is list:
            poly1 = ''.join(str(x) for x in poly1)

        if type(poly2) is list:
            poly2 = ''.join(str(x) for x in poly2)

        n = len(poly1) - 1
        pair = {"n": n, "poly1": poly1, "poly2": poly2}

    pair["poly1"] = [int(bit) for bit in pair["poly1"]]
    pair["poly2"] = [int(bit) for bit in pair["poly2"]]

    return pair
