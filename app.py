import pygame
import math
import sys
from Cuadrado import Cuadrado

WIDTH = 800
HEIGHT = 600
FPS = 60
PLAYER_SIZE = 16
WHITE = (255, 255, 255)


def f1(x: int) -> int:
    return 2 * x - 4


def f2(x: int) -> int:
    return x ** 2 - x + 3


def f3(x: int) -> int:
    return math.cos(x)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Cuadrado(WIDTH // 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    # Seleccionar la función a dibujar
    player.move(f1)
    player.check(screen)
    player.draw(screen)

    clock.tick(FPS)

    pygame.display.flip()
