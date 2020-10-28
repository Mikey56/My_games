import pygame
from checkers.constants import WIDTH, HEIGHT, WHITE, BLACK, SIDE_MARGIN, \
    TOP_MARGIN, BOTTOM_OF_BOARD, SQUARE_SIZE
from checkers.piece import Piece
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax, alpha_beta_pruning
import time

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lego Checkers")


def get_row_col_from_mouse(pos):
    x, y = pos

    if (SIDE_MARGIN < x < WIDTH - SIDE_MARGIN) and TOP_MARGIN < y < BOTTOM_OF_BOARD:
        return int((x - SIDE_MARGIN) // SQUARE_SIZE), int((y - TOP_MARGIN) // SQUARE_SIZE)


def main_AI_vs_AI():
    clock = pygame.time.Clock()
    game = Game(WIN)

    run = True
    while run:
        clock.tick(FPS)
        game.update()

        if game.turn == WHITE:
            value, new_board = alpha_beta_pruning(game.get_board(), 3, False, float("-inf"), float("inf"), game)
            if new_board is None:
                print('WOOOW')
                time.sleep(5000)
            game.ai_move(new_board)

        else:
            value, new_board = alpha_beta_pruning(game.get_board(), 3, True, float("-inf"), float("inf"), game)
            if new_board is None:
                print('WOOOW')
                time.sleep(5000)
            game.ai_move(new_board)

        if game.winner() != None:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

def main_Human_vs_AI():
    clock = pygame.time.Clock()
    game = Game(WIN)

    run = True
    while run:
        clock.tick(FPS)
        game.update()

        if game.turn == WHITE:
            value, new_board = alpha_beta_pruning(game.get_board(), 3, False, float("-inf"), float("inf"), game)
            game.ai_move(new_board)

        if game.winner() != None:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = get_row_col_from_mouse(pygame.mouse.get_pos())
                if x is not None:
                    game.select(x[1], x[0])

    pygame.quit()

def main_Human_vs_Human():
    clock = pygame.time.Clock()
    game = Game(WIN)

    run = True
    while run:
        clock.tick(FPS)
        game.update()

        if game.winner() != None:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = get_row_col_from_mouse(pygame.mouse.get_pos())
                if x is not None:
                    game.select(x[1], x[0])

    pygame.quit()


def main():
    clock = pygame.time.Clock()

    game = Game(WIN)

    run = True
    while run:
        clock.tick(FPS)
        game.update()

        if game.winner() != None:
            run = False

        if game.turn == WHITE:
            value, new_board = alpha_beta_pruning(game.get_board(), 3, False, float("-inf"), float("inf"), game)
            if new_board is None:
                print("WUT")
                time.sleep(5000)
            game.ai_move(new_board)
        # else:
        #     value, new_board = alpha_beta_pruning(game.get_board(), 3, True, float("-inf"), float("inf"), game)
        #     if new_board is None:
        #         print("WUT")
        #         print("WUT")
        #         time.sleep(5000)
        #     game.ai_move(new_board)



        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = get_row_col_from_mouse(pygame.mouse.get_pos())
                if x is not None:
                    game.select(x[1], x[0])
                    print(f"1: {game.board.evaluation_1()}")
                    print(f"2: {game.board.evaluation_2()}")
                    print(f"3: {game.board.evaluation_3()}")


    pygame.quit()


if __name__ == "__main__":
    main_Human_vs_Human()
    #main_Human_vs_AI()
    #main_AI_vs_AI()



