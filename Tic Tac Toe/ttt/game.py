from .constants import *
from .board import Board
import pygame
from copy import deepcopy
import time

class Game:
    def __init__(self, win):
        self.win = win
        self.score = {"X": 0, "O": 0}
        self._init()

    def _init(self):
        self.board = Board()
        self.turn = "X"

    def change_turn(self):
        if self.turn == "X":
            self.turn = 'O'
        else:
            self.turn = "X"

    def select(self, click):
        if click is not None:
            row, col = click
            self.put(row, col)
            self.change_turn()

    def put(self, row, col):
        self.board.put_sign(self.turn, row, col)

    def new_game(self, win=False):
        if win:
            self.change_turn()
            self.score[self.turn] += 1

        self._init()

    def check_if_end(self):
        if self.board.winning()[0]:
            #time.sleep(500)
            self.new_game(True)
            return True

        elif self.board.is_draw():
            #time.sleep(500)
            self.new_game(False)
            return True
        return False

    def copy_board(self):
        return deepcopy(self.board.get_board())

    def set_board(self, board):
        self.board.board = board
        self.change_turn()

    def draw(self):
        self.win.fill(BLACK)
        self.draw_lines()
        self.draw_signs()
        self.draw_score()

        pygame.display.update()

    def draw_lines(self):
        for i in range(4):
            # Horizontal
            x_c = SIDE_MARGIN
            y_c = TOP_MARGIN + i * SQUARE_SIZE
            pygame.draw.line(self.win, WHITE, (x_c, y_c), (x_c + 3*SQUARE_SIZE, y_c), 3)

            # Vertical
            x_c = SIDE_MARGIN + i * SQUARE_SIZE
            y_c = TOP_MARGIN
            pygame.draw.line(self.win, WHITE, (x_c, y_c), (x_c, y_c + 3*SQUARE_SIZE), 3)

    def draw_signs(self):

        for row in range(3):
            for col in range(3):
                if self.board.get_sign(row, col) != "":
                    text = SIGN_FONT.render(self.board.get_sign(row, col), True, WHITE)
                    text_rect = text.get_rect(center=(int(SIDE_MARGIN + col * SQUARE_SIZE + SQUARE_SIZE/2),
                                                      int(TOP_MARGIN + row * SQUARE_SIZE + SQUARE_SIZE/2)))

                    self.win.blit(text, text_rect)

    def draw_score(self):
        text = SCORE_FONT.render(f"X: {self.score['X']}  O: {self.score['O']}", True, WHITE)
        self.win.blit(text, (SIDE_MARGIN, BOTTOM_OF_BOARD + 3))
