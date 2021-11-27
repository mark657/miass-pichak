import pygame
import random
import sys


COLORS = (pygame.Color('red'), pygame.Color('green'), pygame.Color('blue'))


def draw(screen, circle_with, num):
    radius = circle_with * num
    circle_pos = (radius, radius)
    while num > 0:
        pygame.draw.circle(screen, COLORS[num % 3], circle_pos, radius, 0)
        num -= 1
        radius = circle_with * num


def main():
    pygame.init()
    pygame.display.set_caption('mishen')
    try:
        circle_wight, num = [int(i) for i in input().split()]
    except ValueError:
        print('Неправильный формат ввода')
        return -1
    size = (circle_wight * num * 2, circle_wight * num * 2)
    screen = pygame.display.set_mode(size)
    draw(screen,circle_wight, num)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
