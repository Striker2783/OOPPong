import pygame

WHITE = (255, 255, 255)


class Background(pygame.sprite.Sprite):
    def __init__(self, color=WHITE, sizex=10, sizey=10, axis="center", position=(0, 0)):
        super().__init__()
        
        self.image = pygame.Surface([sizex, sizey])
        pygame.draw.rect(self.image, color, [0, 0, sizex, sizey])
        self.rect = self.image.get_rect()
        self.rect.__setattr__(axis, position)
