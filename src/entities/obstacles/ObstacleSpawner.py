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

        self.current_time = 0


        # Obstacle information
        self.speed = speed
        self.speed_increaseFactor = 1.1

        # Obstacle Tracking
        self.obstacleList = []
        self.offScreenX = -10

        self.isStopped = False


    def update(self, frame_count):
        self.current_time = pygame.time.get_ticks()
        self.updateSpeed(frame_count)
        print(frame_count)


        if self.should_spawn():
            self.last_spawntime = self.current_time

            new_obstacle = self.factory.create_obstacle(self.speed)
            if new_obstacle is not None:  # only append if it's not None
                self.obstacleList.append(new_obstacle)


        for obstacle in self.obstacleList:
            obstacle.update()
            if obstacle.is_off_screen(self.offScreenX):  # remove off-screen
                self.obstacleList.remove(obstacle)


    def should_spawn(self):
        if self.current_time - self.last_spawntime >= self.spawn_interval:
            return True
        else:
            return False

    def draw(self, screen):
        for obstacle in self.obstacleList:
            obstacle.draw(screen)

    def getObstacleList(self):
        return self.obstacleList
    
    def getObstacleListRect(self):
        obstacle_rect = []
        for obstacle in self.obstacleList:
            obstacle_rect.append(obstacle.get_obstacle_rect())
        
        return obstacle_rect
    
    def stopAllObstacles(self):
        for obstacle in self.obstacleList:
            obstacle.setIsStopped(True)

    def resetObstacles(self):
        self.obstacleList = []
        self.speed = -6
    
    def updateSpeed(self, frame_count):
        if frame_count % 500 == 0:
            print("BANG")
            self.speed *= self.speed_increaseFactor