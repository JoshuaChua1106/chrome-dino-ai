import pygame

class CollisionManager:
    def __init__(self, dino, ObstacleSpawner):
        self.dino = dino
        self.ObstacleSpawner = ObstacleSpawner

        self.obstacleListRect = []

        self.isCollided = False

    def update(self):
        self.checkCollision()
        self.handleCollision()


    def checkCollision(self):
        dino_rect = self.dino.get_dino_rect()
        self.obstacleListRect = self.ObstacleSpawner.getObstacleListRect()

        self.isCollided = False
        for obstacleRect in self.obstacleListRect:
            if dino_rect.colliderect(obstacleRect):
                self.isCollided = True
        
        
    def handleCollision(self):
        if self.isCollided:
            self.dino.setisDead(True)
            self.ObstacleSpawner.stopAllObstacles()
            