import pygame
from display import Display
from classic_model import ClassicModel
from q_model import QModel
import sys
from benchmarking import print_benchmarking, record_duration

def main():
    rows, cols, cell_size = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    pygame.init()
    model = QModel(rows, cols)
    display = Display(rows*cell_size, cols*cell_size)
    display.determine_sizing(model)
    running = True
    display.update(model)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        model.update()
        display.update(model)
    pygame.quit()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python ./main.py <columns> <rows> <cell sizes>")
        sys.exit(1)
    main()
    print_benchmarking()
