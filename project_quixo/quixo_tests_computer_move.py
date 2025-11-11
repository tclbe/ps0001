from quixo import *
win_count = 0
block_count = 0
valid_count = 0
board = [0, 0, 1, 2, 2, 1, 0, 2, 1, 2, 0, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 0, 2, 0, 2, 1, 1, 1, 0, 2, 1, 2, 0, 1, 2, 2, 2, 2, 1, 1, 0, 1, 2, 2, 0, 2, 0, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(13, 'L'), (27, 'L'), (28, 'R'), (34, 'L'), (42, 'R'), (45, 'T')]: print('computer_move test 1 failed - with blocking move'); block_count += 1

board = [0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 0, 2, 1, 0, 1, 1, 0, 0, 0, 2, 2, 2, 2, 1, 1, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (2, 'B'), (4, 'B'), (5, 'B'), (6, 'B'), (13, 'B'), (27, 'B'), (28, 'R')]: print('computer_move test 2 failed - with blocking move'); block_count += 1

board = [1, 2, 2, 2, 2, 1, 0, 0, 0, 2, 1, 2, 1, 1, 2, 1, 0, 0, 1, 2, 0, 1, 2, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(20, 'T'), (22, 'R'), (23, 'R'), (24, 'T')]: print('computer_move test 3 failed - with winning move'); win_count += 1

board = [2, 2, 2, 0, 1, 1, 0, 2, 2, 1, 0, 0, 2, 1, 2, 0, 1, 2, 1, 2, 2, 0, 1, 0, 0, 0, 1, 2, 2, 1, 1, 0, 0, 2, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(3, 'B'), (23, 'L')]: print('computer_move test 4 failed - with winning move'); win_count += 1

board = [0, 0, 2, 0, 0, 2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 0, 2, 0, 2, 2, 0, 1, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'B'), (1, 'L'), (2, 'B'), (2, 'L'), (3, 'B'), (3, 'L'), (4, 'B'), (4, 'L'), (9, 'B'), (10, 'R'), (19, 'T'), (19, 'L'), (20, 'T'), (24, 'T')]: print('computer_move test 5 failed - with blocking move'); block_count += 1

board = [1, 1, 2, 1, 1, 1, 0, 1, 2, 0, 0, 0, 1, 0, 2, 2, 2, 2, 1, 0, 0, 1, 2, 1, 1]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(5, 'R'), (9, 'L'), (21, 'T')]: print('computer_move test 6 failed - with winning move'); win_count += 1

board = [0, 0, 2, 2, 0, 1, 0, 2, 1, 2, 0, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 0, 1, 1, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(10, 'T'), (10, 'R'), (15, 'T'), (20, 'T')]: print('computer_move test 7 failed - with winning move'); win_count += 1

board = [0, 0, 1, 2, 1, 0, 2, 2, 0, 0, 1, 2, 0, 2, 2, 1, 2, 2, 2, 0, 1, 2, 2, 0, 2, 1, 0, 1, 2, 0, 0, 2, 0, 1, 0, 2]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(2, 'B'), (4, 'B'), (5, 'B'), (12, 'R'), (23, 'B'), (23, 'L'), (29, 'B'), (29, 'L'), (30, 'R'), (32, 'T'), (32, 'R'), (33, 'T'), (33, 'R'), (34, 'R')]: print('computer_move test 8 failed - with blocking move'); block_count += 1

board = [0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2, 2, 0, 2, 1, 1, 1, 1, 1, 2, 0, 1, 2]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'B'), (2, 'B'), (4, 'B'), (9, 'B'), (14, 'B'), (15, 'R'), (21, 'T'), (21, 'L'), (22, 'T'), (22, 'L'), (24, 'T'), (24, 'L')]: print('computer_move test 9 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 2, 0, 2, 0, 2, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'R'), (1, 'R'), (3, 'L'), (4, 'L'), (10, 'R'), (14, 'L'), (19, 'L'), (22, 'T'), (22, 'L'), (23, 'L')]: print('computer_move test 10 failed - with blocking move'); block_count += 1

board = [2, 1, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 1, 1, 2, 0, 2, 1, 0, 1, 1, 2, 2, 1, 2, 1, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(43, 'T'), (43, 'L'), (43, 'R')]: print('computer_move test 11 failed - with winning move'); win_count += 1

board = [1, 0, 2, 2, 2, 0, 1, 2, 0, 2, 1, 0, 0, 1, 1, 0, 2, 0, 0, 0, 1, 2, 0, 2, 1, 1, 1, 1, 2, 0, 2, 1, 1, 2, 1, 2, 2, 0, 1, 0, 1, 0, 2, 2, 2, 0, 2, 1, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'R'), (2, 'R'), (3, 'R'), (4, 'R'), (5, 'R'), (7, 'R'), (21, 'R'), (28, 'R'), (35, 'R'), (42, 'R'), (43, 'R'), (44, 'R'), (45, 'R'), (46, 'R')]: print('computer_move test 12 failed - with blocking move'); block_count += 1

board = [0, 1, 2, 1, 1, 1, 1, 2, 1, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 0, 0, 2, 0, 0, 2]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(23, 'T')]: print('computer_move test 13 failed - with winning move'); win_count += 1

board = [0, 0, 2, 1, 2, 0, 0, 0, 2, 2, 0, 0, 1, 2, 0, 0, 2, 2, 2, 0, 0, 1, 0, 2, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(3, 'B'), (14, 'T'), (14, 'L'), (15, 'R'), (19, 'T'), (20, 'R'), (21, 'R'), (22, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 14 failed - with blocking move'); block_count += 1

board = [0, 2, 0, 2, 0, 0, 0, 0, 2, 2, 1, 2, 1, 2, 0, 0, 0, 1, 2, 2, 2, 0, 0, 2, 0, 1, 1, 1, 1, 2, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'B'), (5, 'B'), (7, 'B'), (14, 'B'), (21, 'B'), (41, 'L'), (42, 'R'), (47, 'R')]: print('computer_move test 15 failed - with blocking move'); block_count += 1

board = [2, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 1, 1, 2, 2, 2, 2, 0, 1, 2, 2, 0, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 2, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(11, 'L'), (17, 'L'), (23, 'L'), (24, 'R')]: print('computer_move test 16 failed - with blocking move'); block_count += 1

board = [0, 2, 0, 2, 0, 0, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 0, 0, 2, 1, 1, 2, 2, 0, 1]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (4, 'B'), (4, 'L'), (5, 'T'), (5, 'B'), (5, 'R'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 17 failed - with valid move'); valid_count += 1

board = [1, 0, 2, 2, 0, 0, 0, 0, 2, 0, 2, 2, 1, 1, 0, 0, 0, 2, 2, 1, 1, 1, 2, 0, 1, 2, 1, 1, 1, 1, 2, 0, 2, 1, 1, 0, 0, 0, 0, 2, 1, 1, 2, 1, 0, 1, 2, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(4, 'B'), (4, 'L'), (5, 'L'), (6, 'L')]: print('computer_move test 18 failed - with winning move'); win_count += 1

board = [0, 2, 2, 1, 0, 0, 2, 1, 1, 0, 0, 0, 0, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'R'), (1, 'R'), (2, 'R'), (4, 'L'), (5, 'R'), (9, 'L'), (20, 'R'), (22, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 19 failed - with blocking move'); block_count += 1

board = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 2, 0, 0, 1, 1, 1, 2, 2, 1, 1, 0, 0, 0, 1, 1, 0, 2]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(0, 'R'), (6, 'T'), (18, 'T'), (24, 'T'), (30, 'T')]: print('computer_move test 20 failed - with winning move'); win_count += 1

board = [0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 1, 2, 0, 1, 2, 0, 2, 1, 2, 2, 0, 2, 0, 0, 0, 1, 2, 0, 2, 1]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (6, 'T'), (6, 'B'), (6, 'R'), (12, 'T'), (12, 'B'), (12, 'R'), (18, 'T'), (18, 'B'), (18, 'R'), (23, 'T'), (23, 'B'), (23, 'L'), (29, 'T'), (29, 'B'), (29, 'L'), (30, 'T'), (30, 'R'), (31, 'T'), (31, 'L'), (31, 'R'), (33, 'T'), (33, 'L'), (33, 'R'), (35, 'T'), (35, 'L')]: print('computer_move test 21 failed - with valid move'); valid_count += 1

board = [2, 2, 0, 1, 1, 2, 0, 1, 1, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 2, 1, 0]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R'), (21, 'T'), (21, 'L'), (21, 'R'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 22 failed - with valid move'); valid_count += 1

board = [1, 1, 2, 0, 0, 1, 1, 2, 1, 1, 1, 1, 2, 2, 0, 1, 1, 2, 2, 2, 0, 0, 1, 2, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (14, 'T'), (14, 'B'), (14, 'L'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R'), (21, 'T'), (21, 'L'), (21, 'R'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 23 failed - with valid move'); valid_count += 1

board = [0, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B'), (0, 'R'), (6, 'T'), (24, 'T'), (30, 'T')]: print('computer_move test 24 failed - with winning move'); win_count += 1

board = [0, 1, 1, 0, 0, 2, 2, 1, 1, 0, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 0, 1, 1, 2, 2, 2, 2, 0, 2, 2, 1, 0, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 0, 1, 2, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(21, 'R'), (34, 'L'), (35, 'R'), (41, 'L'), (43, 'R'), (45, 'R'), (46, 'R'), (48, 'L')]: print('computer_move test 25 failed - with blocking move'); block_count += 1

board = [2, 2, 1, 0, 0, 1, 0, 0, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 0, 0, 1, 0, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0, 1, 2, 1, 0, 1, 0, 2, 0, 2, 1, 1, 2, 1, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'R'), (1, 'R'), (3, 'L'), (4, 'L'), (6, 'L'), (7, 'T'), (21, 'T'), (21, 'R'), (27, 'L'), (34, 'L'), (41, 'L'), (42, 'T'), (46, 'L')]: print('computer_move test 26 failed - with blocking move'); block_count += 1

board = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 2, 0, 1, 0, 1, 1, 0, 0, 2, 1, 0, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(24, 'B'), (24, 'R'), (29, 'B'), (30, 'R'), (31, 'T'), (31, 'L'), (31, 'R'), (33, 'T'), (33, 'L'), (33, 'R'), (35, 'L')]: print('computer_move test 27 failed - with blocking move'); block_count += 1

