from .ObstacleFactory import ObstacleFactory

import random

class ObstacleSpawner:
    def __init__(self, frame_count, speed):
        self.factory = ObstacleFactory()
        self.spawn_timer = 0

        # Spawning information
        self.spawn_interval = 0
        self.last_spawntime = 0

        # Obstacle information
        self.speed = speed


    def update(self):
        if self.should_spawn:
            return self.factory.createObstacle(self.speed)

    def should_spawn(self, current_time):
        return current_time - self.last_spawntime > self.spawn_interval

