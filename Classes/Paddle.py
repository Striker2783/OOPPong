import pygame

WHITE = (255, 255, 255)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color=WHITE, size=(10, 50), speed=10, position=("center", (0, 0))):
        super().__init__()
        
        self.image = pygame.Surface(size)
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        self.rect = self.image.get_rect()
        self.rect.__setattr__(position[0], position[1])
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
