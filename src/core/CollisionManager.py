import pygame

class CollisionManager:
    def __init__(self, dino, ObstacleSpawner):
        self.dino = dino  # Single dino for human mode
        self.ObstacleSpawner = ObstacleSpawner
        self.obstacleListRect = []
        self.isCollided = False

    def update(self):
        # Human mode - check single dino
        if self.dino:
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
    
    def check_dino_collision(self, dino):
        """Check collision for a specific dino (used in AI mode)"""
        dino_rect = dino.get_dino_rect()
        obstacle_rects = self.ObstacleSpawner.getObstacleListRect()
        
        for obstacle_rect in obstacle_rects:
            if dino_rect.colliderect(obstacle_rect):
                dino.setisDead(True)
                return True
        return False
            