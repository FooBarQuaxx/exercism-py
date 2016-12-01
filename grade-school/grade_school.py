#!/usr/bin/env python
from collections import OrderedDict, defaultdict


class School(object):
    def __init__(self, name=None):
        self._name = name
        self._grades = defaultdict(set)

    def grade(self, gr):
        return self._grades[gr]

    def add(self, student, gr):
        self._grades[gr].add(student)

    def sort(self):
        res = OrderedDict()
        for grade in sorted(self._grades.keys()):
            res[grade] = tuple(sorted(self._grades[grade]))
        return res.items()
