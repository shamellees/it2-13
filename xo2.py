import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_SIZE = 3
SPACE = WIDTH // BOARD_SIZE
BACKGROUND_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики нолики')
