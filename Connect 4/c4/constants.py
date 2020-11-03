
SIZE = WIDTH, HEIGHT = 700, 600
SQUARE_SIZE = int(WIDTH / 7)
PIECE_RADIUS = int((SQUARE_SIZE - 10) / 2 - 5)
ROWS, COLS = 6, 7

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY_LIGHT = (180, 180, 180)
GREY_DARK = (128, 128, 128)

WINNING_POS_7 = [[True, True, True, True, False, False, False],
                 [False, True, True, True, True, False, False],
                 [False, False, True, True, True, True, False],
                 [False, False, False, True, True, True, True]]

WINNING_POS_6 = [[True, True, True, True, False, False],
                 [False, True, True, True, True, False],
                 [False, False, True, True, True, True]]

WINNING_POS_5 = [[False, True, True, True, True],
                 [True, True, True, True, False]]

WINNING_POS_4 = [[True, True, True, True]]

