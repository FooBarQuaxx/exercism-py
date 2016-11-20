#!/usr/bin/env python
from __future__ import division


class Clock(object):
    def __init__(self, hours, minutes):
        self.hours = self.minutes = 0
        self.add(hours * 60  + minutes)

    def add(self, minutes):
        if minutes >= 0:
            self.hours += minutes // 60
            self.minutes += minutes % 60
        else:
            abs_minutes = abs(minutes)
            to_remove_hours = abs_minutes // 60
            to_remote_minutes = abs_minutes % 60
            self.hours -= to_remove_hours
            if to_remote_minutes > 0:
                self.hours -= 1
                self.minutes += 60 - to_remote_minutes
        self.hours += self.minutes // 60
        self.hours %= 24
        self.minutes %= 60
        return self

    def __str__(self):
        return "{:0>2d}:{:0>2d}".format(self.hours, self.minutes)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return False
        return self.hours == other.hours and self.minutes == other.minutes
