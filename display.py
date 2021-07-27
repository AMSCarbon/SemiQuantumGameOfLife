import pygame
from pygame import Rect
from model import Model

# Set up the drawing window
SCREEN_X = 500
SCREEN_Y = 500

class Display:
    def __init__(self, screen_x: int = SCREEN_X, screen_y: int = SCREEN_Y, model: Model = None):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.screen = pygame.display.set_mode([screen_x, screen_y])
        if model:
            self.determine_sizing(model)
        else:
            self.rows = 0
            self.cols = 0
            self.x_size = 0
            self.y_size = 0

    def determine_sizing(self, model):
        self.rows, self.cols = model.get_dimensions()
        self.x_size = int(self.screen_x / self.rows)
        self.y_size = int(self.screen_y / self.cols)

    def update(self, model: Model):
        # Fill the background with white
        self.screen.fill((255, 255, 255))
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if model.should_draw(i, j):
                    pygame.draw.rect(self.screen, model.get_cell_colour(i, j),
                                     Rect(i * self.x_size, j * self.y_size, self.x_size, self.y_size))
        # Update the display
        pygame.display.flip()
