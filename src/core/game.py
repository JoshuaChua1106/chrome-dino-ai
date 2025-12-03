from ..entities.dino import Dino
import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True


        # Instantiate classes
        self.dino = Dino()


    def run(self):
        while self.running:
            self.draw()
            self.handle_events()
            self.update()
            self.clock.tick(60)
            pygame.display.flip()


    def update(self):
        self.dino.update()

    def draw(self):
        self.screen.fill("#EDEEF0")
        self.dino.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.dino.jump()

            
