import pygame
from .constants import BLACK, WHITE, ROWS, COLS, SQUARE_SIZE, \
                       WHITE_CUBE, BLACK_CUBE, BACKGROUND, SIDE_MARGIN, TOP_MARGIN, \
                       wood_black, wood_white

from .piece import Piece

class Board:
    # wood_black = pygame.image.load("checkers/Images/extras/wood_dark.png")
    # wood_white = pygame.image.load("checkers/Images/extras/wood_white.png")

    def __init__(self):
        self.board = self._load_pieces()
        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0

    # Check if some player has already won
    def winner(self):
        if self.white_left <= 0:
            return WHITE
        elif self.black_left <= 0:
            return BLACK
        else:
            return None

    # Move piece to a new position, check if it hasn't became a king
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col],self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS -1 or row == 0:
            piece.set_king()
            if piece.color == BLACK:
                self.black_kings += 1
            else:
                self.white_kings += 1

    # Load new piece during initialization
    def _load_pieces(self):
        pieces = []

        for r in range(ROWS):
            pieces.append([])
            for c in range(COLS):
                if (r+c) % 2 == 0:
                    if r < 3:
                        pieces[r].append(Piece(r, c, WHITE))
                    elif r > 4:
                        pieces[r].append(Piece(r, c, BLACK))
                    else:
                        pieces[r].append(0)

                else:
                    pieces[r].append(0)

        return pieces

    # Draw cubes in grid
    def draw_cubes(self, win: pygame.Surface):
        win.fill(BACKGROUND)
        for row in range(ROWS):
            for col in range(COLS):
                pos = (col * SQUARE_SIZE + SIDE_MARGIN,
                       row * SQUARE_SIZE + TOP_MARGIN,
                       SQUARE_SIZE, SQUARE_SIZE)

                if (row + col) % 2 == 0:
                    #pygame.draw.rect(win, BLACK, (SIDE_MARGIN + row * SQUARE_SIZE,
                    #                           TOP_MARGIN + col * SQUARE_SIZE,
                    #                              SQUARE_SIZE, SQUARE_SIZE))

                    win.blit(wood_black, (SIDE_MARGIN + row * SQUARE_SIZE,
                                               TOP_MARGIN + col * SQUARE_SIZE))
                else:
                    #pygame.draw.rect(win, WHITE, (SIDE_MARGIN + row * SQUARE_SIZE,
                    #                              TOP_MARGIN + col * SQUARE_SIZE,
                    #                              SQUARE_SIZE, SQUARE_SIZE))
                    win.blit(wood_white, (SIDE_MARGIN + row * SQUARE_SIZE,
                                               TOP_MARGIN + col * SQUARE_SIZE))

    # Draw all pieces
    def draw_pieces(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(win)

    # Draw everything
    def draw(self, win):
        self.draw_cubes(win)
        self.draw_pieces(win)

    def get_piece(self, row, col):
        return self.board[row][col]

    # For given piece it returns all valid moves
    def get_valid_moves(self, piece):
        moves = {}

        left  = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # If given color is BLACK it means it moves down, same for king for the opposite color
        if piece.color == BLACK or piece.is_king:
            # Go left down
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))
            # Go right down
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.is_king:
            # Go right up
            moves.update(self._traverse_right(row + 1, min(row+3, ROWS), 1, piece.color, right))
            # Go left up
            moves.update(self._traverse_left(row + 1, min(row+3, ROWS), 1, piece.color, left))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        # Check just 2 next cubes, on the left side of the given piece
        for r in range(start, stop, step):

            # If is out of the board break
            if left < 0:
                break

            current = self.board[r][left]
            # If current piece is empty
            if current == 0:
                if skipped and not last:
                    break
                # If we have already jumped over some pieces (skipped) and we jump over one
                # more (lest) and the next one is empty add it to moves we skipped pieces
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                # If we jumped over a piece and the next one is empty, we check
                # if we can do another jump on the left side and right side
                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                        r_new = min(r + 3, ROWS)
                    else:
                        row = min(r + 3, ROWS)
                        r_new = max(r - 3, -1)

                    if skipped:
                        moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=skipped + last))
                        moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=skipped + last))

                        # New back jump
                        moves.update(
                            self._traverse_left(r - step, r_new, step * (-1), color, left - 1, skipped=skipped + last))
                    else:
                        moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                        moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))

                        # New back jump
                        moves.update(self._traverse_left(r - step, r_new, step * (-1), color, left - 1, skipped=last))

                break

            elif current.color == color:
                break

            else:
                last = [current]

            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):

            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                        r_new = min(r + 3, ROWS)
                    else:
                        row = min(r + 3, ROWS)
                        r_new = max(r - 3, -1)

                    if skipped:
                        moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=skipped + last))
                        moves.update(
                            self._traverse_right(r + step, row, step, color, right + 1, skipped=skipped + last))

                        # New jump
                        moves.update(self._traverse_right(r - step, r_new, step * (-1), color, right + 1,
                                                          skipped=skipped + last))
                    else:
                        moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                        moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))

                        # New jump
                        moves.update(self._traverse_right(r - step, r_new, step * (-1), color, right + 1, skipped=last))

                break

            elif current.color == color:
                break

            else:
                last = [current]

            right += 1

        return moves

    # Remove all pieces from list, update the number of lest pieces and kings
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0

            if piece != 0:
                if piece.color == WHITE:
                    if piece.is_king:
                        self.white_kings -= 1
                    self.white_left -= 1
                else:
                    if piece.is_king:
                        self.black_kings -= 1
                    self.black_left -= 1

    # Get all pieces of given color
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)

        return pieces

    def is_only_kings(self):
        if self.white_left == self.white_kings and self.black_left == self.black_kings:
            return True
        return False

    # Evaluation functions, BLACK is MAXIMIZER

    # Piece to value
    def evaluation_1(self):
        return (self.black_left - self.black_kings) - \
               (self.white_left - self.white_kings) + \
               (self.black_kings - self.white_kings) * 2

    # Piece & Board part of value
    def evaluation_2(self):
        # Pawn in the opponent's half of the board value = 7
        # Pawn in the player's half of the board value = 5
        # King's value = 10

        black_pieces = self.get_all_pieces(BLACK)
        black_value = 0

        for piece in black_pieces:
            if piece.is_king:
                black_value += 10
            elif piece.row >= 3:
                black_value += 5
            elif piece.row <= 4:
                black_value += 7

        white_pieces = self.get_all_pieces(WHITE)
        white_value = 0
        for piece in white_pieces:
            if piece.is_king:
                white_value += 10
            elif piece.row <= 3:
                white_value += 5
            elif piece.row >= 4:
                white_value += 7

        return black_value - white_value

    # Piece & Row to value
    def evaluation_3(self):
        # Pawn's value: 5 + row number
        # King's value: 7 + num. of rows

        black_pieces = self.get_all_pieces(BLACK)
        black_value = 0
        for piece in black_pieces:
            if piece.is_king:
                black_value += 15
            else:
                black_value += 6 + piece.row

        white_pieces = self.get_all_pieces(WHITE)
        white_value = 0
        for piece in white_pieces:
            if piece.is_king:
                white_value += 15
            else:
                white_value += 6 + piece.row

        return black_value - white_value


