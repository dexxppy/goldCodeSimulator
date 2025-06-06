import re

def validate_seed(n, seed):
    if len(seed) != n:
        return False

    for bit in seed:
        if int(bit) not in [0, 1]:
            return False
    return True

def validate_form_input(sent_to_transmit, error_rate_id, runs, n, seed1, seed2):
    if not sent_to_transmit or not error_rate_id or not runs:
        raise ValueError("Input to trasmit, error rate id and runs cannot be empty")

    if not bool(re.fullmatch(r'[a-zA-Z0-9]+', sent_to_transmit)):
        raise ValueError("Sentence to transmit must contain only letters and numbers")

    try:
        runs_int = int(runs)
        if runs_int < 1:
            raise ValueError("Run times must be greater than 1.")
    except (ValueError, TypeError):
        raise ValueError("Run times must be an integer")

    if not n:
        if seed1:
            n = len(seed1)
        else:
            n = None
    else:
        if int(n) not in [5, 6, 7, 9, 10, 11]:
            raise ValueError("Degree n must be in [5, 6, 7, 9, 10, 11]")

    if not seed1:
        seed1 = None
    else:
        if not validate_seed(n, seed1):
            raise ValueError("Seed must be of n degree length and consist only of binary values")

    if not seed2:
        seed2 = None
    else:
        if not validate_seed(n, seed1):
            raise ValueError("Seed must be of n degree length and consist only of binary values")

    return {"input_sent": sent_to_transmit, "error_rate_id": int(error_rate_id), "runs": int(runs),
            "n": n, "seed1": seed1, "seed2": seed2}