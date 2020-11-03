from .constants import ROWS, COLS, WINNING_POS_7, WINNING_POS_6, WINNING_POS_5, WINNING_POS_4, GREY_LIGHT, GREY_DARK, SQUARE_SIZE, PIECE_RADIUS, WIDTH, HEIGHT, RED, YELLOW
import pygame
from pygame import gfxdraw


class Board:

    def __init__(self):
        self._load_board()

    def _load_board(self):
        self.board = []
        self.load = dict()
        for r in range(ROWS):
            self.board.append([])
            for c in range(COLS):
                self.board[r].append("")
                self.load[c] = 0

    def print_board(self):
        for row in self.board:
            print(row)

    def get_piece(self, row, col):
        return self.board[row][col]

    def set_piece(self, piece, col):
        self.board[ROWS-1-self.load[col]][col] = piece
        self.load[col] += 1

    def get_last_row(self, col):
        return self.load[col]

    def get_col_to_list(self, col):
        new_col = []
        for row in range(ROWS):
            new_col.append(self.board[row][col])

        return new_col

    def get_diag_to_list(self, row, left=True):
        new_diag = []
        if left:
            if row < 3:
                for i in range(ROWS-row):
                    new_diag.append(self.get_piece(row+i, i))
                return new_diag
            else:
                for i in range(row+1):
                    new_diag.append(self.get_piece(row-i, i))
                return new_diag

        else:
            if row < 3:
                for i in range(ROWS-row):
                    new_diag.append(self.get_piece(row+i, COLS-i-1))
                return new_diag
            else:
                for i in range(row+1):
                    new_diag.append(self.get_piece(row-i, COLS-i-1))
                return new_diag

    def _helper_if_win(self, lst):
        if len(lst) == 4:
            win_list = WINNING_POS_4
        elif len(lst) == 5:
            win_list = WINNING_POS_5
        elif len(lst) == 6:
            win_list = WINNING_POS_6

        temp_row = lst.copy()
        temp_row = [True if e == "R" else False for e in temp_row]
        if temp_row in win_list:
            return True, "R"

        temp_row = [True if e == "Y" else False for e in temp_row]
        if temp_row in win_list:
            return True, "Y"

        return False, ""

    def check_if_win(self):
        # ROWS
        for row in range(ROWS):

            # Check RED
            temp_row = self.board[row].copy()
            temp_row = [True if e == "R" else False for e in temp_row]
            if temp_row in WINNING_POS_7:
                return True, "R"

            # Check YELLOW
            temp_row = self.board[row].copy()
            temp_row = [True if e == "Y" else False for e in temp_row]
            if temp_row in WINNING_POS_7:
                return True, "Y"

        # COLS
        for col in range(COLS):
            temp_row = self.get_col_to_list(col)
            # Check RED
            temp_row = [True if e == "R" else False for e in temp_row]
            if temp_row in WINNING_POS_6:
                return True, "R"

            # Check YELLOW
            self.get_col_to_list(col)
            temp_row = [True if e == "Y" else False for e in temp_row]
            if temp_row in WINNING_POS_6:
                return True, "Y"

        # DIAG
        for row in range(ROWS):
            # Left
            res = self._helper_if_win(self.get_diag_to_list(row, True))
            if res[0]:
                return res

            # Left
            res = self._helper_if_win(self.get_diag_to_list(row, False))
            if res[0]:
                return res

        return False, ""

    def draw_grid(self, win: pygame.Surface):
        win.fill(GREY_LIGHT)

        # Draw lines
        for r in range(1, COLS):
            pygame.draw.line(win, GREY_DARK, (SQUARE_SIZE * r, 0), (SQUARE_SIZE * r, HEIGHT), 5)

            if r < COLS-1:
                pygame.draw.line(win, GREY_DARK, (0, SQUARE_SIZE * r), (WIDTH, SQUARE_SIZE * r), 5)

    def draw_pieces(self, win):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece == "":
                    self._draw_circle(win, int(SQUARE_SIZE * x + SQUARE_SIZE/2),
                                      int(SQUARE_SIZE * y + SQUARE_SIZE/2), GREY_DARK)
                elif piece == "R":
                    self._draw_circle(win, int(SQUARE_SIZE * x + SQUARE_SIZE / 2),
                                      int(SQUARE_SIZE * y + SQUARE_SIZE / 2), RED)
                else:
                    self._draw_circle(win, int(SQUARE_SIZE * x + SQUARE_SIZE / 2),
                                      int(SQUARE_SIZE * y + SQUARE_SIZE / 2), YELLOW)

    def _draw_circle(self, win, x, y, color):
        pygame.gfxdraw.filled_circle(win, x, y, PIECE_RADIUS, color)
        pygame.gfxdraw.aacircle(win, x, y, PIECE_RADIUS, color)

    def draw_temp_piece(self, win):
        pass




