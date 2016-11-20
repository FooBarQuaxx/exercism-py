
try:
    from functools import reduce  # py3
except ImportError as e:
    pass  # py2


def slices(S, n):

    S_len = len(S)
    if n > S_len or n <= 0:
        raise ValueError

    return [
        [int(x) for x in S[i:i+n]]
        for i in range(S_len - n + 1)
    ]
