import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, sizex, sizey, speed):
        super().__init__()
        
        self.image = pygame.Surface((sizex, sizey))
        pygame.draw.rect(self.image, color, [10, 300, sizex, sizey])
        self.rect = self.image.get_rect()
        self.speed = speed


class PlayerPaddle(Paddle):
    def update(self):
        pass


class EnemyPaddle(Paddle):
    def update(self):
        pass
