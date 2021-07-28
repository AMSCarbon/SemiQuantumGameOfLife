import pygame
from display import Display
from classic_model import ClassicModel
import sys
from benchmarking import print_benchmarking, record_duration
from time import perf_counter, sleep

def main():
    rows, cols, cell_size = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    pygame.init()
    model = ClassicModel(rows, cols)
    display = Display(rows*cell_size, cols*cell_size)
    display.determine_sizing(model)
    running = True
    display.update(model)
    while running:
        frame_start = perf_counter()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        model.update()
        display.update(model)
        frame_end = perf_counter()
        # if the frame took less than 0.1 seconds to complete, sleep til you're over
        if frame_end-frame_start < 0.1:
            sleep(0.1-(frame_end-frame_start))
    pygame.quit()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python ./main.py <columns> <rows> <cell sizes>")
        sys.exit(1)
    main()
    print_benchmarking()
