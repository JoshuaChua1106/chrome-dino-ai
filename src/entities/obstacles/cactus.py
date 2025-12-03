from ..obstacles.obstacle import Obstacle

import pygame
import os
import random

class Cactus(Obstacle):
    def __init__(self, x, y, speed, image):

        self.image = image

        super().__init__(x, y, speed, self.image)


