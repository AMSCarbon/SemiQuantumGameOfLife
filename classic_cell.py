from cell import Cell
from typing import List
import enum
from benchmarking import record_duration
class CellState(enum.Enum):
    Dead = 0
    Alive = 1

class ClassicCell(Cell):
    def __init__(self, initial_value):
        super().__init__(initial_value)
        self.state: CellState = CellState.Dead

    @record_duration
    def get_next_state(self, neighbours: List):
        live_neighbours = len([n for n in neighbours if n.state == CellState.Alive])
        if self.state == CellState.Alive and ( live_neighbours == 2 or live_neighbours == 3) or \
           self.state == CellState.Dead and live_neighbours == 3:
            return CellState.Alive
        return CellState.Dead

