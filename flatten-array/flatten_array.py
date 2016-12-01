#!/usr/bin/env python
from collections import Iterable 

try:
    from functools import reduce
except ImportError as e:
    pass 

def flatten(ary):
    def _reducer(x, y):
        if isinstance(y, Iterable) and not isinstance(y, (str, bytes)):
            val = flatten(y)
        else:
            val = ([y] if y is not None else [])
        return x + val
    return reduce(_reducer, ary, [])
