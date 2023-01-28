import pygame


class Cuadrado:
    def __init__(self, x, y, size, color, vel=1):
        self.x = 0
        self.y = 0
        self.surface = pygame.Surface((size, size))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center=(x, y))
        self.transform = lambda: (x + self.x, y - self.y)
        self.vel = 1

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def check(self, screen):
        if (
            self.rect.right >= screen.get_width() or
            self.rect.left <= 0 or
            self.rect.bottom >= screen.get_height() or
            self.rect.top <= 0
        ):
            self.vel *= -1

    def move(self, func):
        self.x += self.vel
        self.y = func(self.x)
        self.rect.center = self.transform()
