import pygame
from Classes import Ball, Background, Paddle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Pong")

player_paddle = Paddle.PlayerPaddle(WHITE, 10, 50, 10)
enemy_paddle = Paddle.EnemyPaddle(WHITE, 10, 50, 8)
ball = Ball.Ball(WHITE, 10, 10, 10)
back_line = Background.Background(WHITE, 5, 600)
back_line.image.set_alpha(50)

player_paddle.rect.midleft = (10, 300)
enemy_paddle.rect.midright = (890, 300)
ball.rect.center = (450, 300)
back_line.rect.center = (450, 300)

sprites = pygame.sprite.Group()
sprites.add(player_paddle)
sprites.add(enemy_paddle)
sprites.add(ball)
sprites.add(back_line)

clock = pygame.time.Clock()

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
while True:
    events()
    
    player_paddle.update()
    enemy_paddle.update(ball)
    ball.update(player_paddle, enemy_paddle)
    
    screen.fill(BLACK)
    sprites.draw(screen)
    pygame.display.flip()
    
    clock.tick(60)