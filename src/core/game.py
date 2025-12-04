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
        
        # Fitness tracking
        self.fitness = 0
        self.obstacles_cleared = 0
        self.cleared_obstacle_ids = set()  # Track which obstacles have been counted
        self.total_jumps = 0  # Track total jumps for penalty

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
            self.check_obstacles_cleared()
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
    
    def process_ai(self):
        """Process AI decisions for each dino"""
        for i, dino in enumerate(self.ai_dinos):
            if not dino.isDead:
                # Get AI inputs
                inputs = self.get_ai_inputs(dino)
                
                # Get neural network decision
                output = self.ai_nets[i].activate(inputs)
                
                # Jump if output > 0.5
                if output[0] > 0.5:
                    if dino.jump():  # jump() returns True if jump was successful
                        self.total_jumps += 1
        
        # Update fitness for dead dinos
        for i, dino in enumerate(self.ai_dinos):
            if dino.isDead and self.ai_genomes[i].fitness == 0:
                self.ai_genomes[i].fitness = self.calculate_fitness()
    
    def calculate_fitness(self):
        """Calculate fitness based on survival time, game speed, obstacles cleared, and jump efficiency"""
        base_fitness = self.frame_count  # Base score from survival time
        speed_bonus = abs(self.ObstacleSpawner.getGameSpeed()) * 10  # Bonus for surviving at higher speeds
        obstacle_bonus = self.obstacles_cleared * 50  # Bonus for jumping over obstacles
        jump_penalty = self.total_jumps * 5  # Penalty for unnecessary jumps
        return base_fitness + speed_bonus + obstacle_bonus - jump_penalty
    
    def check_obstacles_cleared(self):
        """Check if any obstacles have been passed by all living dinos"""
        living_dinos = [dino for dino in self.ai_dinos if not dino.isDead]
        if not living_dinos:
            return
            
        # Find leftmost living dino position
        min_dino_x = min(dino.x for dino in living_dinos)
        
        # Check obstacles that have been passed
        for obstacle in self.ObstacleSpawner.getObstacleList():
            obstacle_id = id(obstacle)  # Use object id as unique identifier
            # If obstacle is behind the leftmost dino and not already counted
            if obstacle.x < min_dino_x - 50 and obstacle_id not in self.cleared_obstacle_ids:
                self.obstacles_cleared += 1
                self.cleared_obstacle_ids.add(obstacle_id)
    
    def get_ai_inputs(self, dino):
        """Get sensor inputs for AI"""
        # Find nearest obstacle
        nearest_obstacle = None
        min_distance = float('inf')
        
        for obstacle in self.ObstacleSpawner.getObstacleList():
            distance = obstacle.get_distance_to_dino(dino.x)
            if distance > 0 and distance < min_distance:
                min_distance = distance
                nearest_obstacle = obstacle
        
        if nearest_obstacle:
            obstacle_distance = min_distance
            obstacle_height = nearest_obstacle.getHeight()
        else:
            obstacle_distance = 800
            obstacle_height = 0
        
        return [
            dino.y / 400.0,
            obstacle_distance / 800.0,
            obstacle_height / 100.0,
            abs(self.ObstacleSpawner.getGameSpeed()) / 10.0
        ]
                        
