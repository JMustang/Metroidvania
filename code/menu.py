import pygame
from settings import *

class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.create_button()

    def create_button(self):

        # menu area general
        size = 180
        margin = 6
        topLeft = (WINDOW_WIDTH - size - margin, WINDOW_HEIGHT - size - margin)
        self.rect = pygame.Rect(topLeft, (size, size))

    def display(self):
        pygame.draw.rect(self.display_surface, 'red', self.rect)