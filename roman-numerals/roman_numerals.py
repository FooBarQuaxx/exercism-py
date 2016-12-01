#!/usr/bin/env python
from enum import Enum
from functools import partial


RNE = Enum('RomainNumeralEnum', {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})


def numeral(arabic):
    thousand, hundred, tens, digits = [int(x) for x in "{:0>4}".format(arabic)]

    def _show_part(one, five, ten, num):
        assert num in range(0, 10)
        if num is 0:
            return ''
        if 1 <= num < 4:
            return num * one
        elif num is 4:
            return one + five
        elif 5 <= num < 9:
            return five + one * abs(5 - num)
        elif num is 9:
            return one + ten
        assert False

    _show_digits = partial(_show_part, RNE(1).name, RNE(5).name, RNE(10).name)
    _show_tens = partial(_show_part, RNE(10).name, RNE(50).name, RNE(100).name)
    _show_hundred = partial(_show_part, RNE(100).name, RNE(500).name, RNE(1000).name)

    def _show_thousand(num):
        assert num in range(0, 4)
        return num * RNE(1000).name

    _locals = locals()
    return ''.join([
        _locals['_show_' + part](_locals[part])
        for part in ('thousand', 'hundred', 'tens', 'digits')
    ])
