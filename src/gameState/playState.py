import pygame

class PlayState:

    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 30)  # "Arial", size 30

    def update(self, dino, ObstacleSpawner, CollisionManager):
        
        dino.update()
        ObstacleSpawner.update()
        CollisionManager.update()


    def draw(self, dino, ObstacleSpawner, screen, frame_count, gamestate):
        dino.draw(screen, frame_count)
        ObstacleSpawner.draw(screen)

        if gamestate == "lose":
            text_surface = self.font.render("Press spacebar to start again", True, (0, 0, 0))  # text, antialias, color

            screen.blit(text_surface, (350, 100))  # x=100, y=100 on screen

            

    def resetGame(self, dino, ObstacleSpawner):
        ObstacleSpawner.resetObstacles()
        dino.resetDino()
