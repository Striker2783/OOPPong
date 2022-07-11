import pygame

from Classes import Ball, Background, Paddle, Score

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Pong")
icon = pygame.image.load("Graphics/Pong Icon.png")
pygame.display.set_icon(icon)

player_paddle = Paddle.PlayerPaddle(position=("midleft", (10, 300)))
enemy_paddle = Paddle.EnemyPaddle(speed=8, position=("midright", (890, 300)))
ball = Ball.Ball()
player_score = Score.Score(font_size=80, position=("center", (450, 50)))
enemy_score = Score.Score(font_size=80, position=("center", (550, 50)))
back_line = Background.Background(size=(5, 600), position=("center", (450, 300)))
back_line.image.set_alpha(50)

sprites = pygame.sprite.Group()
sprites.add(player_paddle)
sprites.add(enemy_paddle)
sprites.add(ball)
sprites.add(back_line)
sprites.add(player_score, enemy_score)

clock = pygame.time.Clock()


def score(scorer):
    if scorer == "player":
        pass
    elif scorer == "enemy":
        pass


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