board = [2, 0, 0, 0, 0, 0, 1, 1, 0, 2, 1, 1, 0, 0, 0, 1, 1, 2, 0, 1, 1, 0, 0, 1, 1, 1, 2, 0, 1, 2, 1, 1, 2, 1, 1, 2]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'B'), (2, 'B'), (3, 'B'), (12, 'B'), (17, 'L'), (18, 'B'), (32, 'T'), (32, 'L'), (35, 'L')]: print('computer_move test 28 failed - with blocking move'); block_count += 1

board = [1, 1, 1, 1, 0, 0, 2, 1, 1, 1, 2, 0, 1, 2, 0, 1, 1, 2, 1, 0, 0, 2, 1, 1, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(4, 'B'), (4, 'L'), (5, 'T'), (5, 'B'), (5, 'R'), (10, 'T'), (10, 'B'), (10, 'R'), (14, 'T'), (14, 'B'), (14, 'L'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R'), (21, 'T'), (21, 'L'), (21, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 29 failed - with valid move'); valid_count += 1

board = [1, 1, 2, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 2, 1, 2, 2, 1]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(2, 'B'), (2, 'L'), (2, 'R'), (5, 'T'), (5, 'B'), (5, 'R'), (9, 'T'), (9, 'B'), (9, 'L'), (15, 'T'), (15, 'B'), (15, 'R'), (20, 'T'), (20, 'R'), (22, 'T'), (22, 'L'), (22, 'R'), (23, 'T'), (23, 'L'), (23, 'R')]: print('computer_move test 30 failed - with valid move'); valid_count += 1

board = [1, 0, 2, 1, 0, 0, 0, 1, 2, 0, 2, 2, 1, 1, 1, 2, 2, 1, 0, 2, 1, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2, 1, 2, 1, 0, 2, 1, 2, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (1, 'L'), (3, 'L'), (4, 'L'), (5, 'L'), (6, 'L'), (7, 'R'), (13, 'L'), (20, 'L'), (35, 'R'), (42, 'R'), (44, 'L'), (45, 'L'), (46, 'L'), (47, 'L'), (48, 'L')]: print('computer_move test 31 failed - with blocking move'); block_count += 1

board = [0, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 1, 0, 2, 2, 2, 2, 2, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(0, 'B')]: print('computer_move test 32 failed - with winning move'); win_count += 1

board = [2, 0, 2, 2, 2, 0, 0, 2, 1, 2, 1, 2, 1, 2, 0, 0, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 0, 1, 1, 0, 1]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(1, 'B')]: print('computer_move test 33 failed - with winning move'); win_count += 1

board = [2, 0, 1, 1, 1, 2, 2, 2, 2, 0, 2, 1, 1, 2, 0, 1, 1, 2, 2, 0, 0, 0, 0, 1, 0, 2, 1, 2, 2, 2, 1, 0, 1, 2, 2, 1, 0, 2, 2, 2, 0, 2, 2, 1, 1, 2, 1, 1, 2]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(14, 'R'), (20, 'T'), (20, 'B')]: print('computer_move test 34 failed - with winning move'); win_count += 1

board = [0, 0, 1, 0, 0, 0, 2, 2, 2, 2, 1, 0, 2, 2, 0, 2, 0, 0, 1, 1, 2, 2, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 1, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(3, 'B'), (3, 'L'), (4, 'L'), (5, 'L'), (17, 'L'), (29, 'L'), (30, 'R'), (31, 'R'), (32, 'R'), (34, 'L'), (35, 'L')]: print('computer_move test 35 failed - with blocking move'); block_count += 1

board = [2, 2, 1, 2, 1, 1, 2, 0, 2, 2, 0, 2, 1, 1, 2, 2, 2, 0, 2, 1, 1, 2, 1, 0, 0, 1, 1, 2, 1, 0, 0, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 0, 2, 0, 0, 1, 2, 1, 2]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'R'), (1, 'R'), (3, 'R'), (6, 'B'), (21, 'R'), (27, 'B'), (34, 'B'), (34, 'L'), (41, 'T'), (41, 'B'), (42, 'R'), (43, 'R'), (44, 'R'), (46, 'T'), (46, 'R'), (48, 'T'), (48, 'L')]: print('computer_move test 36 failed - with blocking move'); block_count += 1

board = [1, 2, 0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 0, 2, 2, 0, 0, 0, 1, 1, 0, 1, 2, 0, 1, 0, 2, 2, 0, 1, 2, 1, 2, 2, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'B'), (2, 'L'), (6, 'B'), (6, 'L'), (13, 'B'), (14, 'B'), (20, 'B'), (27, 'B'), (28, 'B'), (34, 'B'), (42, 'T'), (42, 'R'), (43, 'R'), (45, 'L'), (46, 'T'), (46, 'L'), (48, 'T'), (48, 'L')]: print('computer_move test 37 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 0, 0, 0, 2, 2, 0, 1, 1, 1, 0, 2, 2, 2, 0, 1, 1, 2, 2, 0, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'R'), (3, 'R'), (4, 'B'), (4, 'R'), (11, 'T'), (11, 'L'), (12, 'T'), (12, 'B'), (12, 'R'), (17, 'T'), (17, 'B'), (17, 'L'), (18, 'T'), (18, 'B'), (18, 'R'), (23, 'T'), (23, 'B'), (23, 'L'), (24, 'T'), (24, 'B'), (24, 'R'), (29, 'T'), (29, 'B'), (29, 'L'), (30, 'T'), (30, 'R'), (31, 'T'), (31, 'L'), (31, 'R'), (34, 'T'), (34, 'L'), (34, 'R'), (35, 'T'), (35, 'L')]: print('computer_move test 38 failed - with blocking move'); block_count += 1

board = [0, 0, 2, 1, 0, 2, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 1, 2, 0, 0, 0, 2, 1, 1, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'B'), (3, 'B'), (6, 'B'), (23, 'L'), (31, 'T')]: print('computer_move test 39 failed - with blocking move'); block_count += 1

board = [0, 2, 2, 1, 2, 0, 1, 2, 2, 2, 2, 0, 0, 2, 0, 2, 0, 1, 2, 2, 0, 1, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(3, 'L'), (5, 'L'), (11, 'L'), (12, 'R'), (17, 'L')]: print('computer_move test 40 failed - with blocking move'); block_count += 1

board = [0, 2, 1, 0, 0, 0, 0, 2, 1, 2, 1, 1, 2, 2, 2, 0, 2, 2, 1, 0, 0, 1, 2, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(3, 'L'), (4, 'L')]: print('computer_move test 41 failed - with winning move'); win_count += 1

board = [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 1, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(1, 'B'), (1, 'L'), (1, 'R'), (23, 'T'), (29, 'T'), (35, 'T')]: print('computer_move test 42 failed - with winning move'); win_count += 1

board = [2, 1, 0, 2, 1, 2, 0, 2, 0, 1, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 2, 0, 1, 2]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(15, 'T'), (15, 'B'), (15, 'R')]: print('computer_move test 43 failed - with winning move'); win_count += 1

board = [2, 2, 2, 2, 0, 0, 1, 2, 0, 2, 0, 0, 0, 0, 2, 2, 1, 1, 1, 2, 1, 2, 0, 1, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(5, 'T'), (10, 'T'), (20, 'T'), (22, 'T'), (23, 'T')]: print('computer_move test 44 failed - with blocking move'); block_count += 1

board = [0, 0, 0, 1, 2, 1, 2, 1, 0, 1, 1, 2, 1, 0, 0, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 0, 1, 0, 1, 0, 0, 0, 1, 2, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(13, 'B'), (20, 'B'), (34, 'T'), (41, 'T'), (48, 'T')]: print('computer_move test 45 failed - with winning move'); win_count += 1

board = [0, 1, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 2, 2, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(5, 'R'), (9, 'B'), (14, 'B'), (14, 'L'), (20, 'R')]: print('computer_move test 46 failed - with blocking move'); block_count += 1

board = [1, 1, 2, 1, 2, 0, 0, 2, 1, 2, 1, 1, 1, 0, 0, 1, 2, 2, 1, 2, 1, 1, 0, 0, 1, 2, 2, 1, 2, 1, 0, 2, 1, 1, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(2, 'R'), (4, 'L'), (5, 'L'), (17, 'L')]: print('computer_move test 47 failed - with blocking move'); block_count += 1

board = [1, 2, 1, 1, 1, 2, 2, 2, 0, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 0, 0, 0, 1, 1, 2, 1, 2, 2, 0, 2, 0, 2, 2, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'B'), (6, 'B'), (20, 'B'), (27, 'B')]: print('computer_move test 48 failed - with blocking move'); block_count += 1

board = [0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 1, 2, 1, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (9, 'T'), (9, 'B'), (9, 'L'), (14, 'T'), (14, 'B'), (14, 'L'), (19, 'T'), (19, 'B'), (19, 'L'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 49 failed - with valid move'); valid_count += 1

board = [0, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 0, 2, 0, 0, 2, 2, 2, 0, 1, 2, 0, 0, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'B'), (0, 'R'), (2, 'B'), (2, 'L'), (4, 'B'), (4, 'L'), (12, 'T'), (18, 'T'), (32, 'T'), (34, 'T')]: print('computer_move test 50 failed - with blocking move'); block_count += 1

board = [0, 0, 2, 0, 1, 0, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 0, 2, 1, 2, 2, 1, 0, 2, 1, 1, 2, 2, 1, 2, 2, 0, 1, 2, 0, 0, 0, 1, 2, 1, 2, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(13, 'L')]: print('computer_move test 51 failed - with winning move'); win_count += 1

board = [0, 1, 2, 2, 0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 0, 2, 2, 0, 0, 1, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'R'), (2, 'R'), (3, 'R'), (4, 'B'), (4, 'L')]: print('computer_move test 52 failed - with winning move'); win_count += 1

