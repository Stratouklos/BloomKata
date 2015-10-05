__author__ = 'exak'


def scale_down(array_of_hex_digits, max_size):
    digits = check_size_and_get_digits(max_size)
    if type(array_of_hex_digits) is None:
        raise TypeError("Expected hexstring found None")
    if len(array_of_hex_digits) is 0:
        raise ValueError("The minimum hexstring length is 1")
    index = int(array_of_hex_digits[0:digits], 16)
    if index > max_size:
        return index - max_size
    else:
        return index


def check_size_and_get_digits(size):
    digits = len(hex(size)) - 2
    if digits <= 2:
        raise ValueError("The minimum indexing size is 256")
    if digits > 64:
        raise ValueError("Maximum indexing size exceeded")
    return digits
