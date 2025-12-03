from ..obstacles.obstacle import Obstacle

import pygame
import os
import random

class Cactus(Obstacle):
    def __init__(self, x, y, speed):

        self.image = self.image_preprocessing()

        super().__init__(x, y, speed, self.image)


    def image_preprocessing(self):
        # Cactus imaging
        self.scale_factor = 0.5

        self.LargeCactus1 = pygame.image.load(os.path.join("assets", "cactus", "LargeCactus1.png"))
        self.LargeCactus2 = pygame.image.load(os.path.join("assets", "cactus", "LargeCactus2.png"))
        self.LargeCactus3 = pygame.image.load(os.path.join("assets", "cactus", "LargeCactus3.png"))

        self.SmallCactus1 = pygame.image.load(os.path.join("assets", "cactus", "SmallCactus1.png"))
        self.SmallCactus2 = pygame.image.load(os.path.join("assets", "cactus", "SmallCactus2.png"))
        self.SmallCactus3 = pygame.image.load(os.path.join("assets", "cactus", "SmallCactus3.png"))

        temp_cactusList = [self.LargeCactus1, self.LargeCactus2, self.LargeCactus3, self.SmallCactus1, self.SmallCactus2, self.SmallCactus3]
        cactusList = []

        for cactus in temp_cactusList:
            cactus_new_width = int(cactus.get_width() * self.scale_factor)
            cactus_new_height = int(cactus.get_height() * self.scale_factor)

            cactusList.append(pygame.transform.scale(cactus, (cactus_new_width, cactus_new_height)))

        random_int = random.randint(0,5)

        return cactusList[random_int]