board = [2, 1, 2, 2, 2, 2, 0, 1, 2, 0, 0, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 1, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(1, 'B')]: print('computer_move test 53 failed - with winning move'); win_count += 1

board = [0, 0, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 2, 2, 1, 1, 0, 2, 0, 2, 1, 1, 0, 1, 1, 2, 2, 1, 0, 2, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 2, 1, 1, 1]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(42, 'R'), (43, 'R'), (44, 'T'), (44, 'R')]: print('computer_move test 54 failed - with winning move'); win_count += 1

board = [1, 2, 0, 1, 1, 2, 0, 0, 2, 1, 0, 2, 1, 2, 2, 2, 0, 0, 1, 2, 1, 1, 2, 1, 1, 1, 2, 0, 2, 2, 1, 1, 1, 2, 2, 0, 0, 2, 1, 1, 2, 0, 0, 1, 1, 0, 1, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(13, 'L')]: print('computer_move test 55 failed - with winning move'); win_count += 1

board = [0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 2, 0, 2, 1, 1, 0, 0, 2, 2, 0, 0, 2, 2, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(10, 'R'), (20, 'R'), (21, 'R')]: print('computer_move test 56 failed - with blocking move'); block_count += 1

board = [0, 1, 0, 0, 1, 2, 1, 2, 0, 1, 1, 2, 0, 2, 0, 2, 0, 2, 1, 0, 0, 2, 2, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(0, 'B'), (5, 'B'), (15, 'B'), (20, 'T'), (20, 'R')]: print('computer_move test 57 failed - with winning move'); win_count += 1

board = [0, 0, 2, 1, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(2, 'B'), (4, 'B')]: print('computer_move test 58 failed - with blocking move'); block_count += 1

board = [2, 2, 1, 0, 0, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 1, 0, 2, 0, 1, 0, 2, 2, 2, 1, 2, 2, 1, 0, 2, 1, 2, 1, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'R'), (6, 'B'), (6, 'R'), (12, 'B'), (18, 'T'), (18, 'B'), (24, 'T'), (30, 'T'), (30, 'R'), (31, 'L'), (31, 'R'), (33, 'L')]: print('computer_move test 59 failed - with blocking move'); block_count += 1

board = [1, 0, 1, 2, 2, 0, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 0, 2, 1, 1, 2, 0, 1, 2, 0, 2, 0, 0, 2, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'L'), (3, 'L'), (4, 'L'), (5, 'L'), (11, 'L'), (17, 'L'), (23, 'L'), (29, 'L')]: print('computer_move test 60 failed - with blocking move'); block_count += 1

board = [2, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 2, 0, 0, 1, 0, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 0, 2, 0, 2, 2, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(2, 'B'), (3, 'B'), (4, 'B'), (31, 'T'), (33, 'T'), (34, 'T')]: print('computer_move test 61 failed - with blocking move'); block_count += 1

board = [2, 1, 0, 1, 0, 2, 1, 1, 2, 2, 2, 0, 0, 0, 0, 2, 1, 2, 1, 2, 0, 2, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'L'), (2, 'L'), (3, 'L'), (4, 'L'), (14, 'L')]: print('computer_move test 62 failed - with blocking move'); block_count += 1

board = [0, 2, 1, 0, 0, 1, 0, 0, 2, 2, 0, 1, 1, 1, 1, 0, 2, 1, 1, 2, 0, 1, 1, 2, 2]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(10, 'T'), (10, 'R'), (15, 'T'), (20, 'T')]: print('computer_move test 63 failed - with winning move'); win_count += 1

board = [2, 1, 1, 2, 0, 1, 0, 2, 2, 0, 2, 1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 2, 2, 1, 0, 1, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'R'), (3, 'R'), (4, 'R'), (12, 'R'), (18, 'R'), (30, 'R'), (31, 'R'), (33, 'R')]: print('computer_move test 64 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 2, 0, 0, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(23, 'T'), (23, 'L'), (35, 'T')]: print('computer_move test 65 failed - with winning move'); win_count += 1

board = [0, 1, 1, 2, 0, 1, 0, 2, 1, 2, 1, 1, 1, 0, 1, 2, 2, 1, 1, 0, 1, 2, 2, 1, 0, 0, 1, 2, 2, 1, 0, 2, 2, 1, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(34, 'L'), (35, 'L')]: print('computer_move test 66 failed - with winning move'); win_count += 1

board = [0, 0, 0, 1, 2, 2, 0, 2, 1, 2, 0, 0, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(5, 'R'), (9, 'L')]: print('computer_move test 67 failed - with winning move'); win_count += 1

board = [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 2, 2, 1, 0, 2, 1, 1, 2, 2, 1, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(2, 'B')]: print('computer_move test 68 failed - with winning move'); win_count += 1

board = [2, 1, 0, 2, 1, 1, 1, 2, 2, 0, 0, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 0, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(15, 'R')]: print('computer_move test 69 failed - with winning move'); win_count += 1

board = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 2, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 1, 1, 2, 2, 1, 0, 1, 2, 2, 2, 1]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(23, 'L')]: print('computer_move test 70 failed - with winning move'); win_count += 1

board = [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 1, 1, 0, 1, 1, 2, 1, 0, 2, 2, 1, 1, 2, 0, 0, 1, 2, 1, 1, 2, 0, 1, 1, 1, 1, 2, 2, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (6, 'B'), (6, 'L'), (7, 'T'), (7, 'B'), (7, 'R'), (13, 'T'), (13, 'B'), (13, 'L'), (14, 'T'), (14, 'B'), (14, 'R'), (28, 'T'), (28, 'B'), (28, 'R'), (34, 'T'), (34, 'B'), (34, 'L'), (35, 'T'), (35, 'B'), (35, 'R'), (41, 'T'), (41, 'B'), (41, 'L'), (46, 'T'), (46, 'L'), (46, 'R'), (47, 'T'), (47, 'L'), (47, 'R'), (48, 'T'), (48, 'L')]: print('computer_move test 71 failed - with valid move'); valid_count += 1

board = [0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 1, 2, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 2, 1, 1, 2, 1, 0, 1, 2, 1, 2, 0, 0, 0, 0, 0, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B'), (0, 'R'), (7, 'T'), (14, 'T'), (21, 'T'), (35, 'T'), (42, 'T')]: print('computer_move test 72 failed - with winning move'); win_count += 1

board = [2, 1, 1, 2, 0, 1, 0, 1, 1, 1, 2, 0, 1, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 1, 2, 2, 2, 2, 0, 0, 2, 1]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(4, 'B'), (4, 'L')]: print('computer_move test 73 failed - with winning move'); win_count += 1

board = [1, 0, 2, 1, 2, 2, 0, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 1, 1, 1, 2, 0, 0, 2, 1, 2, 1, 0, 2, 0, 0, 2, 0, 1, 1, 2, 1, 2, 1, 2, 0, 0, 2, 1, 2, 1, 2, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (5, 'B'), (5, 'L'), (5, 'R'), (6, 'L'), (13, 'T'), (13, 'L'), (20, 'T'), (21, 'T'), (21, 'B'), (21, 'R'), (27, 'T'), (28, 'T'), (28, 'B'), (28, 'R'), (35, 'T'), (35, 'B'), (35, 'R'), (41, 'T'), (41, 'B'), (41, 'L'), (42, 'T'), (42, 'R'), (44, 'T'), (44, 'L'), (44, 'R'), (46, 'T'), (46, 'L'), (46, 'R'), (48, 'T'), (48, 'L')]: print('computer_move test 74 failed - with blocking move'); block_count += 1

board = [0, 2, 0, 2, 1, 1, 2, 0, 1, 2, 0, 0, 1, 2, 1, 1, 0, 1, 2, 2, 1, 0, 1, 0, 2, 2, 2, 2, 0, 0, 1, 2, 0, 1, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'B'), (0, 'R'), (2, 'L'), (4, 'L'), (5, 'B'), (5, 'L'), (11, 'T'), (11, 'B'), (12, 'T'), (12, 'R'), (17, 'T'), (17, 'L'), (23, 'T'), (29, 'T'), (30, 'T'), (30, 'R'), (32, 'L'), (33, 'L'), (34, 'L'), (35, 'T'), (35, 'L')]: print('computer_move test 75 failed - with blocking move'); block_count += 1

board = [0, 1, 1, 2, 2, 0, 1, 1, 2, 2, 2, 0, 2, 1, 1, 1, 2, 2, 2, 0, 1, 0, 2, 2, 0, 2, 0, 1, 1, 2, 0, 2, 1, 2, 2, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'R'), (1, 'R'), (2, 'R'), (5, 'B'), (6, 'R'), (11, 'B'), (11, 'L'), (30, 'R'), (32, 'R')]: print('computer_move test 76 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 2, 2, 0, 2, 2, 2, 2, 2, 0, 1, 0, 2, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B'), (5, 'B'), (5, 'R')]: print('computer_move test 77 failed - with winning move'); win_count += 1

board = [1, 0, 2, 0, 2, 0, 0, 1, 2, 2, 2, 2, 0, 0, 1, 1, 0, 0, 0, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 1, 2, 1, 0, 2, 2, 2, 1, 0, 1, 1, 2, 0, 2, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(2, 'B'), (3, 'B'), (5, 'B'), (45, 'T'), (46, 'T'), (47, 'T')]: print('computer_move test 78 failed - with blocking move'); block_count += 1

