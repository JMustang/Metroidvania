import pygame
from settings import *

class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.create_button()

    def create_button(self):

        # menu area
        size = 180
        margin = 6
        topLeft = (WINDOW_WIDTH - size - margin, WINDOW_HEIGHT - size - margin)
        self.rect = pygame.Rect(topLeft, (size, size))

        # Button area
        self.generic_button_rect = pygame.Rect(self.rect.topleft, (self.rect.width / 2, self.rect.height / 2))

    def display(self):
        pygame.draw.rect(self.display_surface, 'red', self.rect)
        pygame.draw.rect(self.display_surface, 'yellow', self.generic_button_rect)