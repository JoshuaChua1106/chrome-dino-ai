import pygame

class CollisionManager:
    def __init__(self, dino, ObstacleSpawner):
        self.dino = dino
        self.ObstacleSpawner = ObstacleSpawner

        self.obstacleListRect = []

    def update(self):
        self.checkCollision()

    def checkCollision(self):
        dino_rect = self.dino.get_dino_rect()
        self.obstacleListRect = self.ObstacleSpawner.getObstacleListRect()

        for obstacleRect in self.obstacleListRect:
            if dino_rect.colliderect(obstacleRect):
                print("Collision detected!")
        

    def handleCollision(self):
        pass