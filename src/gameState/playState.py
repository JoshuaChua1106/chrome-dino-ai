import pygame

class PlayState:

    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 30)  # "Arial", size 30

    def update(self, dino, ObstacleSpawner, CollisionManager, frame_count):
        # Human mode - single dino
        if dino:
            dino.update()
        ObstacleSpawner.update(frame_count)
        CollisionManager.update()

    def update_ai(self, dinos, ObstacleSpawner, CollisionManager, frame_count):
        # AI mode - multiple dinos
        ObstacleSpawner.update(frame_count)
        for dino in dinos:
            if not dino.isDead:
                dino.update()
                CollisionManager.check_dino_collision(dino)

    def draw(self, dino, ObstacleSpawner, screen, frame_count, gamestate):
        # Human mode - single dino
        if dino:
            dino.draw(screen, frame_count)
        ObstacleSpawner.draw(screen)

        if gamestate == "lose":
            text_surface = self.font.render("Press spacebar to start again", True, (0, 0, 0))  # text, antialias, color
            screen.blit(text_surface, (350, 100))  # x=100, y=100 on screen

    def draw_ai(self, dinos, ObstacleSpawner, screen, frame_count):
        # AI mode - multiple dinos
        ObstacleSpawner.draw(screen)
        for dino in dinos:
            if not dino.isDead:
                dino.draw(screen, frame_count)

    def resetGame(self, dino, ObstacleSpawner):
        ObstacleSpawner.resetObstacles()
        if dino:
            dino.resetDino()
