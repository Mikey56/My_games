from copy import deepcopy
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def alpha_beta_pruning(position, depth, max_player, alpha, beta, game):
    if depth == 0 or position.winner() != None:
        return position.evaluation_2(), position

    if max_player:
        max_eval = float("-inf")
        best_move = None

        moves = get_all_moves(position, BLACK, game)
        if moves is None:
            if game.turn == WHITE:
                return -1000, position
            else:
                return 1000, position



        for move in moves:
            evaluation = alpha_beta_pruning(move, depth-1, False, alpha, beta, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

            alpha = max(alpha, max_eval)

            if beta <= alpha:
                break

        return max_eval, best_move

    else:
        min_eval = float("inf")
        best_move = None

        moves = get_all_moves(position, WHITE, game)
        if moves is None:
            if game.turn == BLACK:
                return -1000, position
            else:
                return 1000, position

        for move in moves:
            evaluation = alpha_beta_pruning(move, depth-1, True, alpha, beta, game)[0]
            min_eval = min(min_eval, evaluation)
            beta = min(beta, min_eval)
            if min_eval == evaluation:
                best_move = move
            if beta <= alpha:
                break

        return min_eval, best_move



def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluation_3(), position

    if max_player:
        max_eval = float("-inf")
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move

    else:
        min_eval = float("inf")
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, True, game)[0]
       
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move

        return min_eval, best_move

