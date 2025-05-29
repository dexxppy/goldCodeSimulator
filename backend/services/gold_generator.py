from .. import utils


def lfsr_step(register, poly):

    """
        Calculate single step of LFSR calculation

        Args:
            register (list[int]):  register to calculate feedback and single output from
            poly (list[int]): polynomial to calculate feedback from

        Returns:
            dict: {
            - output (int): LFSR single step output
            - state (list of ints): LFSR state after iteration
            }

        Raises:
            TypeError: If provided register or polynomial is invalid
    """

    if type(register) is not list or type(poly) is not list:
        raise TypeError("Register and poly must be lists")

    output = register[-1]
    tapped_bits = []

    for i, value in enumerate(poly[1:]):
        if value == 1:
            tapped_bits.append(register[i])

    tapped_bits.append(1)

    feedback = tapped_bits[0] ^ tapped_bits[1]
    for bit in tapped_bits[2:]:
        feedback = feedback ^ bit

    state = [feedback] + register[:-1]

    return {"output": output, "state": state}


def generate_lfsr(n=None, seed=None, poly=None):

    """
        Calculate single step of LFSR calculation

        Args:
            n (int, optional):  highest power of polynomial
            seed (list of ints): initial value of LFSR state
            poly (list of ints): polynomial to calculate output from

        Returns:
            output (string): LFSR output value

        Raises:
            RuntimeError: If output is not of required length
    """
    n = utils.handle_n(n)
    seed = utils.handle_seed(n, seed)["seed"]
    poly = utils.handle_polynom(n, poly)["poly"]

    loops = 2 ** n - 2

    step0 = lfsr_step(seed, poly)
    register = step0["state"]
    output = [step0["output"]]

    for i in range(loops):
        step = lfsr_step(register, poly)
        register = step["state"]
        output.append(step["output"])

    if len(output) != loops + 1:
        raise RuntimeError("There was an error while generating outputs")

    return {"n": n, "output": output,
            "poly": poly, "seed": seed}


def lfsr_generator(n=None, seed1=None, seed2=None, poly1=None, poly2=None):

    """
        Generate two LFSR's for Gold's code

        Args:
            n (int, optional): highest power of polynomial and length of seed, in range <5, 15>
            seed1 (list[int], optional): initial value of first LFSR, empty for random
            seed2 (list[int], optional): initial value of first LFSR, empty for random

        Returns:
            dict: {
            - output (string): LFSR single step output
            - state (list of ints): LFSR state after iteration
            }

        Raises:
            TypeError: If provided register or polynomial is invalid
    """
    n = utils.handle_n(n)
    polynoms = utils.handle_multiple_polynoms(n, {"poly1": poly1, "poly2": poly2})

    poly1 = polynoms["poly1"]
    poly2 = polynoms["poly2"]

    seed1 = utils.handle_seed(n, seed1)["seed"]
    seed2 = utils.handle_seed(n, seed2)["seed"]

    print("poly1")
    print(poly1)

    print("poly2")
    print(poly2)

    print("seed1")
    print(seed1)

    print("seed2")
    print(seed2)

    lfsr1 = generate_lfsr(n, seed1, poly1)
    lfsr2 = generate_lfsr(n, seed2, poly2)

    return {"n": n,
            "poly1": poly1, "poly2": poly2,
            "seed1": seed1, "seed2": seed2,
            "lfsr1": lfsr1, "lfsr2": lfsr2}

