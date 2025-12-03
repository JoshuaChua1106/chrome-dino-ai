import pygame
import os

class Dino:
    def __init__(self):

        # Dino imaging
        self.image = pygame.image.load(os.path.join("assets", "dino", "DinoRun1.png"))
        self.location = (600,600)

        # Dino Location
        self.y = 300

        # Dino physics
        self.velocity = 0
        self.gravity = 1
        self.jump_strength = 1

        # Dino state
        self.is_jumping = False

        # Other
        self.ground_y = 300

    def draw(self, screen):
        self.img_location = self.image.get_rect()
        self.img_location.center = self.location
        screen.blit(self.image, self.img_location)


    def jump(self):
        if self.is_jumping == False:
            self.velocity = self.jump_strength
            self.is_jumping = True

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        # Stop velocity when dino is on the ground
        if self.y == self.ground_y:
            self.y = self.ground_y
            self.velocity = 0
            self.is_jumping = False
