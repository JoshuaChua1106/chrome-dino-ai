class PlayState:
    def update(self, dino, ObstacleSpawner, CollisionManager):
        
        dino.update()
        ObstacleSpawner.update()
        CollisionManager.update()


    def draw(self, dino, ObstacleSpawner, screen, frame_count):
        dino.draw(screen, frame_count)
        ObstacleSpawner.draw(screen)