from .cactus import Cactus

import random

class ObstacleSpawner:
    def __init__(self):
        self.CACTUS_X_LEVEL = 1000
        self.CACTUS_Y_LEVEL = 200

        self.cactus_types = ["TallShortCactus", "TallMediumCactus", "TallLongCactus", "ShortShortCactus", "ShortMediumCactus", "ShortLongCactus"]
        self.cactus_weights = [20, 12, 8, 30, 20, 10]

        self.obstacle_types = ["Cactus"]
        self.spawn_interval = 0
        self.last_spawntime = 0


    def create_obstacle(self, speed):
        # Random to determine if cactus or bird (0.75 cactus, 0.25 bird)
        # If cactus, run define_cactus_obstacle to determine which cactus to spawn
        # Spawning logic.

        return Cactus(self.CACTUS_X_LEVEL, self.CACTUS_Y_LEVEL, speed)
    
    
    def define_cactus_obstacle(self):
        # Random calculation to determine which cactus to spawn.
        chosen_cactus = random.choices(self.cactus_types, weights=self.weights, k=1)[0]

        return chosen_cactus
    
    