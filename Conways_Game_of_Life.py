import pygame
from random import randint
from copy import deepcopy

res = width, height = 1600, 900
cell = 10
w, h = width // cell, height // cell
fps = 10

pygame.init()
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

next_field = [[0 for i in range(w)] for j in range(h)]
current_field = [[randint(0, 1) for i in range(w)] for j in range(h)]


def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw grid
    [pygame.draw.line(surface, pygame.Color('violet'), (x, 0), (x, height)) for x in range(0, width, cell)]
    [pygame.draw.line(surface, pygame.Color('violet'), (0, y), (width, y)) for y in range(0, height, cell)]
    # draw life
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('violet'), (x * cell + 2, y * cell + 2, cell - 2, cell - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)

    pygame.display.flip()
    clock.tick(fps)
