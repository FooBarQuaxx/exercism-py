NORTH = 1 << 0
EAST = 1 << 1
SOUTH = 1 << 2
WEST = 1 << 3


def bearning_name(code):
    index = "{0:b}".format(code)[::-1].index('1')
    return ['NORTH', 'EAST', 'SOUTH', 'WEST'][index]


class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self._bearing = bearing
        self._x, self._y = x, y

    @property
    def coordinates(self):
        return (self._x, self._y)

    @property
    def bearing(self):
        return self._bearing

    def turn_left(self):
        self._bearing >>= 1
        if self._bearing <= 0:
            self._bearing = WEST

    def turn_right(self):
        self._bearing <<= 1
        if self._bearing >= 16:
            self._bearing = NORTH

    def advance(self):
        self._x += {EAST: 1, WEST: -1}.get(self.bearing, 0)
        self._y += {NORTH: 1, SOUTH: -1}.get(self.bearing, 0)

    def simulate(self, insts):
        for inst in insts:
            move = {'R': self.turn_right, 'A': self.advance,
                    'L': self.turn_left}.get(inst)
            move()

    def __repr__(self):
        return "<{}({}, {}, {})>".format(self.__class__.__name__, bearning_name(self.bearing), *self.coordinates)