board = [0, 1, 1, 1, 1, 0, 0, 2, 1, 0, 1, 1, 1, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 1, 0, 1, 2, 2]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (5, 'B'), (5, 'L'), (6, 'T'), (6, 'B'), (6, 'R'), (11, 'T'), (11, 'B'), (11, 'L'), (12, 'T'), (12, 'B'), (12, 'R'), (18, 'T'), (18, 'B'), (18, 'R'), (24, 'T'), (24, 'B'), (24, 'R'), (30, 'T'), (30, 'R'), (31, 'T'), (31, 'L'), (31, 'R'), (32, 'T'), (32, 'L'), (32, 'R'), (33, 'T'), (33, 'L'), (33, 'R')]: print('computer_move test 79 failed - with valid move'); valid_count += 1

board = [1, 1, 0, 1, 1, 2, 0, 1, 1, 2, 1, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(2, 'B'), (2, 'L'), (2, 'R'), (22, 'T')]: print('computer_move test 80 failed - with winning move'); win_count += 1

board = [1, 1, 1, 0, 1, 1, 2, 0, 2, 0, 1, 1, 1, 0, 2, 0, 2, 1, 1, 0, 0, 2, 2, 1, 0, 0, 2, 1, 2, 2, 2, 2, 2, 0, 2, 1, 2, 1, 1, 0, 2, 0, 1, 1, 2, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(47, 'T')]: print('computer_move test 81 failed - with winning move'); win_count += 1

board = [2, 1, 0, 2, 0, 1, 0, 1, 0, 0, 2, 2, 2, 0, 0, 1, 1, 1, 1, 0, 0, 2, 0, 2, 1]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(4, 'B'), (9, 'B'), (14, 'B'), (19, 'B'), (19, 'L')]: print('computer_move test 82 failed - with winning move'); win_count += 1

board = [0, 2, 2, 0, 0, 1, 1, 1, 2, 1, 1, 0, 0, 1, 0, 2, 2, 2, 1, 0, 2, 1, 2, 2, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(3, 'B')]: print('computer_move test 83 failed - with winning move'); win_count += 1

board = [2, 0, 1, 2, 2, 0, 1, 2, 1, 0, 1, 1, 1, 2, 2, 0, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 0, 2, 1, 1, 1, 0, 1, 2, 2, 0, 2, 0, 0, 2, 2, 1, 2, 2, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'L'), (2, 'L'), (5, 'L'), (6, 'L'), (27, 'L'), (34, 'L'), (44, 'L'), (47, 'L'), (48, 'L')]: print('computer_move test 84 failed - with blocking move'); block_count += 1

board = [1, 2, 1, 2, 1, 0, 2, 2, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 0, 1, 1, 0, 2, 0, 1, 0, 2, 0, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(31, 'T')]: print('computer_move test 85 failed - with winning move'); win_count += 1

board = [1, 2, 2, 1, 1, 2, 1, 1, 0, 1, 2, 1, 0, 1, 1, 0, 0, 2, 1, 1, 1, 0, 2, 0, 1, 1, 2, 0, 2, 0, 1, 2, 0, 2, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(23, 'L'), (29, 'L')]: print('computer_move test 86 failed - with blocking move'); block_count += 1

board = [0, 1, 2, 0, 0, 2, 2, 2, 0, 1, 2, 2, 2, 2, 1, 0, 2, 2, 2, 2, 0, 0, 1, 0, 2]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (9, 'T'), (9, 'B'), (9, 'L'), (14, 'T'), (14, 'B'), (14, 'L'), (15, 'T'), (15, 'B'), (15, 'R'), (20, 'T'), (20, 'R'), (21, 'T'), (21, 'L'), (21, 'R'), (22, 'T'), (22, 'L'), (22, 'R'), (23, 'T'), (23, 'L'), (23, 'R')]: print('computer_move test 87 failed - with valid move'); valid_count += 1

board = [1, 1, 1, 1, 0, 2, 1, 0, 1, 1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2, 0, 1, 1, 1, 1]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(4, 'B'), (4, 'L'), (5, 'T'), (5, 'B'), (5, 'R'), (10, 'T'), (10, 'B'), (10, 'R'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R')]: print('computer_move test 88 failed - with valid move'); valid_count += 1

board = [0, 0, 1, 2, 2, 0, 2, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 0, 0, 1, 1, 1, 1, 0, 1, 2, 1, 1, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (5, 'B'), (5, 'L'), (6, 'T'), (6, 'B'), (6, 'R'), (11, 'T'), (11, 'B'), (11, 'L'), (12, 'T'), (12, 'B'), (12, 'R'), (23, 'T'), (23, 'B'), (23, 'L'), (24, 'T'), (24, 'B'), (24, 'R'), (30, 'T'), (30, 'R'), (32, 'T'), (32, 'L'), (32, 'R'), (35, 'T'), (35, 'L')]: print('computer_move test 89 failed - with valid move'); valid_count += 1

board = [2, 1, 0, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0, 0, 1, 2, 0, 1, 1, 1, 1, 0]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(1, 'B'), (2, 'B'), (4, 'B'), (9, 'B'), (14, 'B'), (15, 'R'), (19, 'B'), (24, 'L')]: print('computer_move test 90 failed - with winning move'); win_count += 1

board = [1, 1, 2, 1, 0, 1, 1, 2, 1, 0, 0, 1, 1, 1, 2, 1, 0, 2, 1, 1, 1, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(2, 'B'), (2, 'L'), (2, 'R'), (4, 'B'), (4, 'L'), (9, 'T'), (9, 'B'), (9, 'L'), (10, 'T'), (10, 'B'), (10, 'R'), (14, 'T'), (14, 'B'), (14, 'L'), (21, 'T'), (21, 'L'), (21, 'R'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 91 failed - with valid move'); valid_count += 1

board = [1, 1, 1, 2, 2, 1, 2, 2, 1, 0, 1, 1, 1, 2, 0, 2, 1, 2, 2, 2, 0, 1, 1, 2, 2]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(3, 'R'), (4, 'B'), (9, 'T'), (9, 'B'), (14, 'T'), (14, 'B'), (15, 'T'), (15, 'B'), (19, 'T'), (19, 'B'), (20, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 92 failed - with blocking move'); block_count += 1

board = [2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 2, 1, 0, 2, 2, 1, 2, 2, 1, 0, 2, 2, 1]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(2, 'B'), (22, 'T')]: print('computer_move test 93 failed - with winning move'); win_count += 1

board = [2, 1, 1, 1, 0, 1, 1, 1, 2, 2, 0, 0, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 0, 2, 0, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0, 2, 1, 2, 1, 0, 1, 0, 2, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (1, 'L'), (2, 'L'), (3, 'B'), (3, 'L'), (4, 'B'), (4, 'L'), (5, 'L'), (6, 'L'), (7, 'T'), (13, 'L'), (14, 'T'), (14, 'R'), (21, 'T'), (21, 'R'), (28, 'T'), (28, 'R'), (34, 'L'), (35, 'T'), (35, 'R'), (41, 'L'), (43, 'T'), (45, 'T'), (46, 'T')]: print('computer_move test 94 failed - with blocking move'); block_count += 1

board = [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 1, 2, 0, 2, 2, 2, 1, 0, 2, 1, 1, 1, 2, 1, 0, 2, 1, 2, 0, 2]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(12, 'R'), (17, 'L'), (23, 'L'), (33, 'T'), (34, 'T')]: print('computer_move test 95 failed - with blocking move'); block_count += 1

board = [2, 1, 0, 1, 1, 1, 0, 0, 0, 2, 0, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B'), (9, 'B'), (10, 'B'), (15, 'B'), (19, 'B'), (19, 'L'), (20, 'R')]: print('computer_move test 96 failed - with winning move'); win_count += 1

board = [0, 1, 2, 0, 2, 0, 1, 0, 2, 1, 0, 1, 1, 0, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(33, 'L'), (35, 'L')]: print('computer_move test 97 failed - with winning move'); win_count += 1

board = [0, 1, 0, 2, 1, 2, 2, 0, 2, 2, 0, 2, 2, 0, 1, 2, 1, 2, 1, 2, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'B'), (2, 'L'), (4, 'B'), (4, 'L'), (10, 'T'), (10, 'R'), (14, 'T'), (20, 'T'), (21, 'T'), (22, 'T'), (24, 'T')]: print('computer_move test 98 failed - with blocking move'); block_count += 1

board = [0, 2, 0, 0, 1, 0, 0, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 0, 1, 2, 0, 0, 2, 2, 0, 1, 0, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(5, 'B')]: print('computer_move test 99 failed - with winning move'); win_count += 1

board = [0, 0, 1, 2, 0, 0, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 0, 1, 1, 1]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(0, 'R'), (1, 'B'), (1, 'R'), (2, 'R'), (21, 'L'), (21, 'R'), (24, 'T')]: print('computer_move test 100 failed - with winning move'); win_count += 1

board = [2, 0, 0, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 2, 2, 1, 0, 1, 2, 2, 0, 0, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0, 0, 1, 1, 1, 1, 2, 0, 2, 2, 1, 2, 1, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(34, 'T'), (34, 'B')]: print('computer_move test 101 failed - with winning move'); win_count += 1

board = [1, 1, 1, 2, 2, 0, 0, 2, 2, 2, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 0, 1, 0, 2, 1, 1, 2, 2, 0, 1, 0, 0, 0, 1, 0, 1, 2, 1, 2, 0, 2, 0, 0, 1, 2, 0, 2, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (2, 'B'), (5, 'B'), (34, 'T'), (46, 'T'), (48, 'T')]: print('computer_move test 102 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(11, 'T'), (11, 'L'), (17, 'T'), (23, 'T'), (29, 'T'), (35, 'T')]: print('computer_move test 103 failed - with winning move'); win_count += 1

board = [1, 1, 1, 1, 2, 1, 1, 2, 0, 0, 2, 1, 2, 1, 1, 1, 2, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 2, 1, 2, 1, 2, 0, 0, 2, 2, 2, 2, 1, 2, 2, 0, 0, 0, 1, 0, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(46, 'T')]: print('computer_move test 104 failed - with winning move'); win_count += 1

board = [2, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 1, 1, 1, 0, 0, 1, 2, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 0, 1, 0, 2, 1, 1, 1, 2]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (6, 'B'), (6, 'L'), (7, 'T'), (7, 'B'), (7, 'R'), (13, 'T'), (13, 'B'), (13, 'L'), (14, 'T'), (14, 'B'), (14, 'R'), (20, 'T'), (20, 'B'), (20, 'L'), (27, 'T'), (27, 'B'), (27, 'L'), (35, 'T'), (35, 'B'), (35, 'R'), (41, 'T'), (41, 'B'), (41, 'L'), (43, 'T'), (43, 'L'), (43, 'R'), (44, 'T'), (44, 'L'), (44, 'R'), (48, 'T'), (48, 'L')]: print('computer_move test 105 failed - with valid move'); valid_count += 1

