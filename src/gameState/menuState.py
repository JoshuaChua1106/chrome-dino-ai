import pygame

class MenuState:

    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 30)  # "Arial", size 30


    def update(self):
        pass

    def draw(self, screen):
        text_surface = self.font.render("Menu", True, (0, 0, 0))  # text, antialias, color
        text_surface = self.font.render("Press Spacebar to Start", True, (0, 0, 0))  # text, antialias, color

        screen.blit(text_surface, (350, 100))  # x=100, y=100 on screen
