import pygame

WHITE = (255, 255, 255)


class Background(pygame.sprite.Sprite):
    def __init__(self, color=WHITE, size=[10, 10], axis="center", position=(0, 0)):
        super().__init__()
        
        self.image = pygame.Surface(size)
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        self.rect = self.image.get_rect()
        self.rect.__setattr__(axis, position)
