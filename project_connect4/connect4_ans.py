import random


def check_move(board, turn, col, pop):
    if pop: return board[col] == turn
    else: return board[len(board) - 7 + col] == 0


def apply_move(board, turn, col, pop):
    board = board.copy()
    if pop: board[col : len(board) : 7] = board[col + 7 :: 7] + [0]
    else:
        for i in range(col, len(board), 7):
            if board[i] == 0:
                board[i] = turn
                break
    return board


def check_victory(board, who_played):
    nrows = len(board) // 7
    p1_win = False
    p2_win = False
    for col in range(7):
        curr_token = board[col]
        tokens_in_row = 0
        for row in range(nrows):
            if board[row * 7 + col] == 0: break
            if board[row * 7 + col] != curr_token:
                curr_token = board[row * 7 + col]
                tokens_in_row = 1
            else:
                tokens_in_row += 1
            if tokens_in_row == 4:
                if curr_token == 1: p1_win = True
                elif curr_token == 2: p2_win = True

    for row in range(nrows-1):
        if board[row * 7 + 3] == 0: continue
        curr_token = board[row * 7 + 3]
        tokens_in_row = 1
        for col in range(2, -1, -1):
            if board[row * 7 + col] != curr_token: break
            else: tokens_in_row += 1
        for col in range(4, 7):
            if board[row * 7 + col] != curr_token: break
            else: tokens_in_row += 1
        if tokens_in_row >= 4:
            if curr_token == 1: p1_win = True
            elif curr_token == 2: p2_win = True

        tokens_in_row = 1
        for col in range(1, 4):
            if row * 7 + 3 + col * 6 >= len(board) or board[row * 7 + 3 + col * 6] != curr_token: break
            else:
                tokens_in_row += 1
        for col in range(1, 4):
            if row * 7 + 3 - col * 6 < 0 or board[row * 7 + 3 - col * 6] != curr_token: break
            else: tokens_in_row += 1
        if tokens_in_row >= 4:
            if curr_token == 1: p1_win = True
            elif curr_token == 2: p2_win = True

        tokens_in_row = 1
        for col in range(1, 4):
            if row * 7 + 3 + col * 8 >= len(board) or board[row * 7 + 3 + col * 8] != curr_token: break
            else:
                tokens_in_row += 1
        for col in range(1, 4):
            if row * 7 + 3 - col * 8 < 0 or board[row * 7 + 3 - col * 8] != curr_token: break
            else: tokens_in_row += 1
        if tokens_in_row >= 4:
            if curr_token == 1: p1_win = True
            elif curr_token == 2: p2_win = True

    if p1_win and p2_win: return 3 - who_played
    elif not p1_win and not p2_win: return 0
    elif p1_win: return 1
    elif p2_win: return 2


def computer_move(board, turn, level):
    valid_moves = get_valid_moves(board, turn)

    if level == 1:
        return random.choice(valid_moves)
    elif level == 2:
        winning_moves = get_winning_moves(board, turn)
        if winning_moves: return random.choice(winning_moves)

        ok_moves = get_not_losing_moves(board, turn)
        if ok_moves: return random.choice(ok_moves)
        else: return random.choice(valid_moves)

    return (0, False)


def display_board(board):
    nrows = len(board) // 7
    for row in range(nrows - 1, -1, -1):
        print(board[row * 7 : (row + 1) * 7])


def get_all_moves(board):
    moves = [(col, pop) for col in range(7) for pop in (True, False)]
    return moves


def get_valid_moves(board, turn):
    moves = get_all_moves(board)
    val_moves = [(col, pop) for (col, pop) in moves if check_move(board, turn, col, pop)]
    return val_moves


def get_winning_moves(board, turn):
    valid_moves = get_valid_moves(board, turn)
    win_moves = [(col, pop) for (col, pop) in valid_moves if check_victory(apply_move(board, turn, col, pop), turn) == turn]
    return win_moves


def get_not_losing_moves(board, turn):
    valid_moves = get_valid_moves(board, turn)
    opp = 3 - turn
    ok_moves = [(col, pop) for (col, pop) in valid_moves if not get_winning_moves(apply_move(board, turn, col, pop), opp)]
    return ok_moves


def menu():
    pass


if __name__ == "__main__":
    menu()
