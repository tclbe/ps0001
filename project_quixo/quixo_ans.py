import random


def check_move(board, turn, index, push_from):
    n = int(len(board)**0.5)
    r = index // n
    c = index % n

    if 0 < r < n - 1 and 0 < c < n - 1: return False
    if board[index] == 3 - turn: return False
    if r == 0 and push_from == 'T': return False
    if r == n - 1 and push_from == 'B': return False
    if c == 0 and push_from == 'L': return False
    if c == n - 1 and push_from == 'R': return False

    return True


def apply_move(board, turn, index, push_from):
    board = board[:]
    n = int(len(board)**0.5)
    r = index // n
    c = index % n

    if push_from == "T":
        blocks = [turn] + board[c:index:n]
        board[c:index + n:n] = blocks[:]
    elif push_from == "B":
        blocks = board[index + n::n] + [turn]
        board[index::n] = blocks[:]
    elif push_from == "L":
        blocks = [turn] + board[r * n:index]
        board[r * n:index + 1] = blocks[:]
    elif push_from == "R":
        blocks = board[index + 1:(r + 1) * n] + [turn]
        board[index:(r + 1) * n] = blocks[:]

    return board


def check_victory(board, who_played):
    n = int(len(board)**0.5)
    rows = [board[r * n:(r + 1) * n] for r in range(n)]
    cols = [board[c::n] for c in range(n)]
    diags = [board[::n + 1]] + [board[::n - 1][1:-1]]
    all_ways = rows + cols + diags

    p1_win = any(all(x == 1 for x in way) for way in all_ways)
    p2_win = any(all(x == 2 for x in way) for way in all_ways)

    if p1_win and p2_win: return 3 - who_played
    elif not p1_win and not p2_win: return 0
    elif p1_win: return 1
    elif p2_win: return 2


def computer_move(board, turn, level, depth=0, max_depth=1):
    valid_moves = get_valid_moves(board, turn)

    if level == 1:
        return random.choice(valid_moves)
    elif level == 2:
        # winning_moves = get_winning_moves(board, turn)
        # if winning_moves: return random.choice(winning_moves)

        # ok_moves = get_not_losing_moves(board, turn)
        # if ok_moves: return random.choice(ok_moves)
        # else: return random.choice(valid_moves)

        if depth > max_depth: return random.choice(valid_moves)

        winning_moves = get_winning_moves(board, turn)
        if winning_moves: return random.choice(winning_moves)

        opp = 3 - turn

        random.shuffle(valid_moves)
        for i, d in valid_moves:
            board_post_move = apply_move(board, turn, i, d)
            opp_i, opp_d = computer_move(board_post_move, opp, 2, depth + 1,
                                         max_depth)
            if check_victory(apply_move(board_post_move, opp, opp_i, opp_d),
                             opp) != opp:
                return i, d

        if valid_moves: return random.choice(valid_moves)

    return (0, 'B')


def get_all_moves(board):
    n = int(len(board)**0.5)
    moves = [(i, d) for i in range(n**2) for d in "TBLR"]
    return moves


def get_valid_moves(board, turn):
    moves = get_all_moves(board)
    val_moves = [(i, d) for (i, d) in moves if check_move(board, turn, i, d)]
    return val_moves


def get_winning_moves(board, turn):
    valid_moves = get_valid_moves(board, turn)
    win_moves = [(i, d) for (i, d) in valid_moves
                 if check_victory(apply_move(board, turn, i, d), turn) == turn]
    return win_moves


def get_not_losing_moves(board, turn):
    valid_moves = get_valid_moves(board, turn)
    opp = 3 - turn
    ok_moves = [(i, d) for (i, d) in valid_moves
                if not get_winning_moves(apply_move(board, turn, i, d), opp)]
    return ok_moves


def display_board(board):
    n = int(len(board)**0.5)

    tiles = {0: ".", 1: "O", 2: "X"}

    for i, val in enumerate(board):
        if i % n == 0 and i > 0: print()
        print(tiles[val], end="")

    print()


def menu():
    # implement your function here
    pass


if __name__ == "__main__":
    menu()
