"""

draw tree and learn how to find if two int has difference of 1 bit
"""
n= 2


def match_bit(x, y):
    print(x,y)
    z = x ^ y

    count = 0
    if z:
        count += z & 1
        z >>= 1

    return count == 1

def is_bit_valid(i, path):


    if len(path) == 0:
        return True
    elif i in path: return False
    elif len(path) == 2**n - 1:
        if match_bit(path[0], i) and match_bit(path[len(path) - 1], i):
            return True
    else:
        if match_bit(path[len(path) - 1], i):
            return True

    return False

print(is_bit_valid(2, [0,1]))
# print(match_bit(1, 2))