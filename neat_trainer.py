import neat
import pickle
from main import main

class NEATTrainer:
    def __init__(self):
        self.generation = 0
        
    def run_neat(self):
        """Main NEAT training function"""
        config_path = "config.txt"
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                   neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                   config_path)
        
        # Create population
        population = neat.Population(config)
        
        # Add reporters for tracking progress
        population.add_reporter(neat.StdOutReporter(True))
        population.add_reporter(neat.StatisticsReporter())
        population.add_reporter(neat.Checkpointer(5))
        
        # Initialize pygame once for all generations
        import pygame
        pygame.init()
        screen = pygame.display.set_mode((1000, 300))
        pygame.display.set_caption("NEAT Training")
        
        # Create wrapper function that passes screen
        def eval_genomes_with_screen(genomes, config):
            main(genomes, config, screen)
        
        # Run evolution
        winner = population.run(eval_genomes_with_screen, 50)
        
        # Cleanup pygame
        pygame.quit()
        
        # Save the best genome
        with open("best_genome.pickle", "wb") as f:
            pickle.dump(winner, f)
        
        print(f"\nTraining complete! Best fitness: {winner.fitness}")
        return winner

if __name__ == "__main__":
    trainer = NEATTrainer()
    trainer.run_neat()