board = [0, 0, 2, 1, 0, 1, 0, 2, 0, 1, 1, 2, 2, 0, 1, 0, 0, 2, 0, 2, 2, 1, 0, 2, 1, 0, 1, 0, 2, 2, 0, 2, 2, 2, 0, 2]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(6, 'R'), (18, 'R'), (24, 'R'), (30, 'R'), (34, 'R')]: print('computer_move test 106 failed - with blocking move'); block_count += 1

board = [0, 0, 0, 1, 0, 2, 0, 2, 1, 1, 2, 0, 1, 2, 1, 2, 2, 0, 1, 1, 2, 1, 2, 1, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(14, 'L')]: print('computer_move test 107 failed - with winning move'); win_count += 1

board = [0, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 0, 0, 0, 1, 2, 0, 1, 2, 2, 1, 1, 2, 1, 0, 2, 2, 0, 0, 1, 0, 1, 2, 2, 1, 0, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(13, 'T'), (43, 'T'), (44, 'T'), (45, 'T'), (46, 'T'), (47, 'T'), (48, 'T')]: print('computer_move test 108 failed - with blocking move'); block_count += 1

board = [2, 1, 2, 0, 0, 2, 0, 1, 2, 0, 1, 1, 1, 1, 2, 1, 0, 1, 0, 1, 2, 1, 2, 1, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(14, 'L'), (20, 'T')]: print('computer_move test 109 failed - with blocking move'); block_count += 1

board = [1, 0, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 2, 1, 2, 0, 2, 0, 2, 1, 0, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (6, 'T'), (6, 'B'), (6, 'R'), (17, 'T'), (17, 'B'), (17, 'L'), (18, 'T'), (18, 'B'), (18, 'R'), (23, 'T'), (23, 'B'), (23, 'L'), (30, 'T'), (30, 'R'), (32, 'T'), (32, 'L'), (32, 'R'), (35, 'T'), (35, 'L')]: print('computer_move test 110 failed - with valid move'); valid_count += 1

board = [2, 1, 0, 0, 1, 2, 0, 1, 2, 1, 0, 1, 1, 2, 0, 2, 0, 0, 0, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 0, 2, 0, 1, 2, 2, 2, 0, 1, 0, 1, 0, 0, 2, 0, 1, 1, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (7, 'T'), (7, 'R'), (14, 'T'), (14, 'R'), (21, 'T'), (21, 'R'), (42, 'T'), (42, 'R'), (44, 'L'), (45, 'L'), (46, 'L'), (47, 'L'), (48, 'L')]: print('computer_move test 111 failed - with blocking move'); block_count += 1

board = [0, 1, 2, 0, 1, 0, 1, 1, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (5, 'B'), (5, 'L'), (6, 'T'), (6, 'B'), (18, 'T'), (18, 'B'), (18, 'R'), (23, 'B'), (23, 'L'), (24, 'T'), (24, 'B'), (29, 'B'), (29, 'L'), (30, 'T'), (30, 'R'), (31, 'T'), (31, 'L'), (31, 'R'), (32, 'L'), (32, 'R'), (33, 'T'), (33, 'L'), (33, 'R'), (34, 'L'), (34, 'R'), (35, 'L')]: print('computer_move test 112 failed - with blocking move'); block_count += 1

board = [1, 1, 1, 0, 2, 0, 0, 0, 1, 1, 2, 0, 1, 2, 0, 1, 2, 2, 1, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1, 2, 0, 1, 1, 1, 1, 1, 1]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(28, 'T'), (28, 'R')]: print('computer_move test 113 failed - with winning move'); win_count += 1

board = [2, 2, 2, 0, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2, 2, 1, 1, 0, 0, 2, 2, 1, 0, 1, 2, 0, 0, 2, 2, 1, 0, 0, 1, 2, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(3, 'L'), (3, 'R'), (33, 'T')]: print('computer_move test 114 failed - with winning move'); win_count += 1

board = [1, 1, 0, 1, 2, 1, 2, 1, 1, 2, 0, 0, 2, 0, 1, 2, 2, 1, 2, 1, 2, 1, 2, 0, 2, 1, 2, 1, 2, 0, 0, 2, 1, 0, 2, 1]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(11, 'L')]: print('computer_move test 115 failed - with winning move'); win_count += 1

board = [0, 0, 2, 1, 0, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 0, 2, 2, 0, 1, 1, 2, 1]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(1, 'B')]: print('computer_move test 116 failed - with winning move'); win_count += 1

board = [2, 0, 0, 2, 2, 2, 2, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 2, 2, 1, 0, 0, 0, 0, 2, 0, 1, 2, 0, 2, 1, 2, 2, 0, 0, 0, 2, 0, 0, 1, 1, 1, 2, 0, 1, 1, 1, 0, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (1, 'R'), (2, 'R'), (7, 'B'), (14, 'B'), (14, 'R'), (20, 'T'), (21, 'B'), (21, 'R'), (28, 'B'), (34, 'T'), (35, 'B'), (35, 'R'), (41, 'T'), (41, 'L'), (43, 'L'), (44, 'L'), (45, 'L'), (46, 'T'), (46, 'L'), (47, 'L'), (48, 'T'), (48, 'L')]: print('computer_move test 117 failed - with blocking move'); block_count += 1

board = [2, 1, 0, 1, 0, 1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 2, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'R'), (2, 'L'), (4, 'L'), (10, 'R'), (14, 'L'), (21, 'T')]: print('computer_move test 118 failed - with blocking move'); block_count += 1

board = [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 0, 2, 0, 2, 1, 1, 2, 0, 1, 1, 2, 1, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(4, 'B'), (4, 'L'), (5, 'T'), (5, 'B'), (5, 'R'), (10, 'T'), (10, 'B'), (10, 'R'), (14, 'T'), (14, 'B'), (14, 'L'), (15, 'T'), (15, 'B'), (15, 'R'), (19, 'T'), (19, 'B'), (19, 'L'), (22, 'T'), (22, 'L'), (22, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 119 failed - with valid move'); valid_count += 1

board = [2, 1, 2, 0, 0, 2, 0, 2, 0, 0, 1, 2, 2, 1, 2, 2, 2, 2, 2, 0, 1, 1, 0, 1, 2, 0, 1, 1, 0, 0, 2, 0, 2, 1, 2, 2]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(1, 'B'), (1, 'L'), (1, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (6, 'T'), (6, 'B'), (6, 'R'), (23, 'T'), (23, 'B'), (23, 'L'), (29, 'T'), (29, 'B'), (29, 'L'), (31, 'T'), (31, 'L'), (31, 'R'), (33, 'T'), (33, 'L'), (33, 'R')]: print('computer_move test 120 failed - with valid move'); valid_count += 1

board = [1, 1, 1, 0, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 2, 1, 1, 0, 2, 2, 2, 1, 2, 2, 2, 1, 0, 2, 0, 1, 0, 2, 0, 0, 1, 2]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(3, 'L'), (3, 'R'), (33, 'T')]: print('computer_move test 121 failed - with winning move'); win_count += 1

board = [1, 2, 1, 0, 2, 0, 2, 0, 2, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 2, 1, 1, 1, 1, 0, 2, 0, 1, 1, 1, 2, 0, 2, 2, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(1, 'B'), (31, 'L'), (31, 'R')]: print('computer_move test 122 failed - with winning move'); win_count += 1

board = [0, 0, 2, 1, 2, 0, 2, 2, 1, 2, 1, 2, 2, 0, 0, 0, 2, 2, 0, 1, 0, 2, 0, 2, 0]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (5, 'T'), (5, 'B'), (5, 'R'), (10, 'T'), (10, 'B'), (10, 'R'), (14, 'T'), (14, 'B'), (14, 'L'), (15, 'T'), (15, 'B'), (15, 'R'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R'), (22, 'T'), (22, 'L'), (22, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 123 failed - with valid move'); valid_count += 1

board = [0, 1, 2, 1, 0, 1, 0, 2, 0, 0, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (4, 'B'), (4, 'L'), (9, 'T'), (9, 'B'), (9, 'L'), (10, 'T'), (10, 'B'), (10, 'R'), (14, 'T'), (14, 'B'), (14, 'L'), (19, 'T'), (19, 'B'), (19, 'L'), (23, 'T'), (23, 'L'), (23, 'R')]: print('computer_move test 124 failed - with valid move'); valid_count += 1

board = [0, 2, 1, 2, 1, 0, 2, 2, 2, 1, 2, 1, 2, 1, 0, 1, 1, 2, 2, 0, 0, 1, 0, 1, 2, 1, 0, 1, 2, 0, 2, 2, 1, 1, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B'), (1, 'L')]: print('computer_move test 125 failed - with winning move'); win_count += 1

board = [0, 2, 1, 2, 1, 1, 0, 2, 1, 2, 1, 0, 2, 0, 1, 2, 1, 2, 0, 0, 2, 2, 1, 0, 0, 1, 1, 1, 2, 1, 2, 2, 0, 2, 1, 2]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(29, 'L')]: print('computer_move test 126 failed - with winning move'); win_count += 1

board = [0, 1, 0, 2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2, 0, 1, 0, 2, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 0, 0, 1]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(20, 'L')]: print('computer_move test 127 failed - with winning move'); win_count += 1

