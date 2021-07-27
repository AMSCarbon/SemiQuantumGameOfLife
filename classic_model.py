from model import Model, COLS, ROWS
from typing import Tuple
from classic_cell import ClassicCell, CellState
import random
from benchmarking import record_duration


class ClassicModel(Model):
    def __init__(self, x: int = COLS, y: int = ROWS):
        super().__init__(x, y)
        self.grid = self.__create_empty_matrix()
        self.populate()

    def populate(self):
        initial_rate = 0.1
        for i in range(self.cols):
            for j in range(self.rows):
                if random.uniform(0.0, 1.0) < initial_rate:
                    self.grid[i][j].state = CellState.Alive

    @record_duration
    def update(self):
        # create a copy of the matrix.
        new_grid = self.__create_empty_matrix()
        for i in range(self.cols):
            for j in range(self.rows):
                cell_neighbours = self.get_neighbours(i, j)
                new_grid[i][j].state = self.grid[i][j].get_next_state(cell_neighbours)
        self.grid = new_grid

    def get_dimensions(self) -> Tuple[int, int]:
        return self.cols, self.rows

    @record_duration
    def get_neighbours(self, col: int, row: int):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    pass
                # modulo allows for wrap around.
                neighbours.append(self.grid[(col + i) % self.cols][(row + j) % self.rows])
        return neighbours

    def would_overflow(self, col, row, i, j):
        return not(0 <= col + i < self.cols and 0 <= row + j < self.cols)

    def should_draw(self, col: int, row: int) -> bool:
        return self.grid[col][row].state == CellState.Alive

    def get_cell_colour(self, col: int, row: int):
        return (0, 0, 0) if self.grid[col][row].state == CellState.Alive else (255, 255, 255)

    @record_duration
    def __create_empty_matrix(self):
        return [[ClassicCell(0) for i in range(self.rows)] for j in range(self.cols)]
