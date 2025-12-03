from ..entities.dino import Dino
from ..entities.obstacles.ObstacleSpawner import ObstacleSpawner
from .CollisionManager import CollisionManager
from ..gameState.loseState import LoseState
from ..gameState.playState import PlayState
from ..gameState.menuState import MenuState



import pygame
import os

class Game:
    def __init__(self, screen):
        CACTUS_Y_LEVEL = 200

        # Initializing Pygame screen
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Background
        self.background = pygame.image.load(os.path.join("assets", "background", "ground.png"))
        self.background_location = (0 ,190)


        # Game states
        self.running = True

        # Counting frames
        self.frame_count = 0

        # Instantiate classes
        self.dino = Dino()
        self.ObstacleSpawner = ObstacleSpawner(-4)
        self.CollisionManager = CollisionManager(self.dino, self.ObstacleSpawner)
        self.LoseState = LoseState()
        self.MenuState = MenuState()
        self.PlayState = PlayState()


        # Obstacles
        self.obstacles = []

        # Game state
        self.gamestate = "menu"

        
    def run(self):
        while self.running:
            # Game logic
            self.draw()
            self.handle_events()
            self.update()

            # Control frame-rate
            self.clock.tick(60)
            self.frame_count += 1

            # Check if dino is still alive
            # if self.dino.isDead:
            #     self.gamestate = "lose"

            # Updated Pygame
            pygame.display.flip()


    def update(self):
        if self.gamestate == "menu":
            self.MenuState.update()
        elif self.gamestate == "play":
            self.PlayState.update(self.dino, self.ObstacleSpawner, self.CollisionManager)


    def draw(self):
        self.screen.fill("#EDEEF0")
        self.screen.blit(self.background, self.background_location)

        if self.gamestate == "menu":
            self.MenuState.draw(self.screen)
        elif self.gamestate == "play":
            self.PlayState.draw(self.dino, self.ObstacleSpawner, self.screen, self.frame_count)



    def handle_events(self):

        if self.gamestate == "menu":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gamestate = "play"

        elif self.gamestate == "play":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dino.jump()

            
