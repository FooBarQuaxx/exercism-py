#!/usr/bin/env python


def to_rna(s):
    return ''.join(
            list(map(lambda x: {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}[x], s))
            )
