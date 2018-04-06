def sign(x):
    if x > 0:
        return 1.
    elif x < 0:
        return -1.
    elif x == 0:
        return 0.
    else:
        return x


def symbolic_sign(x):
    if x >= 0:
        return '+'
    elif x < 0:
        return '-'
    else:
        return x
