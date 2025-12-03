from .cactus import Cactus

import random
import pygame

class ObstacleFactory:
    def __init__(self):

        self.obstacleList = ["Cactus", "Bird"]

        # CACTUS
        self.CACTUS_X_LEVEL = 1000
        self.CACTUS_Y_LEVEL = 200

        self.cactus_types = ["LargeShortCactus", "LargeMediumCactus", "LargeLongCactus", "SmallShortCactus", "SmallMediumCactus", "SmallLongCactus"]
        self.cactus_weights = [20, 12, 8, 30, 20, 10]

        # Cactus images
        self.cactus_scale_factor = 0.5
        self.cactusImages = {
            "LargeShortCactus": self.scale_cactus("assets/cactus/LargeCactus1.png"),
            "LargeMediumCactus": self.scale_cactus("assets/cactus/LargeCactus2.png"),
            "LargeLongCactus": self.scale_cactus("assets/cactus/LargeCactus3.png"),
            "SmallShortCactus": self.scale_cactus("assets/cactus/SmallCactus1.png"),
            "SmallMediumCactus": self.scale_cactus("assets/cactus/SmallCactus2.png"),
            "SmallLongCactus": self.scale_cactus("assets/cactus/SmallCactus3.png"),
        }


    def create_obstacle(self, speed):
        # Random to determine if cactus or bird (0.75 cactus, 0.25 bird)
        # If cactus, run define_cactus_obstacle to determine which cactus to spawn
        # Spawning logic.

        selectedObstacle = self.define_cactus_obstacle()
        image = self.cactusImages[selectedObstacle]

        return Cactus(self.CACTUS_X_LEVEL, self.CACTUS_Y_LEVEL, speed, image)
    
    
    def define_cactus_obstacle(self):
        # Random calculation to determine which cactus to spawn.
        chosen_cactus = random.choices(self.cactus_types, weights=self.cactus_weights, k=1)[0]

        return chosen_cactus
    
    
    def scale_cactus(self, path):
        img = pygame.image.load(path)
        w = int(img.get_width() * self.cactus_scale_factor)
        h = int(img.get_height() * self.cactus_scale_factor)
        return pygame.transform.scale(img, (w, h))