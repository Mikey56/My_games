import pygame
from .constants import *

class Board:

    def __init__(self):
        self._load_board()

    # Load empty board
    def _load_board(self):
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]

    def get_sign(self, row, col):
        return self.board[row][col]

    # Check if on current state of board somebody won
    def winning(self):
        for r in range(3):
            # Horizontal
            if self.board[r][0] == self.board[r][1] == self.board[r][2] and self.board[r][0] != "":
                if self.board[r][0] == "X":
                    return True, "X"
                else:
                    return True, "O"

            # Vertical
            if self.board[0][r] == self.board[1][r] == self.board[2][r] and self.board[0][r] != "":
                if self.board[0][r] == "X":
                    return True, "X"
                else:
                    return True, "O"

        # Diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[1][1] != "":
            if self.board[1][1] == "X":
                return True, "X"
            else:
                return True, "O"

        if self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[1][1] != "":
            if self.board[1][1] == "X":
                return True, "X"
            else:
                return True, "O"

        return False, ""

    # Put sign in given place
    def put_sign(self, sign, row, col):
        if self.board[row][col] != "":
            return False

        if not (sign == "X" or sign == "O"):
            return False

        self.board[row][col] = sign
        return True

    # Returns all valid moves
    def get_valid_moves(self):
        moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    moves.append((r, c))

        return moves

    # Return valid moves, if there are none return False
    def valid_moves(self):
        moves = self.get_valid_moves()
        if len(moves) > 0:
            return moves
        else:
            return False

    # Check if is draw
    def is_draw(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    return False
        return True

    def print_board(self):
        for r in range(3):
            print(self.board[r])

    def get_board(self):
        return self.board

    def evaluate(self):
        result = self.winning()
        if not result[0]:
            return 0
        elif result[1] == "X":
            return -1
        elif result[1] == "O":
            return 1