board = [0, 2, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 2, 2, 1, 0, 2, 1, 2, 1, 1, 0, 2, 1]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(2, 'L'), (3, 'L'), (4, 'L'), (5, 'T'), (10, 'T'), (15, 'T'), (20, 'T'), (21, 'T')]: print('computer_move test 128 failed - with winning move'); win_count += 1

board = [0, 1, 1, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(23, 'T')]: print('computer_move test 129 failed - with winning move'); win_count += 1

board = [0, 0, 1, 2, 0, 2, 1, 0, 1, 1, 1, 1, 0, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(1, 'B')]: print('computer_move test 130 failed - with winning move'); win_count += 1

board = [0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 1, 0, 1, 0, 2, 2, 0, 0, 2, 0, 1, 0]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (14, 'T'), (14, 'B'), (14, 'L'), (15, 'T'), (15, 'B'), (15, 'R'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R'), (22, 'T'), (22, 'L'), (22, 'R'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 131 failed - with valid move'); valid_count += 1

board = [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 2, 0, 0, 0, 2, 2, 2, 2, 0, 1, 1, 2, 2, 0, 0, 1, 2, 1, 0, 2, 2, 0, 0, 0, 1, 1, 2, 0, 0, 1, 1, 1, 0, 2, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(5, 'B'), (7, 'R'), (13, 'L'), (35, 'R'), (41, 'L'), (42, 'R'), (43, 'R'), (44, 'R'), (45, 'R'), (46, 'R'), (48, 'L')]: print('computer_move test 132 failed - with blocking move'); block_count += 1

board = [0, 2, 0, 2, 2, 2, 0, 1, 1, 2, 2, 1, 1, 0, 1, 2, 0, 1, 2, 1, 1, 1, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 1, 2, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 1, 1, 2]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(43, 'T'), (44, 'T'), (47, 'T')]: print('computer_move test 133 failed - with blocking move'); block_count += 1

board = [1, 2, 0, 2, 2, 2, 2, 1, 2, 0, 1, 0, 2, 1, 1, 0, 2, 2, 0, 2, 1, 1, 2, 1, 0, 1, 0, 1, 1, 0, 0, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 0, 2, 1]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(0, 'R'), (2, 'R'), (41, 'L')]: print('computer_move test 134 failed - with winning move'); win_count += 1

board = [2, 1, 1, 2, 0, 1, 2, 1, 1, 0, 2, 0, 2, 2, 2, 1, 2, 0, 2, 0, 0, 0, 1, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(4, 'B'), (9, 'B'), (14, 'B'), (19, 'B'), (20, 'R'), (21, 'T'), (21, 'R')]: print('computer_move test 135 failed - with winning move'); win_count += 1

board = [2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 1, 1, 2, 2, 0, 2, 1, 2, 1, 0, 1, 2, 0, 2, 1, 1, 0, 0, 2, 1, 0, 0, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(14, 'T'), (35, 'T'), (43, 'T'), (44, 'T'), (45, 'T'), (46, 'T'), (47, 'T')]: print('computer_move test 136 failed - with blocking move'); block_count += 1

board = [2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 0, 2, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 0, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0, 2, 0, 0, 0, 2, 0, 1, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(42, 'T'), (43, 'L'), (44, 'L'), (45, 'L'), (48, 'L')]: print('computer_move test 137 failed - with winning move'); win_count += 1

board = [0, 1, 1, 1, 2, 0, 0, 1, 2, 2, 2, 0, 1, 2, 1, 2, 2, 0, 1, 1, 0, 2, 2, 2, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'R'), (29, 'L')]: print('computer_move test 138 failed - with winning move'); win_count += 1

board = [1, 2, 1, 0, 0, 2, 1, 1, 1, 1, 0, 2, 2, 1, 0, 1, 1, 2, 1, 2, 1, 0, 2, 1, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(1, 'B'), (1, 'L'), (1, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (5, 'T'), (5, 'B'), (5, 'R'), (10, 'T'), (10, 'B'), (10, 'R'), (14, 'T'), (14, 'B'), (14, 'L'), (19, 'T'), (19, 'B'), (19, 'L'), (21, 'T'), (21, 'L'), (21, 'R'), (22, 'T'), (22, 'L'), (22, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 139 failed - with valid move'); valid_count += 1

board = [0, 2, 2, 0, 1, 0, 2, 2, 1, 1, 2, 1, 2, 0, 1, 0, 2, 1, 1, 0, 2, 1, 2, 2, 0, 0, 2, 2, 2, 1, 1, 0, 1, 1, 2, 2, 0, 1, 0, 1, 0, 2, 0, 0, 0, 2, 1, 2, 2]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'R'), (3, 'R'), (4, 'R'), (5, 'R'), (14, 'R'), (21, 'R'), (42, 'R'), (43, 'R'), (44, 'R'), (46, 'R')]: print('computer_move test 140 failed - with blocking move'); block_count += 1

board = [0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 2, 0, 1, 2, 0, 0, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 2, 0, 2, 2, 1, 1, 0, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'R'), (7, 'T'), (21, 'T'), (35, 'T'), (42, 'T')]: print('computer_move test 141 failed - with winning move'); win_count += 1

board = [2, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 0, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (5, 'T'), (5, 'B'), (5, 'R'), (10, 'T'), (10, 'B'), (10, 'R'), (20, 'T'), (20, 'R'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 142 failed - with valid move'); valid_count += 1

board = [1, 1, 0, 0, 1, 1, 2, 1, 2, 1, 0, 1, 1, 2, 0, 1, 1, 1, 2, 2, 0, 1, 1, 0, 1, 1, 2, 2, 1, 2, 1, 0, 1, 2, 2, 1, 0, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(20, 'T'), (20, 'B')]: print('computer_move test 143 failed - with winning move'); win_count += 1

board = [2, 1, 0, 1, 1, 1, 2, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2, 0, 1, 0, 1, 1, 2, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(30, 'T'), (30, 'R'), (31, 'L'), (32, 'L'), (33, 'L'), (34, 'L'), (35, 'L')]: print('computer_move test 144 failed - with winning move'); win_count += 1

board = [0, 0, 0, 1, 2, 0, 1, 0, 1, 0, 2, 2, 1, 0, 1, 0, 2, 2, 1, 0, 1, 1, 0, 2, 1, 1, 0, 2, 0, 2, 1, 2, 1, 1, 2, 1, 1, 2, 0, 1, 0, 1, 0, 2, 0, 2, 1, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'R'), (1, 'B'), (1, 'R'), (2, 'B'), (2, 'R'), (4, 'R'), (5, 'B'), (5, 'R'), (13, 'T'), (13, 'L'), (27, 'T'), (27, 'L'), (28, 'R'), (34, 'T'), (34, 'L'), (43, 'T'), (44, 'T'), (45, 'T'), (48, 'T')]: print('computer_move test 145 failed - with blocking move'); block_count += 1

board = [0, 0, 2, 2, 1, 1, 0, 1, 0, 2, 1, 0, 2, 1, 0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 2, 0, 2, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(32, 'T'), (35, 'T')]: print('computer_move test 146 failed - with blocking move'); block_count += 1

board = [2, 0, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 0, 1, 0, 2, 2, 0, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 2, 1, 0, 0, 1, 0, 1, 1, 2, 1, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (5, 'B'), (5, 'L'), (5, 'R'), (6, 'B'), (6, 'L'), (13, 'B'), (20, 'B'), (20, 'L'), (21, 'T'), (21, 'B'), (21, 'R'), (27, 'B'), (27, 'L'), (28, 'T'), (28, 'B'), (28, 'R'), (34, 'B'), (34, 'L'), (35, 'T'), (35, 'B'), (35, 'R'), (41, 'B'), (41, 'L'), (42, 'T'), (42, 'R'), (43, 'T'), (43, 'L'), (43, 'R'), (44, 'T'), (44, 'L'), (44, 'R'), (46, 'T'), (46, 'L'), (46, 'R'), (47, 'T'), (47, 'L'), (47, 'R'), (48, 'L')]: print('computer_move test 147 failed - with blocking move'); block_count += 1

board = [2, 1, 1, 0, 0, 0, 2, 2, 2, 2, 0, 2, 1, 0, 1, 0, 1, 1, 1, 2, 0, 1, 1, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(5, 'T'), (5, 'R'), (10, 'T'), (15, 'T'), (20, 'T')]: print('computer_move test 148 failed - with winning move'); win_count += 1

board = [0, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(22, 'T')]: print('computer_move test 149 failed - with winning move'); win_count += 1

board = [1, 2, 0, 0, 1, 2, 1, 2, 0, 1, 0, 2, 0, 1, 2, 1, 0, 2, 1, 2, 0, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 0, 2, 1, 0]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(12, 'T'), (12, 'B')]: print('computer_move test 150 failed - with winning move'); win_count += 1

board = [2, 1, 2, 1, 2, 0, 0, 1, 2, 1, 0, 1, 0, 0, 1, 2, 1, 0, 1, 0, 0, 0, 2, 1, 2, 1, 1, 0, 0, 2, 1, 1, 1, 0, 2, 1, 2, 1, 0, 1, 0, 2, 0, 2, 1, 1, 1, 1, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(5, 'B'), (5, 'R'), (6, 'B'), (13, 'T'), (13, 'B'), (13, 'L'), (20, 'T'), (20, 'B'), (20, 'L'), (21, 'T'), (21, 'B'), (27, 'T'), (27, 'B'), (27, 'L'), (28, 'T'), (28, 'B'), (34, 'T'), (34, 'B'), (41, 'T'), (41, 'B'), (41, 'L')]: print('computer_move test 151 failed - with blocking move'); block_count += 1

