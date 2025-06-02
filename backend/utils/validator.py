def validate_form_input(sent_to_transmit, error_rate_id, runs, n, seed1, seed2):
    if not sent_to_transmit or not error_rate_id or not runs:
        raise ValueError("Input to trasmit, error rate id and runs cannot be empty")

    if not n:
        n = None

    if not seed1:
        seed1 = None

    if not seed2:
        seed2 = None

    return {"input_sent": sent_to_transmit, "error_rate_id": int(error_rate_id), "runs": int(runs),
            "n": n, "seed1": seed1, "seed2": seed2}