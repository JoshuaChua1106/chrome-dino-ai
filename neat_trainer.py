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
        
        # Run evolution - main() will serve as eval_genomes
        winner = population.run(main, 50)  # 50 generations
        
        # Save the best genome
        with open("best_genome.pickle", "wb") as f:
            pickle.dump(winner, f)
        
        print(f"\nTraining complete! Best fitness: {winner.fitness}")
        return winner

if __name__ == "__main__":
    trainer = NEATTrainer()
    trainer.run_neat()