from backend.utils.generators_utils import handle_n, handle_seed, handle_polynom, generate_polynoms


def lfsr_step(register, poly):

    if type(register) is not list or type(poly) is not list:
        raise TypeError("Register and poly must be lists")

    output = register[-1]
    tapped_bits = []

    for i, value in enumerate(poly):
        if value == 1:
            tapped_bits.append(register[i])

    feedback = tapped_bits[0] ^ tapped_bits[1]
    for bit in tapped_bits[2:]:
        feedback = feedback ^ bit

    state = [feedback] + register[:-1]

    return {"output": output, "state": state}


def generate_lfsr(poly, n=None, seed=None):

    n = handle_n(n=n)
    seed = handle_seed(n=n, seed=seed)["seed"]
    poly = handle_polynom(n=n, poly=poly)["poly"]

    loops = 2 ** n - 2

    step0 = lfsr_step(register=seed, poly=poly)
    register = step0["state"]
    output = [step0["output"]]

    for i in range(loops):
        step = lfsr_step(register=register, poly=poly)
        register = step["state"]
        output.append(step["output"])

    if len(output) != loops + 1:
        raise RuntimeError("There was an error while generating outputs")

    return {"n": n, "output": output,
            "poly": poly, "seed": seed}


def lfsrs_generator(n=None, seed1=None, seed2=None):

    n = handle_n(n=n)
    polynoms = generate_polynoms(n=n)

    poly1 = polynoms["poly1"]
    poly2 = polynoms["poly2"]

    seed1 = handle_seed(n=n, seed=seed1)["seed"]
    seed2 = handle_seed(n=n, seed=seed2)["seed"]

    lfsr1 = generate_lfsr(n=n, seed=seed1, poly=poly1)["output"]
    lfsr2 = generate_lfsr(n=n, seed=seed2, poly=poly2)["output"]

    return {"n": n,
            "poly1": poly1, "poly2": poly2,
            "seed1": seed1, "seed2": seed2,
            "lfsr1": lfsr1, "lfsr2": lfsr2}


def gold_code_generator(lfsr1=None, lfsr2=None):
    if lfsr1 is None or lfsr2 is None:
        lfsrs = lfsrs_generator()

        lfsr1 = lfsrs["lfsr1"]
        lfsr2 = lfsrs["lfsr2"]

    if len(lfsr1) != len(lfsr2):
        raise ValueError("Both LFSR's must be the same length")

    code = []

    for i in range(len(lfsr1)):
        code.append(lfsr1[i] ^ lfsr2[i])

    return code

