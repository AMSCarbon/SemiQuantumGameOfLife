from typing import List
from benchmarking import record_duration

from cell import Cell
import math


class QCell(Cell):
    def __init__(self, initial_value):
        super().__init__(initial_value)
        self.a: float = initial_value
        self.d: float = math.sqrt(1.0 - initial_value ** 2)

    @record_duration
    def get_next_state(self, neighbours: List):
        # 12.5 A =  sum of the a coefficients for all neighbours.
        live_neighbours: float = sum([n.a for n in neighbours])
        # 12.6 G is the state transition matrix determined by A
        g = self.get_G_matrix(live_neighbours)
        # 12.9 new_state = G * old_state
        new_a = g[0][0] * self.a + g[0][1] * self.d
        new_b = g[1][0] * self.a + g[1][1] * self.d
        # 12.2 normalise so |a|^2 + |b|^2 = 1
        magnitude = new_a ** 2 + new_b ** 2
        new_a = math.sqrt(new_a ** 2 / magnitude)
        new_b = math.sqrt(new_b ** 2 / magnitude)
        return (new_a, new_b)

    def alive(self):
        return self.a ** 2

    @staticmethod
    def get_G_matrix(live: float):
        d = [[0, 0], [1, 1]]
        if 0 <= live <= 1.0:
            return d
        elif 1.0 < live <= 2.0:
            d_scalar = (math.sqrt(2) + 1) * (2.0 - live)
            s_scalar = (live - 1.0)
            return [[s_scalar, 0], [d_scalar, (d_scalar + s_scalar)]]
        elif 2.0 < live <= 3.0:
            s_scalar = (math.sqrt(2) + 1) * (3.0 - live)
            b_scalar = (live - 2.0)
            return [[s_scalar + b_scalar, b_scalar], [0, s_scalar]]
        elif 3.0 < live <= 4.0:
            b_scalar = (math.sqrt(2) + 1) * (4.0 - live)
            d_scalar = (live - 3.0)
            return [[b_scalar, b_scalar], [d_scalar, d_scalar]]
        else:
            return d

    def set_a(self, a):
        self.a: float = a
        self.d: float = math.sqrt(1.0 - a ** 2)

    def get_colour(self):
        v = 255 - self.a ** 2 * 255.0
        return (v, v, v)
