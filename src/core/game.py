from ..entities.dino import Dino
from ..entities.obstacles.ObstacleSpawner import ObstacleSpawner
from .CollisionManager import CollisionManager
from ..gameState.playState import PlayState
from ..gameState.menuState import MenuState



import pygame
import os

class Game:
    def __init__(self, screen, ai=False):
        CACTUS_Y_LEVEL = 200

        # Initializing Pygame screen
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Background
        self.background = pygame.image.load(os.path.join("assets", "background", "ground.png"))
        self.background_location = (0 ,190)

        # AI mode
        self.ai = ai

        # Game states
        self.running = True

        # Counting frames
        self.frame_count = 0

        # Instantiate classes
        if not self.ai:
            self.dino = Dino()
        else:
            self.dino = None  # Will be set by main() for AI mode
            self.ai_dinos = []
            self.ai_nets = []
            self.ai_genomes = []
        
        self.ObstacleSpawner = ObstacleSpawner(-6)
        self.CollisionManager = CollisionManager(self.dino, self.ObstacleSpawner)
        self.MenuState = MenuState()
        self.PlayState = PlayState()


        # Obstacles
        self.obstacles = []

        # Game state
        self.gamestate = "play" if self.ai else "menu"

        
    def run(self):
        while self.running:
            # Game logic
            self.draw()
            self.handle_events()
            self.update()

            # Control frame-rate
            self.clock.tick(60)
            self.frame_count += 1

            if self.ai:
                # AI mode: process AI decisions and check if all dinos died
                self.process_ai()
                if len([d for d in self.ai_dinos if not d.isDead]) == 0:
                    self.running = False
            else:
                # Human mode: check single dino
                if self.dino.isDead == True:
                    self.gamestate = "lose"

            # Updated Pygame
            pygame.display.flip()


    def update(self):
        if self.ai:
            # AI mode: update obstacles and AI dinos
            self.ObstacleSpawner.update(self.frame_count)
            for dino in self.ai_dinos:
                if not dino.isDead:
                    dino.update()
                    self.CollisionManager.check_dino_collision(dino)
        else:
            # Human mode: use existing state system
            if self.gamestate == "menu":
                self.MenuState.update()
            elif self.gamestate == "play":
                self.PlayState.update(self.dino, self.ObstacleSpawner, self.CollisionManager, self.frame_count)
            elif self.gamestate == "lose":
                self.PlayState.update(self.dino, self.ObstacleSpawner, self.CollisionManager, self.frame_count)


    def draw(self):
        self.screen.fill("#EDEEF0")
        self.screen.blit(self.background, self.background_location)

        if self.ai:
            # AI mode: draw obstacles and all AI dinos
            self.ObstacleSpawner.draw(self.screen)
            for dino in self.ai_dinos:
                if not dino.isDead:
                    dino.draw(self.screen, self.frame_count)
        else:
            # Human mode: use existing state system
            if self.gamestate == "menu":
                self.MenuState.draw(self.screen)
            elif self.gamestate == "play":
                self.PlayState.draw(self.dino, self.ObstacleSpawner, self.screen, self.frame_count, self.gamestate)
            elif self.gamestate == "lose":
                self.PlayState.draw(self.dino, self.ObstacleSpawner, self.screen, self.frame_count, self.gamestate)



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.running = False
            if self.gamestate == "menu":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gamestate = "play"

            elif self.gamestate == "play":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dino.jump()

            elif self.gamestate == "lose":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.PlayState.resetGame(self.dino, self.ObstacleSpawner)
                        self.gamestate = "play"
                        
