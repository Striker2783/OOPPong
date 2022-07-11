import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, sizex, sizey, speed):
        super().__init__()
        
        self.image = pygame.Surface([sizex, sizey])
        pygame.draw.rect(self.image, color, [0, 0, sizex, sizey])
        self.rect = self.image.get_rect()
        self.speed = speed
        self.velocity = [speed, randint(-8, 8)]
        
    def bounce(self, player, enemy):
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.velocity[1] *= -1
        elif self.rect.colliderect(player.rect) or self.rect.colliderect(enemy.rect):
            self.velocity[0] *= -1
            self.velocity[1] = randint(-self.speed, self.speed)
    
    def move(self):
        self.rect.centerx += self.velocity[0]
        self.rect.centery += self.velocity[1]
    
    def update(self, player, enemy):
        self.bounce(player, enemy)
        self.move()