board = [0, 0, 2, 0, 0, 1, 2, 0, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 0, 2, 2, 1, 0, 0, 2, 2, 2, 1, 0, 0, 1, 1, 2, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(3, 'B'), (18, 'R'), (24, 'R'), (34, 'L'), (35, 'L')]: print('computer_move test 152 failed - with blocking move'); block_count += 1

board = [0, 1, 2, 2, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 2, 2, 1, 2, 0, 2, 2, 2, 2]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(0, 'B'), (5, 'B'), (5, 'R')]: print('computer_move test 153 failed - with winning move'); win_count += 1

board = [2, 1, 2, 1, 1, 1, 2, 0, 1, 1, 0, 1, 1, 2, 1, 1, 2, 2, 2, 0, 1, 2, 2, 2, 2]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(19, 'L')]: print('computer_move test 154 failed - with winning move'); win_count += 1

board = [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 1, 0, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 2, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(41, 'T'), (48, 'T')]: print('computer_move test 155 failed - with winning move'); win_count += 1

board = [2, 2, 2, 0, 1, 0, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 2, 0, 0, 1, 1, 0, 1, 1, 0]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(22, 'T')]: print('computer_move test 156 failed - with winning move'); win_count += 1

board = [2, 1, 2, 2, 2, 0, 0, 2, 2, 0, 2, 1, 0, 0, 1, 0, 2, 1, 2, 0, 1, 2, 2, 1, 1]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(21, 'T')]: print('computer_move test 157 failed - with winning move'); win_count += 1

board = [0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 0, 2, 1, 2, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(4, 'B'), (5, 'B'), (6, 'B'), (13, 'B'), (46, 'T')]: print('computer_move test 158 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2, 1, 0, 0, 1, 2, 2, 0, 1, 0, 0, 1, 1, 2, 0, 0, 0, 1, 1, 2, 2, 1, 1, 2, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'B'), (4, 'B'), (5, 'B'), (28, 'T'), (42, 'T'), (43, 'T'), (46, 'T')]: print('computer_move test 159 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 2, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 2, 0, 1, 1, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'B'), (14, 'R'), (20, 'L'), (34, 'L'), (41, 'L'), (42, 'R'), (44, 'L'), (45, 'L'), (47, 'L'), (48, 'L')]: print('computer_move test 160 failed - with blocking move'); block_count += 1

board = [0, 2, 1, 2, 0, 0, 2, 2, 1, 0, 2, 0, 0, 1, 2, 1, 0, 2, 1, 2, 2, 0, 1, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(5, 'R'), (9, 'T'), (9, 'L'), (10, 'R'), (14, 'T'), (14, 'L'), (19, 'T'), (19, 'L'), (20, 'R'), (21, 'R'), (24, 'T')]: print('computer_move test 161 failed - with blocking move'); block_count += 1

board = [0, 2, 1, 0, 0, 2, 2, 2, 1, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 1, 1, 0, 2, 2, 2, 2, 1, 1, 0, 2, 1, 1, 2, 1, 1, 2]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(30, 'R'), (31, 'R'), (33, 'L'), (34, 'L')]: print('computer_move test 162 failed - with winning move'); win_count += 1

board = [2, 1, 2, 0, 2, 1, 0, 2, 0, 0, 2, 2, 2, 0, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 0, 1, 0, 1, 1, 2, 0, 1, 1, 0, 0, 0, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(1, 'B'), (1, 'L'), (1, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (5, 'B'), (5, 'L'), (5, 'R'), (6, 'B'), (6, 'L'), (13, 'T'), (13, 'B'), (13, 'L'), (21, 'T'), (21, 'B'), (21, 'R'), (27, 'T'), (27, 'B'), (27, 'L'), (28, 'T'), (28, 'B'), (28, 'R'), (34, 'T'), (34, 'B'), (34, 'L'), (35, 'T'), (35, 'B'), (35, 'R'), (41, 'T'), (41, 'B'), (41, 'L'), (44, 'T'), (44, 'L'), (44, 'R')]: print('computer_move test 163 failed - with valid move'); valid_count += 1

board = [2, 2, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 2, 0, 0, 0, 1, 0, 2, 2, 1, 0, 1, 2, 2, 2, 0, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(17, 'L'), (29, 'L')]: print('computer_move test 164 failed - with blocking move'); block_count += 1

board = [2, 2, 2, 0, 2, 1, 1, 0, 1, 2, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 2, 1, 0, 1]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(3, 'L'), (3, 'R'), (23, 'T')]: print('computer_move test 165 failed - with winning move'); win_count += 1

board = [2, 0, 2, 2, 2, 0, 1, 0, 1, 0, 0, 2, 1, 1, 1, 2, 1, 2, 0, 1, 1, 0, 0, 0, 1]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(1, 'L'), (1, 'R'), (21, 'T')]: print('computer_move test 166 failed - with winning move'); win_count += 1

board = [2, 2, 2, 1, 2, 1, 1, 0, 1, 2, 1, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 1, 0]
move = computer_move(board, 1, 2)# valid move exists
if move not in [(3, 'B'), (3, 'L'), (3, 'R'), (5, 'T'), (5, 'B'), (5, 'R'), (10, 'T'), (10, 'B'), (10, 'R'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 167 failed - with valid move'); valid_count += 1

board = [1, 2, 1, 2, 1, 0, 0, 2, 1, 0, 1, 1, 2, 1, 0, 1, 1, 2, 0, 2, 2, 0, 2, 2, 2]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(1, 'B'), (1, 'R'), (3, 'L'), (21, 'L'), (21, 'R')]: print('computer_move test 168 failed - with winning move'); win_count += 1

board = [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 1, 2, 2, 2, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B'), (0, 'R'), (7, 'T'), (14, 'T'), (21, 'T'), (35, 'T'), (42, 'T')]: print('computer_move test 169 failed - with winning move'); win_count += 1

board = [0, 2, 0, 1, 2, 1, 0, 2, 2, 1, 0, 1, 2, 2, 2, 1, 1, 0, 1, 1, 2, 2, 2, 1, 0, 2, 2, 1, 2, 2, 1, 0, 0, 0, 2, 2, 2, 1, 1, 0, 2, 1, 2, 2, 1, 2, 0, 2, 2]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(2, 'B'), (2, 'R')]: print('computer_move test 170 failed - with winning move'); win_count += 1

board = [1, 1, 2, 2, 2, 0, 0, 0, 0, 2, 2, 1, 1, 2, 2, 2, 2, 0, 2, 1, 2, 1, 1, 2, 2, 2, 1, 0, 2, 2, 2, 0, 2, 1, 0, 2]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (31, 'T'), (31, 'L'), (33, 'L'), (34, 'L')]: print('computer_move test 171 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 2, 1, 0, 2, 1, 2, 1, 2, 0, 1, 1, 1, 2, 0, 1, 1, 0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 2, 0, 0, 1, 2, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (3, 'L'), (5, 'B'), (5, 'L'), (6, 'T'), (6, 'B'), (11, 'T'), (11, 'B'), (24, 'T'), (24, 'B'), (24, 'R'), (29, 'T'), (29, 'B'), (29, 'L'), (30, 'T'), (30, 'R'), (31, 'T'), (31, 'L'), (31, 'R'), (33, 'L'), (35, 'T'), (35, 'L')]: print('computer_move test 172 failed - with blocking move'); block_count += 1

board = [0, 2, 2, 2, 0, 1, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 1, 0, 1, 1, 2, 0, 0, 2, 0, 0, 1, 0, 2, 0, 1, 2, 2, 1]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B'), (7, 'B'), (7, 'R')]: print('computer_move test 173 failed - with winning move'); win_count += 1

board = [0, 0, 2, 1, 0, 2, 0, 1, 2, 0, 1, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 0, 2, 0, 2, 2, 1, 2, 0, 0, 0, 2, 0, 0, 1, 2, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(6, 'B'), (13, 'B'), (20, 'B'), (20, 'L')]: print('computer_move test 174 failed - with winning move'); win_count += 1

board = [1, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1, 2, 0, 0, 2, 0, 2, 1, 0, 0, 0, 2, 0, 1, 1, 0, 2, 2, 1, 0, 1, 2, 2, 0, 2]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(5, 'B')]: print('computer_move test 175 failed - with winning move'); win_count += 1

board = [0, 2, 0, 2, 1, 2, 2, 0, 0, 1, 2, 0, 2, 2, 2, 1, 2, 0, 2, 2, 0, 1, 2, 2, 2, 0, 1, 1, 2, 1, 2, 0, 1, 1, 2, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(11, 'L'), (17, 'L'), (29, 'L'), (35, 'L')]: print('computer_move test 176 failed - with blocking move'); block_count += 1

board = [0, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 2, 1, 2, 2, 2, 2, 0, 0, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (5, 'B'), (5, 'L'), (5, 'R'), (6, 'B'), (6, 'L'), (7, 'T'), (7, 'B'), (7, 'R'), (13, 'T'), (13, 'B'), (13, 'L'), (14, 'B'), (21, 'B'), (21, 'R'), (28, 'B'), (28, 'R'), (34, 'T'), (34, 'B'), (34, 'L'), (41, 'T'), (41, 'B'), (41, 'L'), (43, 'T'), (43, 'L'), (43, 'R'), (44, 'T'), (44, 'L'), (44, 'R'), (45, 'T'), (45, 'L'), (45, 'R'), (46, 'T'), (46, 'L'), (46, 'R'), (47, 'T'), (47, 'L'), (47, 'R'), (48, 'T'), (48, 'L')]: print('computer_move test 177 failed - with blocking move'); block_count += 1

board = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 0, 0]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (10, 'T'), (10, 'B'), (10, 'R'), (15, 'T'), (15, 'B'), (15, 'R'), (19, 'T'), (19, 'B'), (19, 'L'), (20, 'T'), (20, 'R'), (21, 'T'), (21, 'L'), (21, 'R'), (23, 'T'), (23, 'L'), (23, 'R'), (24, 'T'), (24, 'L')]: print('computer_move test 178 failed - with valid move'); valid_count += 1

