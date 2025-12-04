from src.core.game import Game
from src.entities.dino import Dino
import neat
import sys
import pygame

def main(genomes=None, config=None, screen=None):
    # Attributes
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 300

    # Initialize pygame screen only if not provided
    if screen is None:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    if genomes is None:
        # Human player mode
        game = Game(screen)
        game.run()
        pygame.quit()
    else:
        # AI training mode
        game = Game(screen, ai=True)
        
        # Create AI players from genomes
        nets = []
        dinos = []
        ge = []
        
        for genome_id, genome in genomes:
            genome.fitness = 0
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            nets.append(net)
            dinos.append(Dino())
            ge.append(genome)
        
        # Replace single dino with multiple AI dinos
        game.ai_dinos = dinos
        game.ai_nets = nets
        game.ai_genomes = ge
        
        # Run game
        game.run()
        
        # Only quit pygame if we initialized it (human mode)
        if screen is None:
            pygame.quit()

def get_ai_inputs(dino, obstacle_spawner):
    """Get sensor inputs for AI"""
    # Find nearest obstacle
    nearest_obstacle = None
    min_distance = float('inf')
    
    for obstacle in obstacle_spawner.getObstacleList():
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
        obstacle_height / 100.0
    ]

if __name__ == "__main__":
    main()