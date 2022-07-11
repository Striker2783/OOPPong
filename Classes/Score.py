import pygame

WHITE = (255, 255, 255)


class Score(pygame.sprite.Sprite):
    def __init__(self, color=WHITE, font="Fonts/Arial.ttf", font_size=10, score=0, position=("center", (0, 0))):
        super().__init__()
        self.score = score
        font_object = pygame.font.Font(font, font_size)
        self.image = font_object.render(str(self.score), True, color)
        test = pygame.Surface((0, 0))
        rect = pygame.draw.rect(test, color, [0, 0, 0, 0])
        self.rect = rect
        self.rect.__setattr__(position[0], position[1])
        print(rect)
