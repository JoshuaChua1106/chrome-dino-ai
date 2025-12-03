from src.core.game import Game


import sys
import pygame

def main():

    # Attributes
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    # Initialize pygame screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    game = Game(screen)
    
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()