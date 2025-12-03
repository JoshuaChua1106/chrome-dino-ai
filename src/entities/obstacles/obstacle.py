import pygame

class Obstacle:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        
        self.speed = speed
        self.image = image

        # Obstacle rectangle
        self.img_location = self.image.get_rect()

        self.isStopped = False

    def update(self):
        if self.isStopped == False:
            self.x += self.speed

        

    def draw(self, screen):
        self.img_location.bottom = self.y
        self.img_location.centerx = self.x
        screen.blit(self.image, self.img_location)


    def is_off_screen(self, xValue):
        if self.x < xValue:
            return True
        else:
            return False
        
    def get_obstacle_rect(self):
        return self.img_location
    
    def setIsStopped(self, value):
        self.isStopped = value