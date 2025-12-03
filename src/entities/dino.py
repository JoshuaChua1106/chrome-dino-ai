import pygame
import os

class Dino:
    def __init__(self):

        # Dino imaging
        self.image = pygame.image.load(os.path.join("assets", "dino", "DinoRun1.png"))
        self.scale_factor = 0.5
        self.new_width = int(self.image.get_width() * self.scale_factor)
        self.new_height = int(self.image.get_height() * self.scale_factor)
        self.scaled_image = pygame.transform.scale(self.image, (self.new_width, self.new_height))


        # Dino Location
        self.x = 100
        self.y = 150

        # Dino physics
        self.velocity = 0
        self.gravity = 1
        self.jump_strength = -15

        # Dino state
        self.is_jumping = False

        # Other
        self.ground_y = 200

    def draw(self, screen):
        self.img_location = self.image.get_rect()
        self.img_location.center = (self.x, self.y)
        screen.blit(self.scaled_image, self.img_location)


    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        
        # Stop velocity when dino is on the ground
        if self.y > self.ground_y:
            self.y = self.ground_y
            self.velocity = 0
            self.is_jumping = False

    
    def jump(self):
        if self.is_jumping == False:
            self.velocity = self.jump_strength
            self.is_jumping = True

