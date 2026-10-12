from connect4_ans import *
import random


def get_random_valid_move(board, turn):
    val_moves = get_valid_moves(board, turn)
    return random.choice(val_moves)

def generate_board(nrows):
    board = random.choices((0, 1, 2), weights=(7,2,2), k=nrows*7)
    return push_tiles_down(board)

def push_tiles_down(board):
    nrows = len(board)//7
    for col in range(7):
        row = 0
        while row < nrows-1:
            if board[row*7 + col] == 0 and board[(row+1)*7 + col] != 0:
                board[row*7 + col], board[(row+1)*7 + col] = board[(row+1)*7 + col], board[row*7 + col]
                if row > 0: row -= 1
                continue
            row += 1

    return board

def undo_move(board, turn, col, pop):
    board = board.copy()
    if pop:
        board[col+7:len(board):7] = board[col:len(board)-7:7]
        board[col] = turn
    else:
        for row in range(len(board)//7 - 1, -1, -1):
            if board[row*7+col] == turn:
                board[row*7+col] = 0
                break
    return board

def make_board_less_winning(board):    
    for i in range(len(board)):
        if random.random() < 0.4: board[i] = 0
    
    return push_tiles_down(board)

def generate_near_win_board(nrow):
    board = [0 for _ in range(nrow*7)]
    
    turn = random.randint(1, 2)
    while check_victory(board, turn) == 0:
        col, pop = computer_move(board, turn, 2)
        board = apply_move(board, turn, col, pop)
        if check_victory(board, turn) != 0:
            break
        turn = 3 - turn
    
    board = undo_move(board, turn, col, pop)
    return board

random.seed(101)
with open("./connect4_tests_caleb.py", "w") as f:
    # check_move
    f.write("from connect4 import *\n")

    n_tests = 100
    f.write("count = 0\n")
    for i in range(1, n_tests + 1):
        nrows = random.randint(6, 13)
        board = generate_board(nrows)

        turn = random.randint(1, 2)
        col = random.randint(0, 6)
        pop = random.choice((True, False))

        result = check_move(board, turn, col, pop)

        f.write(f"board = {board}\n")
        f.write(f"# board with {nrows} rows\n")
        f.write(
            f"if not check_move(board, {turn}, {col}, {pop}) == {result}: print('check_move test {i} failed'); count += 1\n"
        )
        f.write('\n')
    f.write(
        f"print(f\"check_move: {{{n_tests} - count}} out of {n_tests} passed.\")\n"
    )
    
    # apply_move
    n_tests = 100
    f.write("count = 0\n")
    for i in range(1, n_tests + 1):
        nrows = random.randint(6, 13)
        board = generate_board(nrows)
        
        turn = random.randint(1, 2)
        col, pop = get_random_valid_move(board, turn)

        result = apply_move(board, turn, col, pop)

        f.write(f"board = {board}\n")
        f.write(f"board_expected = {result}\n")
        f.write(
            f"board_result = apply_move(board, {turn}, {col}, {pop})\n"
        )
        f.write(f"# board with {nrows} rows\n")
        f.write(
            f"if not board_result == board_expected: print('apply_move test {i} failed'); count += 1\n"
        )
        f.write('\n')
    f.write(
        f"print(f\"apply_move: {{{n_tests} - count}} out of {n_tests} passed.\")\n"
    )

    # check_victory
    n_tests = 100
    f.write("count = 0\n")
    
    results = {0: 0, 1: 0, 2: 0, 3: 0}
    for i in range(1, n_tests + 1):
        nrows = random.randint(6, 13)
        board = generate_board(nrows)
        who_played = random.randint(1, 2)

        if random.random() < 0.3:
            board = make_board_less_winning(board)

        result1 = check_victory(board, who_played)
        result2 = check_victory(board, 3-who_played)
        if result1 > 0 and result2 > 0 and result1 != result2:
            result = 3
        else:
            result = result1
        results[result] += 1

        result = check_victory(board, who_played)
        f.write(f"board = {board}\n")
        f.write(
            f"if not check_victory(board, {who_played}) == {result}: print('check_victory test {i} failed'); count += 1\n"
        )
        f.write('\n')

    f.write(
        f"print(f\"check_victory: {{{n_tests} - count}} out of {n_tests} passed.\")\n"
    )

print(results)

with open("./connect4_tests_caleb_computer_move.py", "w") as f:
    f.write("from connect4 import *\n")

    n_tests = 200
    f.write("win_count = 0\n")
    f.write("block_count = 0\n")
    f.write("valid_count = 0\n")
    win_tests = 0
    block_tests = 0
    valid_tests = 0
    for i in range(1, n_tests + 1):
        nrows = random.randint(6, 13)
        board = generate_near_win_board(nrows)
        
        p1_win_moves = get_winning_moves(board, 1)
        p2_win_moves = get_winning_moves(board, 2)
        p1_not_lose_moves = get_not_losing_moves(board, 1)
        p2_not_lose_moves = get_not_losing_moves(board, 2)


        if p1_win_moves:
            win_tests += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, 1, 2)")
            f.write("# winning move exists for p1\n")
            f.write(
                f"if move not in {str(p1_win_moves)}: print('computer_move test {i} failed - with winning move for p1'); win_count += 1\n\n"
            )
        elif p1_not_lose_moves:
            block_tests += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, 1, 2)")
            f.write("# blocking move exists for p1\n")
            f.write(
                f"if move not in {str(p1_not_lose_moves)}: print('computer_move test {i} failed - with blocking move for p1'); block_count += 1\n\n"
            )
        else:
            val_moves = get_valid_moves(board, 1)
            valid_tests += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, 1, 2)")
            f.write("# valid move exists for p1\n")
            f.write(
                f"if move not in {str(val_moves)}: print('computer_move test {i} failed - with valid move for p1'); valid_count += 1\n\n"
            )
        
        if p2_win_moves:
            win_tests += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, 2, 2)")
            f.write("# winning move exists for p2\n")
            f.write(
                f"if move not in {str(p2_win_moves)}: print('computer_move test {i} failed - with winning move for p2'); win_count += 1\n\n"
            )
        elif p2_not_lose_moves:
            block_tests += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, 2, 2)")
            f.write("# blocking move exists for p2\n")
            f.write(
                f"if move not in {str(p2_not_lose_moves)}: print('computer_move test {i} failed - with blocking move for p2'); block_count += 1\n\n"
            )
        else:
            val_moves = get_valid_moves(board, 2)
            valid_tests += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, 2, 2)")
            f.write("# valid move exists for p2\n")
            f.write(
                f"if move not in {str(val_moves)}: print('computer_move test {i} failed - with valid move for p2'); valid_count += 1\n\n"
            )

    print(
        f"{win_tests=}, {block_tests=}, {valid_tests=}"
    )

    f.write(
        f"print(f\"winning moves: {{{win_tests} - win_count}} out of {win_tests} passed.\")\n"
    )
    f.write(
        f"print(f\"blocking moves: {{{block_tests} - block_count}} out of {block_tests} passed.\")\n"
    )
    f.write(
        f"print(f\"valid moves: {{{valid_tests} - valid_count}} out of {valid_tests} passed.\")\n"
    )
