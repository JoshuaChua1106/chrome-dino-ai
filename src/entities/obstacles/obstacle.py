class Obstacle:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        
        self.speed = speed
        self.image = image

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        self.img_location = self.image.get_rect()
        self.img_location.center = (self.x, self.y)
        screen.blit(self.image, self.img_location)

