import sys


def get_sequence_item(k):
    result = 0

    for i in range(1, k+1):
        shift = 1 << (i - 1)
        mask = (1 << shift) - 1
        negation = result ^ mask
        result = (result << shift) ^ negation

    return result


