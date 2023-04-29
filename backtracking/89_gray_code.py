"""

draw tree and learn how to find if two int has difference of 1 bit
"""
n = 2


def match_bit(x, y):
    print(x, y)
    z = x ^ y  # XOR operator: if bits match then 0 if bits don't match its 1

    count = 0
    if z:
        count += z & 1  # logical & : meaning if last bit of z is 1 then 1 else 0
        z >>= 1  # >> shift 1 bit to right which also means divide by 2

    return count == 1


def is_bit_valid(i, path):
    if len(path) == 0:
        return True
    elif i in path:
        return False
    elif len(path) == 2 ** n - 1:
        if match_bit(path[0], i) and match_bit(path[len(path) - 1], i):
            return True
    else:
        if match_bit(path[len(path) - 1], i):
            return True

    return False


print(is_bit_valid(2, [0, 1]))
# print(match_bit(1, 2))
