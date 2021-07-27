from typing import Tuple, List

ROWS = 500
COLS = 500

class Model:
    def __init__(self, cols: int = COLS, rows: int = ROWS):
        self.cols = cols
        self.rows = rows
        pass

    def update(self):
        pass

    def get_dimensions(self) -> Tuple[int, int]:
        pass

    def get_neighbours(self, row: int , col: int):
        pass

    def get_cell_colour(self, col: int, row: int):
        pass

    def should_draw(self, col: int, row: int) -> bool:
        pass