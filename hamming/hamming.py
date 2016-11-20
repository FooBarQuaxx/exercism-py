import functools


def distance(s1, s2):
    return functools.reduce(lambda x, y: x + y,
                            map(lambda x: 1 if x[0] != x[1] else 0, zip(s1, s2)), 0)
