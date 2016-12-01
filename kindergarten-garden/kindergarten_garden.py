#!/usr/bin/env python
from enum import Enum, unique
from collections import OrderedDict


@unique
class Plan(Enum):
    Radishes = 'R'
    Clover = 'C'
    Grass = 'G'
    Violets = 'V'


ChildEnum = None


DEFAULT_STUDENTS = """
Alice
Bob
Charlie
David
Eve
Fred
Ginny
Harriet
Ileana
Joseph
Kincaid
Larry
""".strip().split()


def make_child_enum(students):
    global ChildEnum
    students = sorted(students)
    enum_map = OrderedDict()
    enum_map = {student: (i, i + 2) for i, student in zip(range(0, 2 * len(students), 2), students)}
    ChildEnum = Enum('ChildEnum', dict(enum_map))


class Garden(object):
    def __init__(self, sills, students=DEFAULT_STUDENTS):
        self._row1, self._row2 = sills.split('\n')
        make_child_enum(students)

    def __repr__(self):
        return '<{}("{}\\n{}")>'.format(self.__class__.__name__, self._row1, self._row2)

    def plants(self, child):
        assert ChildEnum is not None
        row_slice = slice(*ChildEnum[child].value)
        plants = self._row1[row_slice] + self._row2[row_slice]
        return [Plan(plan).name for plan in plants]
