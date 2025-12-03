class Obstacle:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        
        self.speed = speed
        self.image = image

    def update(self):
        self.x += self.speed
        

    def draw(self, screen):
        self.img_location = self.image.get_rect()
        self.img_location.bottom = self.y
        self.img_location.centerx = self.x
        screen.blit(self.image, self.img_location)

