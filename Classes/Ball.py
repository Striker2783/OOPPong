import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, sizex, sizey, speed):
        super().__init__()
        
        self.image = pygame.Surface([sizex, sizey])
        pygame.draw.rect(self.image, color, [0, 0, sizex, sizey])
        self.rect = self.image.get_rect()
        self.speed = speed
    
    def bounce(self):
        pass
    
    def update(self):
        pass