board = [0, 1, 1, 1, 0, 2, 0, 2, 2, 1, 1, 1, 0, 2, 2, 1, 1, 2, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 2, 2, 1, 2, 2, 1, 2, 1, 0, 2, 0, 1, 0, 1, 2, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(4, 'B'), (5, 'B'), (35, 'T'), (42, 'T'), (47, 'T')]: print('computer_move test 179 failed - with blocking move'); block_count += 1

board = [1, 2, 1, 2, 0, 2, 1, 2, 2, 0, 0, 0, 1, 1, 2, 2, 1, 0, 2, 0, 2, 0, 1, 1, 1, 1, 0, 2, 1, 2, 1, 0, 1, 1, 0, 1]
move = computer_move(board, 1, 2)# winning move exists, r1
if move not in [(23, 'L')]: print('computer_move test 180 failed - with winning move'); win_count += 1

board = [0, 1, 2, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 2, 2, 1, 0, 1, 2, 2, 2, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(24, 'L')]: print('computer_move test 181 failed - with winning move'); win_count += 1

board = [1, 1, 0, 1, 2, 0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 1, 2, 2, 2, 2, 2, 0, 0, 1, 2, 0, 2, 0, 0, 0, 1, 2, 1, 2]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(5, 'B'), (11, 'B'), (11, 'L')]: print('computer_move test 182 failed - with winning move'); win_count += 1

board = [0, 0, 1, 1, 2, 1, 2, 2, 0, 1, 2, 1, 1, 0, 1, 0, 0, 2, 2, 2, 0, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 0, 1]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(3, 'B'), (5, 'L'), (13, 'L'), (20, 'L'), (41, 'L'), (43, 'R'), (44, 'R'), (46, 'T'), (46, 'L'), (47, 'L'), (48, 'L')]: print('computer_move test 183 failed - with blocking move'); block_count += 1

board = [0, 2, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 2, 2, 1, 1, 1, 1, 2, 2, 0, 2, 2, 1, 0, 1, 1, 0, 1, 2, 1, 2, 1, 1, 1, 0, 0, 1, 1, 2, 0, 1, 1, 0, 1, 2, 2]
move = computer_move(board, 2, 2)# valid move exists
if move not in [(0, 'B'), (0, 'R'), (1, 'B'), (1, 'L'), (1, 'R'), (2, 'B'), (2, 'L'), (2, 'R'), (3, 'B'), (3, 'L'), (3, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (5, 'B'), (5, 'L'), (5, 'R'), (6, 'B'), (6, 'L'), (13, 'T'), (13, 'B'), (13, 'L'), (14, 'T'), (14, 'B'), (14, 'R'), (20, 'T'), (20, 'B'), (20, 'L'), (21, 'T'), (21, 'B'), (21, 'R'), (41, 'T'), (41, 'B'), (41, 'L'), (42, 'T'), (42, 'R'), (45, 'T'), (45, 'L'), (45, 'R'), (47, 'T'), (47, 'L'), (47, 'R'), (48, 'T'), (48, 'L')]: print('computer_move test 184 failed - with valid move'); valid_count += 1

board = [0, 1, 2, 1, 0, 1, 1, 0, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 0, 1, 1, 2, 2]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(10, 'R'), (14, 'T'), (14, 'L'), (15, 'R'), (19, 'T'), (22, 'T')]: print('computer_move test 185 failed - with blocking move'); block_count += 1

board = [0, 1, 2, 2, 1, 0, 2, 0, 2, 1, 0, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 0, 0, 2, 0, 2, 1, 0, 0, 1, 0, 0, 1]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(0, 'R'), (1, 'R'), (4, 'R'), (5, 'B'), (5, 'L')]: print('computer_move test 186 failed - with winning move'); win_count += 1

board = [1, 2, 2, 2, 0, 2, 2, 1, 1, 1, 2, 0, 0, 0, 2, 1, 2, 2, 0, 1, 0, 2, 2, 1, 2, 0, 1, 2, 2, 0, 2, 2, 1, 1, 2, 2, 0, 1, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'R'), (7, 'R'), (13, 'L')]: print('computer_move test 187 failed - with blocking move'); block_count += 1

board = [0, 0, 2, 2, 0, 2, 1, 1, 0, 0, 0, 1, 1, 2, 1, 0, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 1, 2, 0, 0, 0, 2, 1, 2, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(0, 'B'), (1, 'B'), (6, 'B'), (11, 'B'), (12, 'B'), (24, 'T'), (24, 'R'), (29, 'L'), (30, 'T'), (33, 'T')]: print('computer_move test 188 failed - with blocking move'); block_count += 1

board = [2, 2, 0, 1, 1, 1, 2, 2, 1, 2, 1, 0, 1, 2, 1, 1, 2, 0, 2, 1, 1, 2, 2, 0, 2, 1, 2, 0, 1, 0, 2, 0, 0, 0, 2, 0]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(17, 'L')]: print('computer_move test 189 failed - with winning move'); win_count += 1

board = [2, 0, 0, 2, 2, 2, 2, 1, 2, 1, 2, 0, 2, 2, 1, 2, 2, 0, 1, 1, 0, 1, 2, 1, 1]
move = computer_move(board, 2, 2)# winning move exists, r1
if move not in [(0, 'B'), (5, 'B'), (10, 'B'), (15, 'B'), (20, 'T'), (22, 'L')]: print('computer_move test 190 failed - with winning move'); win_count += 1

board = [2, 0, 0, 1, 0, 1, 0, 2, 2, 2, 1, 1, 0, 0, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 2, 2, 2, 1, 0, 1, 2, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(4, 'B'), (7, 'R'), (35, 'R'), (41, 'L'), (42, 'R'), (43, 'R'), (45, 'R'), (47, 'L')]: print('computer_move test 191 failed - with blocking move'); block_count += 1

board = [0, 2, 1, 2, 0, 1, 2, 2, 2, 2, 2, 1, 1, 0, 1, 2, 1, 1, 1, 1, 0, 2, 2, 0, 2]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B')]: print('computer_move test 192 failed - with winning move'); win_count += 1

board = [0, 1, 1, 2, 1, 0, 0, 0, 2, 1, 2, 2, 2, 1, 0, 1, 1, 1, 0, 1, 2, 1, 2, 1, 2, 2, 0, 1, 0, 1, 1, 0, 0, 2, 2, 2, 0, 1, 0, 0, 1, 2, 1, 1, 2, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(0, 'R'), (7, 'R'), (28, 'R'), (35, 'R'), (41, 'L')]: print('computer_move test 193 failed - with blocking move'); block_count += 1

board = [0, 0, 2, 1, 0, 2, 2, 1, 0, 2, 2, 2, 1, 1, 0, 2, 0, 1, 2, 0, 2, 0, 1, 1, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(0, 'B'), (1, 'L'), (2, 'L'), (4, 'L')]: print('computer_move test 194 failed - with winning move'); win_count += 1

board = [2, 1, 0, 2, 2, 0, 0, 1, 1, 0, 2, 2, 1, 0, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 0, 2, 0, 1, 1, 1, 2, 0, 2, 1, 2, 1, 0, 2, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0]
move = computer_move(board, 2, 2)# winning move exists, r2
if move not in [(41, 'L')]: print('computer_move test 195 failed - with winning move'); win_count += 1

board = [0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 2, 1, 2, 1, 0, 1, 2, 2, 2, 2, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (3, 'B'), (23, 'T')]: print('computer_move test 196 failed - with blocking move'); block_count += 1

board = [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 0, 0, 1, 2, 1, 2, 2, 0, 1, 0, 2, 2, 1, 1, 0, 0, 1, 0, 1, 2, 1, 2, 2, 2, 2, 2]
move = computer_move(board, 1, 2)# winning move exists, r2
if move not in [(1, 'L'), (1, 'R'), (43, 'T')]: print('computer_move test 197 failed - with winning move'); win_count += 1

board = [2, 1, 0, 2, 0, 2, 2, 1, 1, 1, 0, 2, 2, 1, 2, 0, 2, 2, 0, 1, 0, 2, 0, 2, 0]
move = computer_move(board, 1, 2)# blocking move exists
if move not in [(1, 'B'), (10, 'T'), (15, 'T'), (20, 'T'), (20, 'R'), (22, 'L'), (24, 'L')]: print('computer_move test 198 failed - with blocking move'); block_count += 1

board = [0, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 2, 0, 0, 2, 1, 0, 1, 1, 0, 0, 0, 1, 2, 1, 2, 0, 0, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 2, 0, 2, 2, 1, 1]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(20, 'L'), (27, 'L')]: print('computer_move test 199 failed - with blocking move'); block_count += 1

board = [1, 2, 2, 1, 0, 1, 1, 1, 2, 0, 0, 0, 1, 1, 2, 1, 0, 0, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 0, 0, 1, 1, 2, 0, 1, 2, 1, 1, 1, 1, 0, 0, 1, 0, 0, 2, 0]
move = computer_move(board, 2, 2)# blocking move exists
if move not in [(1, 'B'), (1, 'L'), (1, 'R'), (2, 'L'), (2, 'R'), (4, 'B'), (4, 'L'), (4, 'R'), (14, 'T'), (14, 'B'), (14, 'R'), (20, 'T'), (20, 'B'), (20, 'L'), (21, 'T'), (21, 'B'), (21, 'R'), (27, 'T'), (27, 'B'), (27, 'L'), (28, 'T'), (28, 'B'), (28, 'R'), (34, 'T'), (34, 'B'), (34, 'L'), (35, 'T'), (35, 'B'), (35, 'R'), (42, 'T'), (43, 'T'), (43, 'L'), (45, 'T'), (45, 'L'), (46, 'L')]: print('computer_move test 200 failed - with blocking move'); block_count += 1

print(f"winning moves: {93 - win_count} out of 93 passed.")
print(f"blocking moves: {81 - block_count} out of 81 passed.")
print(f"valid moves: {26 - valid_count} out of 26 passed.")
