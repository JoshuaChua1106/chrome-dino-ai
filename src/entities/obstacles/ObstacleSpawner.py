from .ObstacleFactory import ObstacleFactory

import random
import pygame

class ObstacleSpawner:
    def __init__(self, speed):
        self.factory = ObstacleFactory()
        self.spawn_timer = 0

        # Spawning information
        self.last_spawntime = 0
        self.spawn_interval = 1500 #(ms)

        self.current_time = pygame.time.get_ticks()


        # Obstacle information
        self.speed = speed


    def update(self):
        if self.should_spawn:
            self.last_spawn_time = self.current_time
            return self.factory.createObstacle(self.speed)

    def should_spawn(self):
        if self.current_time - self.last_spawn_time >= self.spawn_interval:
            return True
        else:
            return False
