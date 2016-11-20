
try:
    from functools import reduce  # py3
except ImportError as e:
    pass  # py2


def slices(S, n):
    str_list = S.split()

    if n > max((len(w) for w in str_list)) or n <= 0:
        raise ValueError

    def slices_for(w):
        return [
            [int(x) for x in w[i:i+n]]
            for i in range(len(w) - n + 1)
        ]

    res = []
    for w in str_list:
        res.extend(slices_for(w))
    return res
