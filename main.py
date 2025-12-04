from src.core.game import Game
from src.entities.dino import Dino
import neat
import sys
import pygame

def main(genomes=None, config=None):
    # Attributes
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 300

    # Initialize pygame screen
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


if __name__ == "__main__":
    main()