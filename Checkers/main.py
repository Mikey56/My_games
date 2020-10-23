import pygame
from checkers.constant import WIDTH, HEIGHT, SQUARE_SIZE
#from .checkers.board import Board
from checkers.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers AI")

def get_row_col_from_mouse(pos):
    x, y = pos

    return y // SQUARE_SIZE, x // SQUARE_SIZE


def main():
    clock = pygame.time.Clock()
    game = Game(WIN)

    run = True
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()


    pygame.quit()


if __name__ == "__main__":
    main()


