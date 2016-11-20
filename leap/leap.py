#!/usr/bin/env python


def is_leap_year(year):
    def divisible_by(m, n):
        return m % n == 0

    return divisible_by(year, 4) and not divisible_by(year, 100) or \
        divisible_by(year, 4) and \
        divisible_by(year, 100) and \
        divisible_by(year, 400)
