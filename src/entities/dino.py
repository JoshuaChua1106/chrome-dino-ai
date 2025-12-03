import pygame
import os

class Dino:
    def __init__(self):

        # Dino imaging
        self.scale_factor = 0.5

        self.image = pygame.image.load(os.path.join("assets", "dino", "DinoRun1.png"))
        self.new_width = int(self.image.get_width() * self.scale_factor)
        self.new_height = int(self.image.get_height() * self.scale_factor)
        self.scaled_image = pygame.transform.scale(self.image, (self.new_width, self.new_height))

        self.image2 = pygame.image.load(os.path.join("assets", "dino", "DinoRun2.png"))
        self.new_width2 = int(self.image2.get_width() * self.scale_factor)
        self.new_height2 = int(self.image2.get_height() * self.scale_factor)
        self.scaled_image2 = pygame.transform.scale(self.image2, (self.new_width, self.new_height))

        # Dino animation
        self.animation_list = [self.scaled_image, self.scaled_image2]
        self.animation_steps = 2
        self.animation_cooldown = 500

        # Dino death image
        self.imageDeath = pygame.image.load(os.path.join("assets", "dino", "DinoDead.png"))
        self.new_widthDead = int(self.image.get_width() * self.scale_factor)
        self.new_heightDead = int(self.image.get_height() * self.scale_factor)
        self.scaled_imageDead = pygame.transform.scale(self.imageDeath, (self.new_width, self.new_height))


        # Dino Location
        self.x = 100
        self.y = 100

        # Dino rectangle
        self.img_location = self.scaled_image2.get_rect()

        # Dino physics
        self.velocity = 0
        self.gravity = 1
        self.jump_strength = -15

        # Dino state
        self.is_jumping = False
        self.isDead = False

        # Other
        self.ground_y = 180

    def draw(self, screen, frame):
        if self.isDead == False:

            self.img_location.center = (self.x, self.y)

            self.animate(screen, frame)

        elif self.isDead:
            screen.blit(self.scaled_imageDead, self.img_location)
            


    def update(self):
        if self.isDead == False:
            self.velocity += self.gravity
            self.y += self.velocity

            # Stop velocity when dino is on the ground
            if self.y > self.ground_y:
                self.y = self.ground_y
                self.velocity = 0
                self.is_jumping = False

            self.die()

        elif self.isDead:
            self.velocity = 0
    
    def jump(self):
        if self.is_jumping == False:
            self.velocity = self.jump_strength
            self.is_jumping = True

    def animate(self, screen, frame):
        animation_step = (frame//20) % 2
        screen.blit(self.animation_list[animation_step], self.img_location)


    def die(self):
        if self.isDead:
            print("dead")

    def get_dino_rect(self):
        return self.img_location
    
    def setisDead(self, status):
        self.isDead = status

