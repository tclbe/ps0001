from quixo_ans import *
import random


def get_random_move(board, turn):
    val_moves = get_valid_moves(board, turn)
    return random.choice(val_moves)


def make_board_winning(board, winner=None, at_most=None):

    situation = random.random()

    if not winner: winner = random.randint(1, 2)

    if situation < 0.25:
        # set one line to win (may cause additional wins)

        how = random.random()
        if how < 0.33:
            # add winning row
            row = random.randint(0, n - 1)
            board[row * n:(row + 1) * n] = [winner] * n
        elif how < 0.66:
            # add winning column
            col = random.randint(0, n - 1)
            board[col::n] = [winner] * n
        else:
            # add winning diagonal
            which = random.randint(-1, 1)
            if which == 1:
                # diagonal
                board[::n + 1] = [winner] * n
            else:
                # antidiagonal
                board[n - 1:n * (n - 1) + 1:n - 1] = [winner] * n
    elif situation < 0.5:
        # set two lines to win, one of each player.
        # they must be in the same direction, and neither can be diagonal.
        how = random.random()
        if how < 0.5:
            p1_row, p2_row = random.sample(range(n), 2)
            board[p1_row * n:(p1_row + 1) * n] = [1] * n
            board[p2_row * n:(p2_row + 1) * n] = [2] * n
        else:
            p1_col, p2_col = random.sample(range(n), 2)
            board[p1_col::n] = [1] * n
            board[p2_col::n] = [2] * n
    elif situation < 0.75:
        # set 3 lines to win, two for one player, one for other.

        loser = 3 - winner

        how = random.random()
        if how < 0.5:
            p1_row, p2_row, p1_row2 = random.sample(range(n), 3)
            board[p1_row * n:(p1_row + 1) * n] = [winner] * n
            board[p2_row * n:(p2_row + 1) * n] = [loser] * n
            board[p1_row2 * n:(p1_row2 + 1) * n] = [winner] * n
        else:
            p1_col, p2_col, p1_col2 = random.sample(range(n), 3)
            board[p1_col::n] = [winner] * n
            board[p2_col::n] = [loser] * n
            board[p1_col2::n] = [winner] * n
    else:
        # set one player to win multiple times
        if not at_most: times = random.randint(1, min(n // 3, 3))
        else: times = at_most

        how = random.random()

        if how < 0.5:
            for row in random.sample(range(n), times):
                board[row * n:(row + 1) * n] = [winner] * n
        else:
            for col in random.sample(range(n), times):
                board[col::n] = [winner] * n
    return board


random.seed(101)
with open("./tests_caleb.py", "w") as f:
    f.write("from quixo import *\n")

    n_tests = 100
    f.write("count = 0\n")
    for i in range(1, n_tests + 1):
        n = random.randint(5, 10)
        board = [random.choice((0, 1, 2)) for _ in range(n**2)]
        edge_indexes = [
            i for i in range(n**2)
            if i // n in (0, n - 1) or i % n in (0, n - 1)
        ]
        indexes = range(n**2)

        index = random.choice(
            random.choices([edge_indexes, indexes], [0.9, 0.1])[0])
        r = index // n
        c = index % n
        turn = random.randint(1, 2)
        push_from = random.choice('TBLR')

        result = check_move(board, turn, index, push_from)

        # f.write(
        #     f"# on perimeter: {r in (0, n-1) or c in (0, n-1)}: r = {r}, c = {c}\n"
        # )
        # f.write(
        #     f"# moving own tile: {board[index] != turn}: tile at position: {board[index]}\n"
        # )
        f.write(f"board = {board}\n")
        f.write(f"# {n} by {n} board\n")
        f.write(
            f"if not check_move(board, {turn}, {index}, '{push_from}') == {result}: print('check_move test {i} failed'); count += 1\n"
        )
        f.write('\n')
    f.write(
        f"print(f\"check_move: {{{n_tests} - count}} out of {n_tests} passed.\")\n"
    )

with open("./tests_caleb.py", "a") as f:
    n_tests = 100
    f.write("count = 0\n")
    for i in range(1, n_tests + 1):
        n = random.randint(5, 10)
        board = [random.choice((0, 1, 2)) for _ in range(n**2)]
        edge_indexes = [
            i for i in range(n**2)
            if i // n in (0, n - 1) or i % n in (0, n - 1)
        ]
        turn = random.randint(1, 2)
        valid_indexes = [
            i for i in edge_indexes if board[i] == turn or board[i] == 0
        ]
        index = random.choice(valid_indexes)
        r = index // n
        c = index % n

        valid_push_from = ""
        if r != 0: valid_push_from += 'T'
        if r != n - 1: valid_push_from += 'B'
        if c != 0: valid_push_from += 'L'
        if c != n - 1: valid_push_from += 'R'

        push_from = random.choice(valid_push_from)

        result = apply_move(board, turn, index, push_from)

        f.write(f"board = {board}\n")
        f.write(f"board_expected = {result}\n")
        f.write(
            f"board_result = apply_move(board, {turn}, {index}, '{push_from}')\n"
        )
        f.write(f"# {n} by {n} board\n")
        f.write(
            f"if not board_result == board_expected: print('apply_move test {i} failed'); count += 1\n"
        )
        f.write('\n')
    f.write(
        f"print(f\"apply_move: {{{n_tests} - count}} out of {n_tests} passed.\")\n"
    )

with open("./tests_caleb.py", "a") as f:
    n_tests = 100
    f.write("count = 0\n")
    for i in range(1, n_tests + 1):
        n = random.randint(5, 10)
        board = [random.choice((0, 1, 2)) for _ in range(n**2)]
        who_played = random.randint(1, 2)

        if random.random() < 0.8:
            # make a board with a winner
            board = make_board_winning(board)

        else:
            # don't alter board.
            pass

        result = check_victory(board, who_played)

        f.write(f"board = {board}\n")
        f.write(
            f"if not check_victory(board, {who_played}) == {result}: print('check_victory test {i} failed'); count += 1\n"
        )
        f.write('\n')

    f.write(
        f"print(f\"check_victory: {{{n_tests} - count}} out of {n_tests} passed.\")\n"
    )

with open("./tests_caleb_computer_move.py", "w") as f:
    f.write("from quixo import *\n")

    n_tests = 200
    f.write("win_count = 0\n")
    f.write("block_count = 0\n")
    f.write("valid_count = 0\n")
    win_tests_r1 = 0
    win_tests_r2 = 0
    block_tests = 0
    valid_tests = 0
    for i in range(1, n_tests + 1):
        n = random.randint(5, 7)
        board = [random.choice((0, 1, 2)) for _ in range(n**2)]
        while check_victory(board, 2) != 0:
            board = [random.choice((0, 1, 2)) for _ in range(n**2)]

        turn = random.randint(1, 2)
        opp = 3 - turn

        win_moves = get_winning_moves(board, turn)
        if win_moves:
            win_tests_r1 += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, {turn}, 2)")
            f.write("# winning move exists, r1\n")
            f.write(
                f"if move not in {str(win_moves)}: print('computer_move test {i} failed - with winning move'); win_count += 1\n\n"
            )
            continue

        # there is no winning move, attempt to make one.
        original_board = make_board_winning(board, opp, 1)

        move_idx, move_dir = get_random_move(original_board, opp)
        board = apply_move(original_board, 0, move_idx, move_dir)

        while check_victory(board, 2) != 0:
            move_idx, move_dir = get_random_move(board, opp)
            board = apply_move(board, 0, move_idx, move_dir)

        win_moves = get_winning_moves(board, turn)
        if win_moves:
            win_tests_r2 += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, {turn}, 2)")
            f.write("# winning move exists, r2\n")
            f.write(
                f"if move not in {str(win_moves)}: print('computer_move test {i} failed - with winning move'); win_count += 1\n\n"
            )
            continue

        block_moves = get_not_losing_moves(board, turn)
        if block_moves:
            block_tests += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, {turn}, 2)")
            f.write("# blocking move exists\n")
            f.write(
                f"if move not in {str(block_moves)}: print('computer_move test {i} failed - with blocking move'); block_count += 1\n\n"
            )
            continue

        val_moves = get_valid_moves(board, turn)
        if val_moves:
            valid_tests += 1
            f.write(f"board = {board}\n")
            f.write(f"move = computer_move(board, {turn}, 2)")
            f.write("# valid move exists\n")
            f.write(
                f"if move not in {str(val_moves)}: print('computer_move test {i} failed - with valid move'); valid_count += 1\n\n"
            )
            continue

    win_tests = win_tests_r1 + win_tests_r2
    print(
        f"{win_tests_r1=}, {win_tests_r2=}, {win_tests=}, {block_tests=}, {valid_tests=}"
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
