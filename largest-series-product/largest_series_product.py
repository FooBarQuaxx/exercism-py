def slices(s: str, n: int):

    s_len = len(s)
    if n > s_len or n <= 0:
        raise ValueError

    return [
        [int(x) for x in s[i:i+n]]
        for i in range(s_len - n + 1)
    ]


def largest_product(s: str, n: int):
    if n == 0:
        return 1

    if not s.isdigit() or len(s) < n:  # this includes the case when n < 0
        raise ValueError

    from operator import mul
    from functools import reduce
    return max(
        reduce(mul, s, 1) for s in slices(s, n)
    )
