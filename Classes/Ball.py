from random import randint

import pygame

WHITE = (255, 255, 255)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color=WHITE, size=(10, 10), speed=10, position=("center", (450, 300))):
        super().__init__()
        self.position = position
        self.image = pygame.Surface(size)
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        self.rect = self.image.get_rect()
        self.rect.__setattr__(position[0], position[1])
        self.speed = speed
        self.velocity = [speed, randint(-8, 8)]
    
    def bounce(self, player, enemy):
        from main import score
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.velocity[1] *= -1
        elif self.rect.colliderect(player.rect) or self.rect.colliderect(enemy.rect):
            self.velocity[0] *= -1
            self.velocity[1] = randint(-self.speed, self.speed)
        elif self.rect.centerx >= 900:
            score("player")
        elif self.rect.centerx <= 0:
            score("enemy")
    
    def move(self):
        self.rect.centerx += self.velocity[0]
        self.rect.centery += self.velocity[1]
    
    def update(self, player, enemy):
        self.bounce(player, enemy)
        self.move()
        
    def reset(self):
        self.rect.__setattr__(self.position[0], self.position[1])