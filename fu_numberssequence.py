"""
Module to work with sequence of number by rules
"""


def number_sequence(length):
    """
    int -> list
    Create and return sequence list of number with stated length where every object in sequence
    is got by formula A(n) = k XOR k**3 where k is the lowest number with that type that (2n-1)*k
    is is palindromic in base 2
    Expectation:
    length is integel bigger than -1
    >>> number_sequence(1)

    >>> number_sequence(1)

    """
    sequence = []
    for current_number in range(length):
        k_current = 0
        while True:
            if is_palindrom((current_number*2-1)*k_current):
                break
            k_current += 1
        digit_to_add = k_current ^ k_current**3
        sequence.append(digit_to_add)
    return sequence

def is_palindrom(number):
    """
    Check if number in base 2 is palindrom
    Return True if yes, False if not
    """
    bit_len = number.bit_length()
    for cur_pos in range(bit_len//2+1):
        last_bit = (number >> cur_pos) & 1
        first_bit =  (number >> (bit_len - cur_pos - 1)) & 1
        if last_bit != first_bit:
            return False
    return True
