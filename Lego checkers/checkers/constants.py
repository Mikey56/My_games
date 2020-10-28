import pygame

WIDTH, HEIGHT = 900, 1000
ROWS, COLS = 8, 8
SQUARE_SIZE = 90
SIDE_MARGIN = (WIDTH - COLS * SQUARE_SIZE) / 2
TOP_MARGIN = SIDE_MARGIN
BOTTOM_OF_BOARD = TOP_MARGIN + ROWS * SQUARE_SIZE

# RGB
WHITE_CUBE = (128, 128, 128)
BLACK_CUBE = (0, 0, 0)

BACKGROUND = (255, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

wood_black = pygame.image.load("checkers/Images/extras/wood_dark.png")
wood_white = pygame.image.load("checkers/Images/extras/wood_white.png")

# Images
img_king_1 = pygame.image.load(f"checkers/Images/Team_1/img_king.png")
img_king_2 = pygame.image.load(f"checkers/Images/Team_2/img_king.png")

images_1 = [pygame.image.load(f"checkers/Images/Team_1/img_1.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_2.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_3.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_4.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_5.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_6.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_7.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_8.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_9.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_10.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_11.png"),
            pygame.image.load(f"checkers/Images/Team_1/img_12.png")]

images_2 = [pygame.image.load(f"checkers/Images/Team_2/img_1.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_2.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_3.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_4.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_5.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_6.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_7.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_8.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_9.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_10.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_11.png"),
            pygame.image.load(f"checkers/Images/Team_2/img_12.png")]

img_1_1 = pygame.image.load(f"checkers/Images/Team_1/img_1.png")
img_2_1 = pygame.image.load(f"checkers/Images/Team_1/img_2.png")
img_3_1 = pygame.image.load(f"checkers/Images/Team_1/img_3.png")
img_4_1 = pygame.image.load(f"checkers/Images/Team_1/img_4.png")
img_5_1 = pygame.image.load(f"checkers/Images/Team_1/img_5.png")
img_6_1 = pygame.image.load(f"checkers/Images/Team_1/img_6.png")
img_7_1 = pygame.image.load(f"checkers/Images/Team_1/img_7.png")
img_8_1 = pygame.image.load(f"checkers/Images/Team_1/img_8.png")
img_9_1 = pygame.image.load(f"checkers/Images/Team_1/img_9.png")
img_10_1 = pygame.image.load(f"checkers/Images/Team_1/img_10.png")
img_11_1 = pygame.image.load(f"checkers/Images/Team_1/img_11.png")
img_12_1 = pygame.image.load(f"checkers/Images/Team_1/img_12.png")

img_1_2 = pygame.image.load(f"checkers/Images/Team_2/img_1.png")
img_2_2 = pygame.image.load(f"checkers/Images/Team_2/img_2.png")
img_3_2 = pygame.image.load(f"checkers/Images/Team_2/img_3.png")
img_4_2 = pygame.image.load(f"checkers/Images/Team_2/img_4.png")
img_5_2 = pygame.image.load(f"checkers/Images/Team_2/img_5.png")
img_6_2 = pygame.image.load(f"checkers/Images/Team_2/img_6.png")
img_7_2 = pygame.image.load(f"checkers/Images/Team_2/img_7.png")
img_8_2 = pygame.image.load(f"checkers/Images/Team_2/img_8.png")
img_9_2 = pygame.image.load(f"checkers/Images/Team_2/img_9.png")
img_10_2 = pygame.image.load(f"checkers/Images/Team_2/img_10.png")
img_11_2 = pygame.image.load(f"checkers/Images/Team_2/img_11.png")
img_12_2 = pygame.image.load(f"checkers/Images/Team_2/img_12.png")

