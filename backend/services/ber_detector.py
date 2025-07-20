from typing import List


def get_error_count(sentence_sent: List[int], sentence_received: List[int]):
    counter = 0

    for i in range(len(sentence_sent)):
        if sentence_sent[i] != sentence_received[i]:
            counter += 1

    return counter


def calculate_ber(error_count: int, len_of_sentence_to_code: int):
    # 0 = no errors, 1 = all bits with arrors
    return error_count / len_of_sentence_to_code
