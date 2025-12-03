class Dino:
    def __init__(self):

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
