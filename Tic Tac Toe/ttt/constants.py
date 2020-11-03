import pygame

pygame.font.init()

# Setup
SIZE = WIDTH, HEIGHT = (700, 800)
SIDE_MARGIN = 15
TOP_MARGIN = 25
SQUARE_SIZE = int((WIDTH - 2*SIDE_MARGIN) / 3)
BOTTOM_OF_BOARD = TOP_MARGIN + 3 * SQUARE_SIZE

# RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font
SIGN_FONT = pygame.font.SysFont("comicsans", 300)
SCORE_FONT = pygame.font.SysFont("comicsans", 60)


