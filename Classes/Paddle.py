import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, sizex, sizey, speed):
        super().__init__()
        
        self.image = pygame.Surface((sizex, sizey))
        pygame.draw.rect(self.image, color, [0, 0, sizex, sizey])
        self.rect = self.image.get_rect()
        self.speed = speed


class PlayerPaddle(Paddle):
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[1] < self.rect.centery:
            self.rect.centery -= min(self.speed, self.rect.centery - mouse_pos[1])
        elif mouse_pos[1] > self.rect.centery:
            self.rect.centery += min(self.speed, mouse_pos[1] - self.rect.centery)

class EnemyPaddle(Paddle):
    def update(self, ball):
        if ball.rect.centery < self.rect.centery:
            self.rect.centery -= min(self.speed, self.rect.centery - ball.rect.centery)
        elif ball.rect.centery > self.rect.y:
            self.rect.centery += min(self.speed, ball.rect.centery - self.rect.centery)
