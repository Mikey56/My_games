from copy import deepcopy

def evaluation(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            if board[i][0] == "X":
                return -1
            else:
                return 1

        if board[0][i] == board[1][i] == board[2][i] != "":
            if board[0][i] == "X":
                return -1
            else:
                return 1

    if board[0][0] == board[1][1] == board[2][2] != "":
        if board[0][0] == "X":
            return -1
        else:
            return 1

    if board[0][2] == board[1][1] == board[2][0] != "":
        if board[0][2] == "X":
            return -1
        else:
            return 1

    return 0

def end(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                return False
    return True

def get_all_moves(board):
    moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                moves.append((r, c))
    return moves

def simulate_move(board, move, sign):
    board[move[0]][move[1]] = sign

def minimax(board, max_player, depth):
    x = evaluation(board)
    if x != 0:
        return x, board
    if end(board):
        return 0, board


    if max_player:
        max_eval = float("-inf")
        best_board = None

        for move in get_all_moves(board):
            new_board = deepcopy(board)
            simulate_move(new_board, move, "O")

            score = minimax(new_board, False, depth+1)[0]
            max_eval = max(max_eval, score)

            if max_eval == score:
                best_board = deepcopy(new_board)

        #print((max_eval, best_board))
        return max_eval, best_board

    else:
        min_eval = float("inf")
        best_board = None

        for move in get_all_moves(board):
            new_board = deepcopy(board)
            simulate_move(new_board, move, "X")

            score = minimax(new_board, True, depth+1)[0]
            min_eval = min(min_eval, score)

            if min_eval == score:
                best_board = deepcopy(new_board)

        return min_eval, best_board


