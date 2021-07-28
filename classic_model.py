from model import Model, COLS, ROWS
from typing import Tuple
from classic_cell import ClassicCell, CellState
import random
from benchmarking import record_duration


class ClassicModel(Model):
    def __init__(self, x: int = COLS, y: int = ROWS):
        super().__init__(x, y)
        self.grid = self.__create_empty_matrix()
        self.live_cells = []
        self.populate()

    def populate(self):
        initial_rate = 0.1
        for i in range(self.cols):
            for j in range(self.rows):
                if random.uniform(0.0, 1.0) < initial_rate:
                    self.grid[i][j].state = CellState.Alive
                    self.live_cells.append(self.grid[i][j])

    @record_duration
    def update_old(self):
        # create a copy of the matrix.
        new_grid = self.__create_empty_matrix()
        for i in range(self.cols):
            for j in range(self.rows):
                cell_neighbours = self.get_neighbours(i, j)
                new_grid[i][j].state = self.grid[i][j].get_next_state(cell_neighbours)
        self.grid = new_grid

    @record_duration
    def update(self):
        neighbour_occurrences = {}
        for cell in self.live_cells:
            col, row = cell.get_position()
            cell_neighbours = self.get_neighbours(col, row)
            for neighbour in cell_neighbours:
                if neighbour in neighbour_occurrences:
                    neighbour_occurrences[neighbour] += 1
                else:
                    neighbour_occurrences[neighbour] = 1
        new_live_cells = []
        for cell in neighbour_occurrences.keys():
            cell.state = cell.get_next_state(neighbour_occurrences[cell])
            if cell.state == CellState.Alive:
                new_live_cells.append(cell)
        self.live_cells = new_live_cells


    def get_dimensions(self) -> Tuple[int, int]:
        return self.cols, self.rows

    @record_duration
    def get_neighbours(self, col: int, row: int):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
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
        return [[ClassicCell(CellState.Dead, i, j) for j in range(self.rows)] for i in range(self.cols)]
