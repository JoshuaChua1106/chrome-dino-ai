from ..entities.dino import Dino
import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.dino = Dino()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def update(self):
        self.dino.update()

    def draw(self):
        self.screen.fill("#EDEEF0")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
