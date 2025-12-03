from .cactus import Cactus


class ObstacleSpawner:
    def __init__(self):
        self.CACTUS_X_LEVEL = 1000
        self.CACTUS_Y_LEVEL = 200

        self.cactus_types = ["TallShortCactus", "TallMediumCactus", "TallLongCactus", "ShortShortCactus", "ShortMediumCactus", "ShortLongCactus"]

        self.obstacle_types = ["Cactus"]
        self.spawn_interval = 0
        self.last_spawntime = 0

    def should_spawn(self, current_time):
        return current_time - self.last_spawntime > self.spawn_interval

    def create_obstacle(self, speed):
        return Cactus(self.CACTUS_X_LEVEL, self.CACTUS_Y_LEVEL, speed)