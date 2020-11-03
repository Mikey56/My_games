import pygame
from ttt.game import Game
from ttt.constants import SIZE, WIDTH, HEIGHT, SQUARE_SIZE, SIDE_MARGIN, TOP_MARGIN, BOTTOM_OF_BOARD
from minimax.algorithm import minimax, evaluation
import copy

FPS = 60
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic Tac Toe")

def get_row_col(pos):
    x, y = pos

    if SIDE_MARGIN <= x <= WIDTH-SIDE_MARGIN or TOP_MARGIN <= y <= BOTTOM_OF_BOARD:
        return (y-TOP_MARGIN) // SQUARE_SIZE, (x-SIDE_MARGIN) // SQUARE_SIZE
    else:
        return None

def main():
    #print(evaluation([['X', 'O', 'X'], ['O', 'X', 'O'], ['X', '', '']]))
    clock = pygame.time.Clock()

    game = Game(WIN)



    run = True
    while run:
        z = game.check_if_end()
        # print(game.copy_board())
        if z:
            print(game.score)
            pygame.time.wait(500)
        if game.turn == "O":
            x = minimax(game.copy_board(), True, 1)[1]

            game.set_board(x)





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                game.select(get_row_col(pygame.mouse.get_pos()))

        game.draw()



if __name__ == "__main__":
    main()