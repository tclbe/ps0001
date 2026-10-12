from connect4 import *
win_count = 0
block_count = 0
valid_count = 0
board = [1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False), (2, False)]: print('computer_move test 1 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, False)]: print('computer_move test 1 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 0, 1, 2, 1, 0, 1, 2, 0, 2, 2, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 2 failed - with winning move for p1'); win_count += 1

board = [2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 0, 1, 2, 1, 0, 1, 2, 0, 2, 2, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 2 failed - with valid move for p2'); valid_count += 1

board = [0, 2, 2, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 3 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 2, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (4, False)]: print('computer_move test 3 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 2, 1, 1, 1, 2, 2, 0, 1, 1, 2, 1, 2, 0, 0, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(5, True)]: print('computer_move test 4 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 1, 1, 1, 2, 2, 0, 1, 1, 2, 1, 2, 0, 0, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, True), (2, False), (3, True), (3, False), (5, False), (6, False)]: print('computer_move test 4 failed - with valid move for p2'); valid_count += 1

board = [2, 0, 0, 1, 1, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 5 failed - with winning move for p1'); win_count += 1

board = [2, 0, 0, 1, 1, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(2, False)]: print('computer_move test 5 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 2, 1, 0, 1, 2, 2, 1, 1, 1, 0, 1, 0, 1, 1, 2, 1, 0, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, True), (0, False)]: print('computer_move test 6 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 0, 1, 2, 2, 1, 1, 1, 0, 1, 0, 1, 1, 2, 1, 0, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 6 failed - with valid move for p2'); valid_count += 1

board = [0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 7 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (5, False)]: print('computer_move test 7 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 2, 2, 1, 1, 2, 1, 0, 1, 2, 2, 1, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, True), (6, True), (6, False)]: print('computer_move test 8 failed - with blocking move for p1'); block_count += 1

board = [2, 1, 2, 2, 2, 1, 1, 2, 1, 0, 1, 2, 2, 1, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, True), (2, False), (3, True), (3, False), (4, False), (6, False)]: print('computer_move test 8 failed - with blocking move for p2'); block_count += 1

board = [1, 2, 1, 2, 1, 2, 1, 1, 1, 0, 1, 2, 0, 2, 1, 1, 0, 1, 2, 0, 1, 2, 1, 0, 0, 2, 0, 2, 2, 2, 0, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 9 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 2, 1, 2, 1, 1, 1, 0, 1, 2, 0, 2, 1, 1, 0, 1, 2, 0, 1, 2, 1, 0, 0, 2, 0, 2, 2, 2, 0, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 9 failed - with valid move for p2'); valid_count += 1

board = [2, 2, 1, 2, 1, 1, 0, 0, 2, 2, 2, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 10 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 1, 1, 0, 0, 2, 2, 2, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (4, False)]: print('computer_move test 10 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 11 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, True), (2, True)]: print('computer_move test 11 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 0, 2, 1, 1, 1, 2, 2, 0, 1, 1, 1, 0, 2, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(2, False)]: print('computer_move test 12 failed - with blocking move for p1'); block_count += 1

board = [2, 2, 2, 1, 0, 2, 1, 1, 1, 2, 2, 0, 1, 1, 1, 0, 2, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 12 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 0, 2, 2, 0, 1, 2, 2, 0, 2, 1, 0, 1, 2, 2, 0, 1, 0, 0, 2, 2, 1, 0, 2, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(1, False), (2, False), (3, True), (4, True), (4, False), (5, False)]: print('computer_move test 13 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 0, 2, 2, 0, 1, 2, 2, 0, 2, 1, 0, 1, 2, 2, 0, 1, 0, 0, 2, 2, 1, 0, 2, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 13 failed - with winning move for p2'); win_count += 1

board = [1, 2, 0, 1, 2, 1, 1, 1, 2, 0, 2, 2, 1, 2, 1, 1, 0, 2, 1, 2, 2, 2, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(3, False)]: print('computer_move test 14 failed - with blocking move for p1'); block_count += 1

board = [1, 2, 0, 1, 2, 1, 1, 1, 2, 0, 2, 2, 1, 2, 1, 1, 0, 2, 1, 2, 2, 2, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 14 failed - with winning move for p2'); win_count += 1

board = [2, 2, 0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 1, 0, 0, 0, 2, 1, 2, 2, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(6, False)]: print('computer_move test 15 failed - with blocking move for p1'); block_count += 1

board = [2, 2, 0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 1, 0, 0, 0, 2, 1, 2, 2, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(6, False)]: print('computer_move test 15 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 0, 1, 0, 1, 1, 1, 0, 0, 2, 0, 2, 1, 1, 0, 0, 2, 0, 1, 2, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, True), (3, False)]: print('computer_move test 16 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 0, 1, 0, 1, 1, 1, 0, 0, 2, 0, 2, 1, 1, 0, 0, 2, 0, 1, 2, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 16 failed - with valid move for p2'); valid_count += 1

board = [1, 0, 2, 1, 2, 2, 0, 2, 0, 2, 1, 1, 2, 0, 1, 0, 1, 2, 2, 0, 0, 1, 0, 2, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 17 failed - with valid move for p1'); valid_count += 1

board = [1, 0, 2, 1, 2, 2, 0, 2, 0, 2, 1, 1, 2, 0, 1, 0, 1, 2, 2, 0, 0, 1, 0, 2, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, True)]: print('computer_move test 17 failed - with winning move for p2'); win_count += 1

board = [1, 0, 1, 1, 1, 2, 1, 2, 0, 2, 0, 1, 2, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 18 failed - with winning move for p1'); win_count += 1

board = [1, 0, 1, 1, 1, 2, 1, 2, 0, 2, 0, 1, 2, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, False)]: print('computer_move test 18 failed - with blocking move for p2'); block_count += 1

board = [2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 0, 1, 2, 0, 1, 1, 2, 0, 1, 2, 0, 2, 0, 2, 0, 1, 1, 0, 2, 0, 1, 0, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 19 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 0, 1, 2, 0, 1, 1, 2, 0, 1, 2, 0, 2, 0, 2, 0, 1, 1, 0, 2, 0, 1, 0, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False)]: print('computer_move test 19 failed - with winning move for p2'); win_count += 1

board = [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 20 failed - with valid move for p1'); valid_count += 1

board = [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (6, False)]: print('computer_move test 20 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 1, 2, 2, 1, 0, 1, 2, 2, 0, 1, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 0, 1, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (3, True), (3, False), (4, True), (4, False), (5, False)]: print('computer_move test 21 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 2, 1, 1, 2, 2, 1, 0, 1, 2, 2, 0, 1, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 0, 1, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, True)]: print('computer_move test 21 failed - with winning move for p2'); win_count += 1

board = [0, 2, 1, 2, 2, 1, 2, 0, 0, 0, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 2, 0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 22 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 1, 2, 2, 1, 2, 0, 0, 0, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 2, 0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True), (6, False)]: print('computer_move test 22 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 0, 1, 2, 2, 1, 2, 2, 0, 2, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (5, True), (5, False), (6, False)]: print('computer_move test 23 failed - with blocking move for p1'); block_count += 1

board = [2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 0, 1, 2, 2, 1, 2, 2, 0, 2, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, False), (2, False), (3, False), (5, False), (6, False)]: print('computer_move test 23 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 2, 1, 1, 2, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (4, False)]: print('computer_move test 24 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 2, 1, 1, 2, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False)]: print('computer_move test 24 failed - with winning move for p2'); win_count += 1

board = [1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 0, 0, 1, 2, 1, 2, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, True), (4, False)]: print('computer_move test 25 failed - with winning move for p1'); win_count += 1

board = [1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 0, 0, 1, 2, 1, 2, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 25 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False), (4, False), (6, False)]: print('computer_move test 26 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, True), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 26 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 1, 2, 1, 2, 1, 2, 2, 0, 1, 1, 2, 0, 2, 2, 0, 0, 2, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, True), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 27 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 1, 2, 1, 2, 1, 2, 2, 0, 1, 1, 2, 0, 2, 2, 0, 0, 2, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (2, False)]: print('computer_move test 27 failed - with winning move for p2'); win_count += 1

board = [0, 1, 1, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 0, 0, 2, 1, 1, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, True), (6, False)]: print('computer_move test 28 failed - with winning move for p1'); win_count += 1

board = [0, 1, 1, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 0, 0, 2, 1, 1, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (4, False)]: print('computer_move test 28 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 0, 1, 1, 2, 1, 2, 2, 0, 1, 2, 2, 0, 2, 1, 0, 0, 1, 2, 0, 1, 2, 0, 0, 1, 1, 0, 2, 1, 0, 0, 1, 1, 0, 2, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 29 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 0, 1, 1, 2, 1, 2, 2, 0, 1, 2, 2, 0, 2, 1, 0, 0, 1, 2, 0, 1, 2, 0, 0, 1, 1, 0, 2, 1, 0, 0, 1, 1, 0, 2, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 29 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 0, 1, 2, 2, 1, 0, 2, 0, 1, 1, 1, 2, 0, 1, 0, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, True), (3, False), (5, False), (6, True), (6, False)]: print('computer_move test 30 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 0, 1, 2, 2, 1, 0, 2, 0, 1, 1, 1, 2, 0, 1, 0, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(6, False)]: print('computer_move test 30 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 0, 1, 1, 2, 1, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (5, False), (6, False)]: print('computer_move test 31 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 0, 1, 1, 2, 1, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, True)]: print('computer_move test 31 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 1, 2, 2, 1, 0, 2, 1, 2, 2, 1, 1, 0, 2, 0, 0, 1, 2, 2, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(1, True), (2, False)]: print('computer_move test 32 failed - with blocking move for p1'); block_count += 1

board = [2, 1, 2, 1, 2, 2, 1, 0, 2, 1, 2, 2, 1, 1, 0, 2, 0, 0, 1, 2, 2, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 32 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 0, 2, 1, 0, 2, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 2, 2, 0, 0, 0, 1, 0, 0, 1]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, False), (3, True), (4, False), (5, True), (5, False)]: print('computer_move test 33 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 0, 2, 1, 0, 2, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 2, 2, 0, 0, 0, 1, 0, 0, 1]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (4, False)]: print('computer_move test 33 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 0, 2, 1, 1, 1, 2, 2, 0, 1, 2, 2, 1, 1, 1, 0, 1, 2, 2, 1, 0, 2, 0, 1, 1, 1, 2, 0, 1, 0, 2, 2, 1, 2, 0, 1, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False), (4, True)]: print('computer_move test 34 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 0, 2, 1, 1, 1, 2, 2, 0, 1, 2, 2, 1, 1, 1, 0, 1, 2, 2, 1, 0, 2, 0, 1, 1, 1, 2, 0, 1, 0, 2, 2, 1, 2, 0, 1, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, True), (3, True), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 34 failed - with valid move for p2'); valid_count += 1

board = [2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 0, 2, 1, 1, 1, 2, 0, 0, 1, 1, 2, 2, 1, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 35 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 0, 2, 1, 1, 1, 2, 0, 0, 1, 1, 2, 2, 1, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, True)]: print('computer_move test 35 failed - with winning move for p2'); win_count += 1

board = [1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 0, 2, 1, 2, 2, 2, 1, 0, 2, 2, 2, 1, 1, 0, 0, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, True)]: print('computer_move test 36 failed - with winning move for p1'); win_count += 1

board = [1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 0, 2, 1, 2, 2, 2, 1, 0, 2, 2, 2, 1, 1, 0, 0, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, True)]: print('computer_move test 36 failed - with blocking move for p2'); block_count += 1

board = [2, 1, 1, 2, 1, 2, 1, 2, 0, 1, 2, 1, 2, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(4, True)]: print('computer_move test 37 failed - with blocking move for p1'); block_count += 1

board = [2, 1, 1, 2, 1, 2, 1, 2, 0, 1, 2, 1, 2, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True), (5, False)]: print('computer_move test 37 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 0, 2, 1, 1, 2, 1, 2, 0, 2, 2, 2, 0, 2, 1, 0, 1, 1, 2, 0, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(6, False)]: print('computer_move test 38 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 0, 2, 1, 1, 2, 1, 2, 0, 2, 2, 2, 0, 2, 1, 0, 1, 1, 2, 0, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, False)]: print('computer_move test 38 failed - with winning move for p2'); win_count += 1

board = [0, 2, 1, 2, 1, 2, 2, 0, 1, 2, 2, 1, 0, 2, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (4, False)]: print('computer_move test 39 failed - with winning move for p1'); win_count += 1

board = [0, 2, 1, 2, 1, 2, 2, 0, 1, 2, 2, 1, 0, 2, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 39 failed - with valid move for p2'); valid_count += 1

board = [2, 1, 1, 2, 1, 0, 1, 1, 2, 2, 1, 1, 0, 2, 2, 1, 1, 2, 2, 0, 1, 1, 2, 0, 1, 2, 0, 2, 1, 1, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, True), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 40 failed - with blocking move for p1'); block_count += 1

board = [2, 1, 1, 2, 1, 0, 1, 1, 2, 2, 1, 1, 0, 2, 2, 1, 1, 2, 2, 0, 1, 1, 2, 0, 1, 2, 0, 2, 1, 1, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 40 failed - with blocking move for p2'); block_count += 1

board = [0, 2, 1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 2, 2, 0, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False), (5, False)]: print('computer_move test 41 failed - with winning move for p1'); win_count += 1

board = [0, 2, 1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 2, 2, 0, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, False)]: print('computer_move test 41 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 0, 1, 2, 1, 1, 1, 2, 0, 2, 1, 2, 2, 1, 1, 0, 2, 1, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, True)]: print('computer_move test 42 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 0, 1, 2, 1, 1, 1, 2, 0, 2, 1, 2, 2, 1, 1, 0, 2, 1, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 42 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 43 failed - with valid move for p1'); valid_count += 1

board = [1, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, True), (6, False)]: print('computer_move test 43 failed - with winning move for p2'); win_count += 1

board = [0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 2, 1, 2, 2, 0, 0, 0, 1, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 44 failed - with valid move for p1'); valid_count += 1

board = [0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 2, 1, 2, 2, 0, 0, 0, 1, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, True)]: print('computer_move test 44 failed - with winning move for p2'); win_count += 1

board = [1, 2, 2, 1, 2, 2, 0, 1, 0, 2, 2, 1, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 45 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 2, 1, 2, 2, 0, 1, 0, 2, 2, 1, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (4, True)]: print('computer_move test 45 failed - with winning move for p2'); win_count += 1

board = [0, 2, 1, 1, 2, 2, 2, 0, 1, 2, 1, 2, 0, 1, 0, 1, 2, 1, 1, 0, 1, 0, 2, 1, 0, 1, 0, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 2, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, True), (3, False)]: print('computer_move test 46 failed - with winning move for p1'); win_count += 1

board = [0, 2, 1, 1, 2, 2, 2, 0, 1, 2, 1, 2, 0, 1, 0, 1, 2, 1, 1, 0, 1, 0, 2, 1, 0, 1, 0, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 2, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 46 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 2, 1, 2, 1, 0, 1, 2, 2, 1, 1, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 47 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 2, 1, 2, 1, 0, 1, 2, 2, 1, 1, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, False)]: print('computer_move test 47 failed - with winning move for p2'); win_count += 1

board = [0, 1, 1, 1, 2, 0, 1, 0, 1, 1, 2, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 2, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, False), (2, False)]: print('computer_move test 48 failed - with winning move for p1'); win_count += 1

board = [0, 1, 1, 1, 2, 0, 1, 0, 1, 1, 2, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 2, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 48 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 1, 2, 2, 1, 2, 0, 2, 0, 2, 1, 1, 2, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, True), (1, False), (2, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 49 failed - with valid move for p1'); valid_count += 1

board = [1, 1, 1, 2, 2, 1, 2, 0, 2, 0, 2, 1, 1, 2, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False), (6, False)]: print('computer_move test 49 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 50 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (3, False)]: print('computer_move test 50 failed - with winning move for p2'); win_count += 1

board = [1, 2, 2, 2, 1, 2, 2, 0, 2, 1, 2, 2, 1, 2, 0, 0, 1, 1, 2, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 51 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 2, 2, 1, 2, 2, 0, 2, 1, 2, 2, 1, 2, 0, 0, 1, 1, 2, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True), (5, False)]: print('computer_move test 51 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 2, 0, 1, 1, 0, 2, 2, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, True), (1, False)]: print('computer_move test 52 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 2, 0, 1, 1, 0, 2, 2, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, True)]: print('computer_move test 52 failed - with winning move for p2'); win_count += 1

board = [0, 2, 1, 2, 1, 1, 2, 0, 2, 2, 1, 1, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, True), (4, False)]: print('computer_move test 53 failed - with winning move for p1'); win_count += 1

board = [0, 2, 1, 2, 1, 1, 2, 0, 2, 2, 1, 1, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (3, True), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 53 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 0, 1, 2, 2, 1, 2, 0, 0, 2, 1, 1, 1, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 54 failed - with winning move for p1'); win_count += 1

board = [1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 0, 1, 2, 2, 1, 2, 0, 0, 2, 1, 1, 1, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(6, True)]: print('computer_move test 54 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 0, 2, 2, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 55 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 0, 2, 2, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, True)]: print('computer_move test 55 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False), (5, False)]: print('computer_move test 56 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 56 failed - with valid move for p2'); valid_count += 1

board = [2, 2, 1, 2, 1, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2, 1, 0, 1, 2, 0, 1, 1, 1, 0, 1, 2, 0, 2, 0, 2, 0, 2, 1, 0, 1, 0, 1, 0, 2, 2, 0, 2, 0, 1, 0, 1, 1, 0, 2]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (2, True), (2, False), (4, True), (5, False)]: print('computer_move test 57 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 1, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2, 1, 0, 1, 2, 0, 1, 1, 1, 0, 1, 2, 0, 2, 0, 2, 0, 2, 1, 0, 1, 0, 1, 0, 2, 2, 0, 2, 0, 1, 0, 1, 1, 0, 2]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True), (5, False)]: print('computer_move test 57 failed - with winning move for p2'); win_count += 1

board = [1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 0, 1, 2, 2, 0, 1, 2, 0, 1, 1, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 2]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, True), (2, True), (2, False), (5, False), (6, True)]: print('computer_move test 58 failed - with valid move for p1'); valid_count += 1

board = [1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 0, 1, 2, 2, 0, 1, 2, 0, 1, 1, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 2]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (4, True)]: print('computer_move test 58 failed - with winning move for p2'); win_count += 1

board = [2, 0, 1, 2, 2, 0, 2, 1, 0, 2, 2, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 59 failed - with valid move for p1'); valid_count += 1

board = [2, 0, 1, 2, 2, 0, 2, 1, 0, 2, 2, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, False)]: print('computer_move test 59 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 1, 2, 2, 2, 0, 2, 0, 2, 1, 1, 1, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(1, False), (3, True)]: print('computer_move test 60 failed - with blocking move for p1'); block_count += 1

board = [2, 2, 1, 1, 2, 2, 2, 0, 2, 0, 2, 1, 1, 1, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False)]: print('computer_move test 60 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 0, 1, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(2, False)]: print('computer_move test 61 failed - with blocking move for p1'); block_count += 1

board = [1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 0, 1, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 61 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 1, 0, 2, 2, 1, 1, 2, 1, 0, 1, 2, 0, 2, 2, 1, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(4, False)]: print('computer_move test 62 failed - with winning move for p1'); win_count += 1

board = [2, 2, 2, 1, 1, 0, 2, 2, 1, 1, 2, 1, 0, 1, 2, 0, 2, 2, 1, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (1, False)]: print('computer_move test 62 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 0, 1, 2, 1, 2, 1, 1, 0, 2, 2, 1, 2, 1, 2, 0, 2, 2, 1, 1, 2, 1, 0, 2, 1, 2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 2, 2, 1]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 63 failed - with winning move for p1'); win_count += 1

board = [2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 0, 1, 2, 1, 2, 1, 1, 0, 2, 2, 1, 2, 1, 2, 0, 2, 2, 1, 1, 2, 1, 0, 2, 1, 2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 2, 2, 1]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 63 failed - with winning move for p2'); win_count += 1

board = [2, 1, 0, 2, 1, 1, 2, 1, 2, 0, 2, 2, 1, 1, 1, 2, 0, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 2, 0, 2, 0, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(4, False)]: print('computer_move test 64 failed - with winning move for p1'); win_count += 1

board = [2, 1, 0, 2, 1, 1, 2, 1, 2, 0, 2, 2, 1, 1, 1, 2, 0, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 2, 0, 2, 0, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(3, True), (4, False)]: print('computer_move test 64 failed - with blocking move for p2'); block_count += 1

board = [0, 2, 2, 1, 2, 2, 2, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 2, 1, 2, 0, 0, 2, 0, 1, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 65 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 2, 1, 2, 2, 2, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 2, 1, 2, 0, 0, 2, 0, 1, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 65 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 0, 0, 0, 2, 2, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, False)]: print('computer_move test 66 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 0, 0, 0, 2, 2, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, False)]: print('computer_move test 66 failed - with blocking move for p2'); block_count += 1

board = [2, 2, 1, 1, 2, 1, 0, 2, 2, 1, 2, 2, 1, 0, 1, 2, 1, 2, 1, 2, 0, 2, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 67 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 1, 2, 1, 0, 2, 2, 1, 2, 2, 1, 0, 1, 2, 1, 2, 1, 2, 0, 2, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False)]: print('computer_move test 67 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 2, 0, 1, 1, 1, 1, 2, 1, 0, 0, 2, 1, 0, 1, 1, 0, 0, 2, 1, 0, 0, 1, 0, 0, 2, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False), (2, True)]: print('computer_move test 68 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 2, 0, 1, 1, 1, 1, 2, 1, 0, 0, 2, 1, 0, 1, 1, 0, 0, 2, 1, 0, 0, 1, 0, 0, 2, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False)]: print('computer_move test 68 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 2, 2, 1, 1, 1, 0, 0, 1, 1, 2, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(4, False)]: print('computer_move test 69 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 1, 1, 1, 0, 0, 1, 1, 2, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, True), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 69 failed - with valid move for p2'); valid_count += 1

board = [2, 2, 1, 1, 2, 2, 2, 0, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 70 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 1, 2, 2, 2, 0, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (6, False)]: print('computer_move test 70 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 2, 2, 1, 2, 0, 2, 2, 1, 1, 2, 0, 0, 1, 1, 2, 2, 2, 0, 0, 1, 2, 1, 1, 1, 0, 0, 2, 2, 1, 2, 1, 0, 0, 0, 2, 2, 1, 2, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (5, True), (6, False)]: print('computer_move test 71 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 2, 1, 2, 0, 2, 2, 1, 1, 2, 0, 0, 1, 1, 2, 2, 2, 0, 0, 1, 2, 1, 1, 1, 0, 0, 2, 2, 1, 2, 1, 0, 0, 0, 2, 2, 1, 2, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True)]: print('computer_move test 71 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False), (3, True), (3, False)]: print('computer_move test 72 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False)]: print('computer_move test 72 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 0, 2, 1, 1, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 73 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 0, 2, 1, 1, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (4, False)]: print('computer_move test 73 failed - with winning move for p2'); win_count += 1

board = [1, 2, 0, 1, 2, 1, 1, 2, 1, 0, 1, 1, 1, 2, 2, 1, 0, 1, 2, 1, 1, 0, 2, 0, 2, 1, 2, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(6, True), (6, False)]: print('computer_move test 74 failed - with winning move for p1'); win_count += 1

board = [1, 2, 0, 1, 2, 1, 1, 2, 1, 0, 1, 1, 1, 2, 2, 1, 0, 1, 2, 1, 1, 0, 2, 0, 2, 1, 2, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 74 failed - with valid move for p2'); valid_count += 1

board = [0, 1, 1, 2, 1, 1, 1, 0, 1, 0, 1, 2, 2, 1, 0, 2, 0, 1, 2, 1, 2, 0, 1, 0, 0, 1, 2, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 75 failed - with winning move for p1'); win_count += 1

board = [0, 1, 1, 2, 1, 1, 1, 0, 1, 0, 1, 2, 2, 1, 0, 2, 0, 1, 2, 1, 2, 0, 1, 0, 0, 1, 2, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 75 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 2, 2, 1, 0, 2, 2, 1, 2, 2, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 76 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 2, 2, 1, 0, 2, 2, 1, 2, 2, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, True)]: print('computer_move test 76 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 2, 0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(2, False)]: print('computer_move test 77 failed - with blocking move for p1'); block_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 2, 0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 77 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 2, 2, 0, 1, 0, 2, 1, 2, 2, 0, 1, 0, 2, 2, 0, 2, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (2, True), (2, False), (3, False), (5, False), (6, True), (6, False)]: print('computer_move test 78 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 2, 0, 1, 0, 2, 1, 2, 2, 0, 1, 0, 2, 2, 0, 2, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, True), (3, False)]: print('computer_move test 78 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 0, 2, 2, 2, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 79 failed - with valid move for p1'); valid_count += 1

board = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 0, 2, 2, 2, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (4, False)]: print('computer_move test 79 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 0, 2, 1, 2, 1, 1, 0, 0, 2, 2, 0, 1, 2, 0, 0, 1, 1, 0, 1, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(3, False)]: print('computer_move test 80 failed - with blocking move for p1'); block_count += 1

board = [2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 0, 2, 1, 2, 1, 1, 0, 0, 2, 2, 0, 1, 2, 0, 0, 1, 1, 0, 1, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 80 failed - with winning move for p2'); win_count += 1

board = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, False), (4, False)]: print('computer_move test 81 failed - with winning move for p1'); win_count += 1

board = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 81 failed - with valid move for p2'); valid_count += 1

board = [2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 0, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 0, 2, 2, 0, 2, 2, 2, 0, 2, 1, 0, 1, 0, 2, 0, 2, 1, 0, 2, 0, 2, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (2, True), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 82 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 0, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 0, 2, 2, 0, 2, 2, 2, 0, 2, 1, 0, 1, 0, 2, 0, 2, 1, 0, 2, 0, 2, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, True)]: print('computer_move test 82 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 1, 1, 2, 1, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(5, True)]: print('computer_move test 83 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 1, 1, 2, 1, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 83 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 0, 1, 2, 2, 1, 2, 2, 0, 2, 1, 2, 0, 1, 0, 0, 1, 2, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, True)]: print('computer_move test 84 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 0, 1, 2, 2, 1, 2, 2, 0, 2, 1, 2, 0, 1, 0, 0, 1, 2, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(5, True), (6, False)]: print('computer_move test 84 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 0, 1, 2, 1, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 85 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 0, 1, 2, 1, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(2, False), (5, True)]: print('computer_move test 85 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 0, 1, 2, 1, 2, 1, 2, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 2, 0, 1, 1, 0, 1, 2, 1, 0, 2, 0, 0, 2, 1, 2, 0, 2, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (3, True), (5, False)]: print('computer_move test 86 failed - with winning move for p1'); win_count += 1

board = [1, 1, 0, 1, 2, 1, 2, 1, 2, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 2, 0, 1, 1, 0, 1, 2, 1, 0, 2, 0, 0, 2, 1, 2, 0, 2, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 86 failed - with valid move for p2'); valid_count += 1

board = [2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(5, False)]: print('computer_move test 87 failed - with winning move for p1'); win_count += 1

board = [2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, True), (5, False)]: print('computer_move test 87 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 0, 1, 2, 2, 0, 1, 2, 0, 2, 1, 1, 0, 1, 2, 0, 2, 2, 0, 0, 1, 1, 0, 2, 2, 0, 0, 2, 2, 0, 1, 2, 0, 0, 2, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(4, False)]: print('computer_move test 88 failed - with winning move for p1'); win_count += 1

board = [2, 2, 2, 0, 1, 2, 2, 0, 1, 2, 0, 2, 1, 1, 0, 1, 2, 0, 2, 2, 0, 0, 1, 1, 0, 2, 2, 0, 0, 2, 2, 0, 1, 2, 0, 0, 2, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 88 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 2, 2, 1, 1, 0, 2, 1, 2, 1, 2, 1, 0, 0, 2, 2, 1, 1, 1, 0, 0, 1, 1, 1, 0, 2, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(6, True), (6, False)]: print('computer_move test 89 failed - with winning move for p1'); win_count += 1

board = [2, 2, 2, 1, 2, 2, 1, 1, 0, 2, 1, 2, 1, 2, 1, 0, 0, 2, 2, 1, 1, 1, 0, 0, 1, 1, 1, 0, 2, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, True), (2, False), (3, False), (4, True), (5, True), (5, False), (6, False)]: print('computer_move test 89 failed - with valid move for p2'); valid_count += 1

board = [2, 0, 1, 1, 2, 1, 1, 1, 0, 2, 1, 2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(5, False)]: print('computer_move test 90 failed - with winning move for p1'); win_count += 1

board = [2, 0, 1, 1, 2, 1, 1, 1, 0, 2, 1, 2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 90 failed - with valid move for p2'); valid_count += 1

board = [1, 0, 2, 1, 2, 0, 2, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 91 failed - with valid move for p1'); valid_count += 1

board = [1, 0, 2, 1, 2, 0, 2, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, False)]: print('computer_move test 91 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 92 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False), (5, False)]: print('computer_move test 92 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 1, 1, 0, 2, 2, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, True)]: print('computer_move test 93 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 1, 1, 0, 2, 2, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, False)]: print('computer_move test 93 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 1, 2, 1, 1, 1, 2, 0, 2, 0, 2, 1, 2, 1, 0, 2, 0, 1, 2, 0, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, True)]: print('computer_move test 94 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 1, 2, 1, 1, 1, 2, 0, 2, 0, 2, 1, 2, 1, 0, 2, 0, 1, 2, 0, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 94 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 0, 1, 1, 1, 0, 0, 1, 0, 2, 1, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (6, False)]: print('computer_move test 95 failed - with winning move for p1'); win_count += 1

board = [2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 0, 1, 1, 1, 0, 0, 1, 0, 2, 1, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, True), (2, False), (3, False), (4, True), (6, False)]: print('computer_move test 95 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 0, 1, 2, 1, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 96 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 0, 1, 2, 1, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True), (5, True)]: print('computer_move test 96 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 2, 2, 1, 1, 2, 0, 2, 1, 2, 2, 2, 2, 0, 1, 2, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 97 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 2, 1, 1, 2, 0, 2, 1, 2, 2, 2, 2, 0, 1, 2, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, False), (3, True)]: print('computer_move test 97 failed - with blocking move for p2'); block_count += 1

board = [2, 2, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (6, False)]: print('computer_move test 98 failed - with winning move for p1'); win_count += 1

board = [2, 2, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 98 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 0, 2, 2, 1, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(5, False)]: print('computer_move test 99 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 0, 2, 2, 1, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(2, True), (5, False)]: print('computer_move test 99 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 0, 0, 2, 1, 2, 0, 1, 0, 0, 2, 2, 2, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(0, True), (0, False), (1, False), (3, False), (4, False)]: print('computer_move test 100 failed - with blocking move for p1'); block_count += 1

board = [1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 0, 0, 2, 1, 2, 0, 1, 0, 0, 2, 2, 2, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, True), (6, False)]: print('computer_move test 100 failed - with blocking move for p2'); block_count += 1

board = [2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 0, 1, 1, 2, 2, 1, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 1, 1, 2, 1, 1, 0, 2, 2, 2, 1, 0, 1, 0, 2, 1, 2, 2, 0, 1, 0, 1, 2, 2, 1, 0, 2, 0, 1, 1, 1, 0, 0, 2, 0, 1, 2, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, True)]: print('computer_move test 101 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 0, 1, 1, 2, 2, 1, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 1, 1, 2, 1, 1, 0, 2, 2, 2, 1, 0, 1, 0, 2, 1, 2, 2, 0, 1, 0, 1, 2, 2, 1, 0, 2, 0, 1, 1, 1, 0, 0, 2, 0, 1, 2, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 101 failed - with winning move for p2'); win_count += 1

board = [0, 2, 1, 1, 2, 1, 2, 0, 1, 2, 2, 2, 0, 1, 0, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 102 failed - with winning move for p1'); win_count += 1

board = [0, 2, 1, 1, 2, 1, 2, 0, 1, 2, 2, 2, 0, 1, 0, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, True), (4, False), (5, False)]: print('computer_move test 102 failed - with winning move for p2'); win_count += 1

board = [0, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(5, False)]: print('computer_move test 103 failed - with blocking move for p1'); block_count += 1

board = [0, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, False)]: print('computer_move test 103 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 1, 2, 0, 2, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 104 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 1, 2, 0, 2, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(2, False)]: print('computer_move test 104 failed - with blocking move for p2'); block_count += 1

board = [2, 1, 2, 1, 0, 2, 2, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 2, 0, 1, 0, 2, 2, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 105 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 1, 0, 2, 2, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 2, 0, 1, 0, 2, 2, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (3, False)]: print('computer_move test 105 failed - with winning move for p2'); win_count += 1

board = [2, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(6, False)]: print('computer_move test 106 failed - with winning move for p1'); win_count += 1

board = [2, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(6, False)]: print('computer_move test 106 failed - with blocking move for p2'); block_count += 1

board = [0, 2, 2, 2, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 107 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 2, 2, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (4, False)]: print('computer_move test 107 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 1, 2, 2, 2, 0, 1, 1, 2, 0, 2, 2, 0, 2, 1, 1, 0, 1, 1, 0, 2, 2, 2, 0, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 108 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 1, 2, 2, 2, 0, 1, 1, 2, 0, 2, 2, 0, 2, 1, 1, 0, 1, 1, 0, 2, 2, 2, 0, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, True), (4, False)]: print('computer_move test 108 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 1, 0, 0, 1, 2, 1, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, True)]: print('computer_move test 109 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 1, 0, 0, 1, 2, 1, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 109 failed - with valid move for p2'); valid_count += 1

board = [2, 1, 2, 2, 1, 1, 1, 1, 0, 2, 2, 2, 0, 2, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(4, True)]: print('computer_move test 110 failed - with blocking move for p1'); block_count += 1

board = [2, 1, 2, 2, 1, 1, 1, 1, 0, 2, 2, 2, 0, 2, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (5, False)]: print('computer_move test 110 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 0, 1, 2, 1, 0, 1, 0, 0, 1, 1, 2, 0, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 111 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 0, 1, 2, 1, 0, 1, 0, 0, 1, 1, 2, 0, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, True), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 111 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 0, 1, 1, 1, 0, 2, 1, 0, 2, 0, 2, 0, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (6, False)]: print('computer_move test 112 failed - with winning move for p1'); win_count += 1

board = [1, 2, 0, 1, 1, 1, 0, 2, 1, 0, 2, 0, 2, 0, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 112 failed - with valid move for p2'); valid_count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 0, 2, 1, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(4, True)]: print('computer_move test 113 failed - with blocking move for p1'); block_count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 0, 2, 1, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (2, False)]: print('computer_move test 113 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 0, 2, 1, 2, 1, 1, 1, 0, 2, 2, 1, 0, 2, 1, 0, 1, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, False), (2, False)]: print('computer_move test 114 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 0, 2, 1, 2, 1, 1, 1, 0, 2, 2, 1, 0, 2, 1, 0, 1, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True)]: print('computer_move test 114 failed - with valid move for p2'); valid_count += 1

board = [2, 0, 1, 1, 2, 1, 2, 0, 0, 2, 2, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (5, False)]: print('computer_move test 115 failed - with winning move for p1'); win_count += 1

board = [2, 0, 1, 1, 2, 1, 2, 0, 0, 2, 2, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 115 failed - with valid move for p2'); valid_count += 1

board = [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 1, 2, 2, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(5, False)]: print('computer_move test 116 failed - with winning move for p1'); win_count += 1

board = [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 1, 2, 2, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True), (3, False)]: print('computer_move test 116 failed - with winning move for p2'); win_count += 1

board = [2, 0, 2, 1, 2, 1, 2, 1, 0, 2, 2, 2, 1, 2, 0, 0, 1, 1, 2, 2, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 117 failed - with valid move for p1'); valid_count += 1

board = [2, 0, 2, 1, 2, 1, 2, 1, 0, 2, 2, 2, 1, 2, 0, 0, 1, 1, 2, 2, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, False), (5, False)]: print('computer_move test 117 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 0, 1, 1, 2, 2, 1, 0, 0, 2, 1, 2, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 118 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 0, 1, 1, 2, 2, 1, 0, 0, 2, 1, 2, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (3, False)]: print('computer_move test 118 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 2, 1, 1, 0, 2, 1, 1, 2, 2, 0, 0, 0, 1, 1, 1, 2, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, False), (4, True)]: print('computer_move test 119 failed - with winning move for p1'); win_count += 1

board = [2, 2, 1, 2, 1, 1, 0, 2, 1, 1, 2, 2, 0, 0, 0, 1, 1, 1, 2, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(3, True)]: print('computer_move test 119 failed - with blocking move for p2'); block_count += 1

board = [1, 2, 2, 1, 1, 2, 2, 2, 1, 0, 2, 2, 2, 1, 1, 2, 0, 2, 2, 0, 2, 2, 2, 0, 1, 1, 0, 0, 1, 2, 0, 2, 2, 0, 0, 1, 1, 0, 2, 2, 0, 0, 1, 1, 0, 2, 1, 0, 0, 2, 2, 0, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (1, False), (2, False), (3, True), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 120 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 2, 1, 1, 2, 2, 2, 1, 0, 2, 2, 2, 1, 1, 2, 0, 2, 2, 0, 2, 2, 2, 0, 1, 1, 0, 0, 1, 2, 0, 2, 2, 0, 0, 1, 1, 0, 2, 2, 0, 0, 1, 1, 0, 2, 1, 0, 0, 2, 2, 0, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (5, False), (6, True)]: print('computer_move test 120 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 1, 2, 2, 2, 0, 1, 1, 2, 1, 1, 0, 0, 1, 1, 2, 2, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (3, False)]: print('computer_move test 121 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 1, 2, 2, 2, 0, 1, 1, 2, 1, 1, 0, 0, 1, 1, 2, 2, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 121 failed - with valid move for p2'); valid_count += 1

board = [2, 2, 1, 2, 2, 1, 2, 1, 2, 0, 1, 2, 2, 2, 1, 1, 0, 2, 1, 2, 0, 2, 0, 0, 1, 1, 2, 0, 2, 0, 0, 2, 2, 1, 0, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 122 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 2, 1, 2, 1, 2, 0, 1, 2, 2, 2, 1, 1, 0, 2, 1, 2, 0, 2, 0, 0, 1, 1, 2, 0, 2, 0, 0, 2, 2, 1, 0, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True), (4, True), (6, False)]: print('computer_move test 122 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 2, 1, 1, 2, 0, 1, 0, 1, 2, 1, 1, 0, 2, 0, 2, 1, 2, 1, 0, 1, 0, 1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (3, True), (4, False)]: print('computer_move test 123 failed - with winning move for p1'); win_count += 1

board = [2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 2, 1, 1, 2, 0, 1, 0, 1, 2, 1, 1, 0, 2, 0, 2, 1, 2, 1, 0, 1, 0, 1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 123 failed - with valid move for p2'); valid_count += 1

board = [2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 0, 2, 0, 2, 2, 1, 1, 0, 1, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 124 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 0, 2, 0, 2, 2, 1, 1, 0, 1, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, True), (3, False)]: print('computer_move test 124 failed - with winning move for p2'); win_count += 1

board = [1, 1, 0, 1, 2, 2, 2, 2, 1, 0, 1, 1, 1, 2, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 2, 2, 2, 0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 125 failed - with winning move for p1'); win_count += 1

board = [1, 1, 0, 1, 2, 2, 2, 2, 1, 0, 1, 1, 1, 2, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 2, 2, 2, 0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 125 failed - with valid move for p2'); valid_count += 1

board = [0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 126 failed - with valid move for p1'); valid_count += 1

board = [0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (6, False)]: print('computer_move test 126 failed - with winning move for p2'); win_count += 1

board = [0, 2, 2, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 127 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 2, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (4, False)]: print('computer_move test 127 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 1, 2, 1, 2, 0, 2, 2, 1, 1, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 128 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 2, 1, 1, 2, 1, 2, 0, 2, 2, 1, 1, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (5, False)]: print('computer_move test 128 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, True)]: print('computer_move test 129 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, False)]: print('computer_move test 129 failed - with winning move for p2'); win_count += 1

board = [2, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (6, False)]: print('computer_move test 130 failed - with winning move for p1'); win_count += 1

board = [2, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 130 failed - with valid move for p2'); valid_count += 1

board = [2, 2, 1, 1, 1, 2, 1, 0, 1, 1, 2, 2, 1, 0, 0, 1, 2, 1, 1, 2, 0, 0, 1, 1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, True), (3, False)]: print('computer_move test 131 failed - with winning move for p1'); win_count += 1

board = [2, 2, 1, 1, 1, 2, 1, 0, 1, 1, 2, 2, 1, 0, 0, 1, 2, 1, 1, 2, 0, 0, 1, 1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 131 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 0, 2, 1, 2, 2, 0, 1, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False), (3, True)]: print('computer_move test 132 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 0, 2, 1, 2, 2, 0, 1, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 132 failed - with winning move for p2'); win_count += 1

board = [1, 2, 2, 1, 0, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 0, 2, 2, 0, 1, 2, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 133 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 2, 1, 0, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 0, 2, 2, 0, 1, 2, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (2, False)]: print('computer_move test 133 failed - with winning move for p2'); win_count += 1

board = [2, 0, 2, 1, 1, 2, 1, 2, 0, 2, 2, 1, 2, 0, 2, 0, 0, 2, 1, 1, 0, 1, 0, 0, 1, 2, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 134 failed - with valid move for p1'); valid_count += 1

board = [2, 0, 2, 1, 1, 2, 1, 2, 0, 2, 2, 1, 2, 0, 2, 0, 0, 2, 1, 1, 0, 1, 0, 0, 1, 2, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (5, False)]: print('computer_move test 134 failed - with winning move for p2'); win_count += 1

board = [1, 0, 1, 1, 1, 2, 2, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 135 failed - with winning move for p1'); win_count += 1

board = [1, 0, 1, 1, 1, 2, 2, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, False)]: print('computer_move test 135 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 0, 2, 2, 1, 2, 0, 2, 0, 1, 1, 2, 1, 0, 2, 0, 0, 0, 1, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 136 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 1, 2, 2, 0, 2, 2, 1, 2, 0, 2, 0, 1, 1, 2, 1, 0, 2, 0, 0, 0, 1, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 136 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 0, 2, 2, 2, 0, 1, 2, 0, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(1, True), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True)]: print('computer_move test 137 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 0, 2, 2, 2, 0, 1, 2, 0, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True)]: print('computer_move test 137 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 0, 2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 138 failed - with winning move for p1'); win_count += 1

board = [2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 0, 2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 138 failed - with winning move for p2'); win_count += 1

board = [1, 0, 2, 2, 1, 2, 2, 2, 0, 1, 1, 2, 2, 2, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 139 failed - with valid move for p1'); valid_count += 1

board = [1, 0, 2, 2, 1, 2, 2, 2, 0, 1, 1, 2, 2, 2, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, True)]: print('computer_move test 139 failed - with winning move for p2'); win_count += 1

board = [1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 2, 0, 0, 1, 2, 1, 2, 2, 0, 0, 1, 2, 1, 1, 1, 0, 0, 2, 1, 2, 2, 2, 0, 0, 1, 2, 2, 1, 1, 0, 0, 2, 1, 1, 1, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 140 failed - with blocking move for p1'); block_count += 1

board = [1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 2, 0, 0, 1, 2, 1, 2, 2, 0, 0, 1, 2, 1, 1, 1, 0, 0, 2, 1, 2, 2, 2, 0, 0, 1, 2, 2, 1, 1, 0, 0, 2, 1, 1, 1, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, False), (1, True), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 140 failed - with blocking move for p2'); block_count += 1

board = [0, 2, 1, 2, 2, 2, 1, 0, 1, 2, 1, 2, 2, 2, 0, 1, 2, 1, 2, 1, 2, 0, 0, 2, 2, 1, 0, 1, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 141 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 1, 2, 2, 2, 1, 0, 1, 2, 1, 2, 2, 2, 0, 1, 2, 1, 2, 1, 2, 0, 0, 2, 2, 1, 0, 1, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (3, True)]: print('computer_move test 141 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 1, 2, 0, 2, 2, 2, 2, 1, 1, 0, 1, 0, 2, 1, 2, 2, 0, 1, 0, 2, 2, 1, 2, 0, 2, 0, 1, 2, 1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False), (3, False)]: print('computer_move test 142 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 1, 2, 0, 2, 2, 2, 2, 1, 1, 0, 1, 0, 2, 1, 2, 2, 0, 1, 0, 2, 2, 1, 2, 0, 2, 0, 1, 2, 1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 142 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 2, 0, 2, 0, 2, 2, 2, 1, 0, 1, 0, 1, 0, 2, 2, 0, 1, 0, 1, 0, 1, 2, 0, 2, 0, 0, 0, 2, 1]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, True), (2, False), (3, False), (4, False), (5, True)]: print('computer_move test 143 failed - with valid move for p1'); valid_count += 1

board = [1, 1, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 2, 0, 2, 0, 2, 2, 2, 1, 0, 1, 0, 1, 0, 2, 2, 0, 1, 0, 1, 0, 1, 2, 0, 2, 0, 0, 0, 2, 1]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (3, True), (4, True)]: print('computer_move test 143 failed - with winning move for p2'); win_count += 1

board = [1, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(6, False)]: print('computer_move test 144 failed - with winning move for p1'); win_count += 1

board = [1, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(6, False)]: print('computer_move test 144 failed - with blocking move for p2'); block_count += 1

board = [2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 0, 2, 2, 1, 2, 0, 2, 0, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 1, 1, 0, 2, 0, 1, 0, 0, 2, 0, 1, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 145 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 0, 2, 2, 1, 2, 0, 2, 0, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 1, 1, 0, 2, 0, 1, 0, 0, 2, 0, 1, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, True)]: print('computer_move test 145 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 0, 2, 2, 0, 1, 2, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(3, True)]: print('computer_move test 146 failed - with blocking move for p1'); block_count += 1

board = [1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 0, 2, 2, 0, 1, 2, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, False), (6, False)]: print('computer_move test 146 failed - with winning move for p2'); win_count += 1

board = [2, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False), (5, False)]: print('computer_move test 147 failed - with winning move for p1'); win_count += 1

board = [2, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 147 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 1, 2, 2, 2, 1, 1, 0, 1, 2, 1, 2, 1, 2, 0, 2, 2, 2, 1, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(5, False)]: print('computer_move test 148 failed - with blocking move for p1'); block_count += 1

board = [1, 1, 1, 2, 2, 2, 1, 1, 0, 1, 2, 1, 2, 1, 2, 0, 2, 2, 2, 1, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(5, True)]: print('computer_move test 148 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 2, 2, 1, 1, 2, 0, 2, 1, 1, 2, 1, 0, 0, 2, 1, 2, 1, 2, 0, 0, 2, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 149 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 2, 1, 2, 2, 1, 1, 2, 0, 2, 1, 1, 2, 1, 0, 0, 2, 1, 2, 1, 2, 0, 0, 2, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 149 failed - with winning move for p2'); win_count += 1

board = [0, 2, 0, 1, 2, 2, 2, 0, 1, 0, 2, 2, 1, 1, 0, 1, 0, 0, 2, 2, 2, 0, 2, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 150 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 0, 1, 2, 2, 2, 0, 1, 0, 2, 2, 1, 1, 0, 1, 0, 0, 2, 2, 2, 0, 2, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (3, False), (6, True)]: print('computer_move test 150 failed - with winning move for p2'); win_count += 1

board = [1, 2, 2, 0, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 151 failed - with winning move for p1'); win_count += 1

board = [1, 2, 2, 0, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 151 failed - with winning move for p2'); win_count += 1

board = [1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 0, 1, 1, 0, 2, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, False), (1, False)]: print('computer_move test 152 failed - with winning move for p1'); win_count += 1

board = [1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 0, 1, 1, 0, 2, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (4, False)]: print('computer_move test 152 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 2, 2, 2, 1, 0, 2, 2, 1, 2, 2, 1, 0, 0, 2, 1, 2, 1, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(2, False)]: print('computer_move test 153 failed - with blocking move for p1'); block_count += 1

board = [1, 2, 1, 2, 2, 2, 1, 0, 2, 2, 1, 2, 2, 1, 0, 0, 2, 1, 2, 1, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 153 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 0, 0, 2, 1, 2, 1, 1, 0, 0, 1, 2, 2, 2, 2, 0, 0, 1, 2, 1, 2, 1, 0, 0, 1, 2, 2, 1, 2, 0, 0, 2, 1, 0, 2]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 154 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 0, 0, 2, 1, 2, 1, 1, 0, 0, 1, 2, 2, 2, 2, 0, 0, 1, 2, 1, 2, 1, 0, 0, 1, 2, 2, 1, 2, 0, 0, 2, 1, 0, 2]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, False)]: print('computer_move test 154 failed - with blocking move for p2'); block_count += 1

board = [2, 0, 2, 2, 1, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 155 failed - with valid move for p1'); valid_count += 1

board = [2, 0, 2, 2, 1, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (2, False), (6, False)]: print('computer_move test 155 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 2, 1, 0, 2, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 156 failed - with winning move for p1'); win_count += 1

board = [2, 1, 2, 2, 1, 0, 2, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, False)]: print('computer_move test 156 failed - with blocking move for p2'); block_count += 1

board = [2, 1, 0, 1, 1, 2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 157 failed - with winning move for p1'); win_count += 1

board = [2, 1, 0, 1, 1, 2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(2, False)]: print('computer_move test 157 failed - with blocking move for p2'); block_count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 0, 2, 1, 2, 2, 1, 2, 0, 2, 1, 1, 1, 0, 1, 0, 1, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False), (4, False), (5, False)]: print('computer_move test 158 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 0, 2, 1, 2, 2, 1, 2, 0, 2, 1, 1, 1, 0, 1, 0, 1, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 158 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 159 failed - with valid move for p1'); valid_count += 1

board = [1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, True), (1, False)]: print('computer_move test 159 failed - with winning move for p2'); win_count += 1

board = [1, 1, 1, 2, 1, 1, 1, 0, 2, 0, 1, 2, 2, 0, 0, 1, 0, 2, 1, 1, 0, 0, 1, 0, 1, 1, 2, 0, 0, 2, 0, 1, 2, 2, 0, 0, 1, 0, 2, 1, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(5, True), (6, False)]: print('computer_move test 160 failed - with winning move for p1'); win_count += 1

board = [1, 1, 1, 2, 1, 1, 1, 0, 2, 0, 1, 2, 2, 0, 0, 1, 0, 2, 1, 1, 0, 0, 1, 0, 1, 1, 2, 0, 0, 2, 0, 1, 2, 2, 0, 0, 1, 0, 2, 1, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (2, False), (3, True), (4, False), (5, False), (6, False)]: print('computer_move test 160 failed - with valid move for p2'); valid_count += 1

board = [2, 1, 2, 2, 2, 1, 0, 2, 2, 1, 0, 1, 2, 0, 1, 1, 2, 0, 2, 2, 0, 2, 2, 1, 0, 1, 2, 0, 1, 2, 2, 0, 2, 1, 0, 2, 2, 1, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(1, True), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 161 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 2, 2, 1, 0, 2, 2, 1, 0, 1, 2, 0, 1, 1, 2, 0, 2, 2, 0, 2, 2, 1, 0, 1, 2, 0, 1, 2, 2, 0, 2, 1, 0, 2, 2, 1, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 161 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 1, 1, 1, 2, 0, 0, 0, 1, 1, 1, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 162 failed - with winning move for p1'); win_count += 1

board = [2, 1, 2, 1, 1, 1, 2, 0, 0, 0, 1, 1, 1, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(2, False)]: print('computer_move test 162 failed - with blocking move for p2'); block_count += 1

board = [1, 2, 2, 1, 2, 0, 2, 1, 1, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(2, False), (3, True)]: print('computer_move test 163 failed - with blocking move for p1'); block_count += 1

board = [1, 2, 2, 1, 2, 0, 2, 1, 1, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False)]: print('computer_move test 163 failed - with winning move for p2'); win_count += 1

board = [1, 1, 1, 2, 2, 2, 1, 0, 1, 2, 1, 2, 1, 2, 0, 0, 2, 1, 2, 2, 1, 0, 0, 1, 2, 0, 2, 1, 0, 0, 2, 2, 0, 2, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, True), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 164 failed - with valid move for p1'); valid_count += 1

board = [1, 1, 1, 2, 2, 2, 1, 0, 1, 2, 1, 2, 1, 2, 0, 0, 2, 1, 2, 2, 1, 0, 0, 1, 2, 0, 2, 1, 0, 0, 2, 2, 0, 2, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, False), (5, True)]: print('computer_move test 164 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 0, 1, 2, 1, 2, 1, 1, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(1, False), (2, False), (4, False), (5, False), (6, False)]: print('computer_move test 165 failed - with blocking move for p1'); block_count += 1

board = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 0, 1, 2, 1, 2, 1, 1, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, True), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 165 failed - with blocking move for p2'); block_count += 1

board = [2, 1, 1, 2, 2, 2, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, True), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 166 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 1, 2, 2, 2, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, True)]: print('computer_move test 166 failed - with winning move for p2'); win_count += 1

board = [0, 2, 2, 2, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 167 failed - with valid move for p1'); valid_count += 1

board = [0, 2, 2, 2, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, False), (4, False)]: print('computer_move test 167 failed - with winning move for p2'); win_count += 1

board = [1, 0, 2, 1, 2, 1, 2, 0, 0, 2, 1, 2, 2, 2, 0, 0, 2, 2, 1, 1, 2, 0, 0, 1, 1, 1, 2, 1, 0, 0, 2, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(5, True)]: print('computer_move test 168 failed - with winning move for p1'); win_count += 1

board = [1, 0, 2, 1, 2, 1, 2, 0, 0, 2, 1, 2, 2, 2, 0, 0, 2, 2, 1, 1, 2, 0, 0, 1, 1, 1, 2, 1, 0, 0, 2, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(2, True)]: print('computer_move test 168 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 2, 0, 2, 2, 2, 1, 1, 2, 0, 2, 0, 2, 2, 1, 2, 0, 1, 0, 1, 1, 2, 0, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 169 failed - with valid move for p1'); valid_count += 1

board = [1, 1, 2, 0, 2, 2, 2, 1, 1, 2, 0, 2, 0, 2, 2, 1, 2, 0, 1, 0, 1, 1, 2, 0, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (3, False)]: print('computer_move test 169 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, True), (1, False), (2, True), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 170 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, True), (0, False)]: print('computer_move test 170 failed - with winning move for p2'); win_count += 1

board = [2, 2, 2, 1, 1, 0, 2, 1, 2, 0, 2, 1, 0, 1, 1, 0, 0, 2, 2, 0, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(3, False)]: print('computer_move test 171 failed - with blocking move for p1'); block_count += 1

board = [2, 2, 2, 1, 1, 0, 2, 1, 2, 0, 2, 1, 0, 1, 1, 0, 0, 2, 2, 0, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 171 failed - with winning move for p2'); win_count += 1

board = [1, 0, 2, 2, 2, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(1, False)]: print('computer_move test 172 failed - with blocking move for p1'); block_count += 1

board = [1, 0, 2, 2, 2, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False)]: print('computer_move test 172 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, False), (4, False)]: print('computer_move test 173 failed - with winning move for p1'); win_count += 1

board = [2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 173 failed - with valid move for p2'); valid_count += 1

board = [1, 0, 2, 2, 1, 1, 2, 2, 0, 2, 2, 1, 2, 1, 2, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 174 failed - with valid move for p1'); valid_count += 1

board = [1, 0, 2, 2, 1, 1, 2, 2, 0, 2, 2, 1, 2, 1, 2, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 174 failed - with winning move for p2'); win_count += 1

board = [2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 0, 2, 2, 2, 1, 1, 2, 0, 2, 1, 2, 1, 2, 2, 0, 1, 2, 1, 0, 1, 1, 0, 1, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(1, True), (2, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 175 failed - with valid move for p1'); valid_count += 1

board = [2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 0, 2, 2, 2, 1, 1, 2, 0, 2, 1, 2, 1, 2, 2, 0, 1, 2, 1, 0, 1, 1, 0, 1, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(0, True), (2, False)]: print('computer_move test 175 failed - with winning move for p2'); win_count += 1

board = [1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 0, 1, 2, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, True), (5, False)]: print('computer_move test 176 failed - with winning move for p1'); win_count += 1

board = [1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 0, 1, 2, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(6, False)]: print('computer_move test 176 failed - with winning move for p2'); win_count += 1

board = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False), (4, False)]: print('computer_move test 177 failed - with winning move for p1'); win_count += 1

board = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 177 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 0, 1, 2, 1, 1, 2, 2, 0, 1, 2, 2, 2, 1, 1, 0, 2, 1, 1, 1, 2, 1, 0, 2, 0, 0, 2, 1, 2, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(0, False), (1, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 178 failed - with blocking move for p1'); block_count += 1

board = [1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 0, 1, 2, 1, 1, 2, 2, 0, 1, 2, 2, 2, 1, 1, 0, 2, 1, 1, 1, 2, 1, 0, 2, 0, 0, 2, 1, 2, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, False), (1, True), (3, True), (5, False), (6, False)]: print('computer_move test 178 failed - with blocking move for p2'); block_count += 1

board = [2, 1, 2, 1, 1, 2, 1, 2, 0, 2, 1, 1, 1, 2, 2, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(6, True)]: print('computer_move test 179 failed - with winning move for p1'); win_count += 1

board = [2, 1, 2, 1, 1, 2, 1, 2, 0, 2, 1, 1, 1, 2, 2, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 179 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 0, 2, 0, 1, 1, 2, 1, 0, 1, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(4, False)]: print('computer_move test 180 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 0, 2, 0, 1, 1, 2, 1, 0, 1, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(2, True), (3, True), (4, False)]: print('computer_move test 180 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 2, 1, 2, 1, 1, 2, 0, 2, 1, 2, 1, 1, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(6, True)]: print('computer_move test 181 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 2, 1, 1, 2, 0, 2, 1, 2, 1, 1, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(3, False)]: print('computer_move test 181 failed - with winning move for p2'); win_count += 1

board = [2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 0, 1, 0, 1, 2, 2, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, True), (2, False), (3, False), (4, True), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 182 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 0, 1, 0, 1, 2, 2, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, True), (1, False)]: print('computer_move test 182 failed - with winning move for p2'); win_count += 1

board = [1, 1, 2, 1, 0, 1, 2, 1, 1, 1, 2, 0, 2, 1, 2, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, False)]: print('computer_move test 183 failed - with winning move for p1'); win_count += 1

board = [1, 1, 2, 1, 0, 1, 2, 1, 1, 1, 2, 0, 2, 1, 2, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(1, False)]: print('computer_move test 183 failed - with blocking move for p2'); block_count += 1

board = [1, 2, 2, 1, 2, 1, 2, 0, 1, 1, 2, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 2, 2, 2, 0, 2, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(3, True)]: print('computer_move test 184 failed - with blocking move for p1'); block_count += 1

board = [1, 2, 2, 1, 2, 1, 2, 0, 1, 1, 2, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 2, 2, 2, 0, 2, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, True)]: print('computer_move test 184 failed - with winning move for p2'); win_count += 1

board = [2, 2, 0, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, False)]: print('computer_move test 185 failed - with winning move for p1'); win_count += 1

board = [2, 2, 0, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, False), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 185 failed - with valid move for p2'); valid_count += 1

board = [1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 0, 1, 0, 1, 1, 1, 1, 0, 2, 0, 0, 2, 2, 2, 0, 2, 0, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 2, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 186 failed - with winning move for p1'); win_count += 1

board = [1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 0, 1, 0, 1, 1, 1, 1, 0, 2, 0, 0, 2, 2, 2, 0, 2, 0, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 2, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(1, True), (1, False), (2, True), (3, True), (3, False), (4, False), (6, True), (6, False)]: print('computer_move test 186 failed - with valid move for p2'); valid_count += 1

board = [2, 0, 2, 2, 1, 2, 2, 2, 0, 1, 2, 1, 1, 1, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 187 failed - with valid move for p1'); valid_count += 1

board = [2, 0, 2, 2, 1, 2, 2, 2, 0, 1, 2, 1, 1, 1, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(1, False), (5, False)]: print('computer_move test 187 failed - with winning move for p2'); win_count += 1

board = [1, 1, 1, 2, 1, 1, 0, 2, 1, 1, 1, 2, 1, 0, 2, 1, 1, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, True)]: print('computer_move test 188 failed - with winning move for p1'); win_count += 1

board = [1, 1, 1, 2, 1, 1, 0, 2, 1, 1, 1, 2, 1, 0, 2, 1, 1, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 188 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 1, 2, 1, 0, 1, 2, 2, 2, 1, 2, 0, 1, 2, 1, 0, 2, 2, 0, 2, 2, 2, 0, 1, 1, 0, 1, 1, 1, 0, 2, 2, 0, 1, 2, 2, 0, 2, 2, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, True), (2, False), (3, False), (4, True), (5, False), (6, True), (6, False)]: print('computer_move test 189 failed - with blocking move for p1'); block_count += 1

board = [1, 1, 1, 2, 1, 0, 1, 2, 2, 2, 1, 2, 0, 1, 2, 1, 0, 2, 2, 0, 2, 2, 2, 0, 1, 1, 0, 1, 1, 1, 0, 2, 2, 0, 1, 2, 2, 0, 2, 2, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (5, False), (6, False)]: print('computer_move test 189 failed - with blocking move for p2'); block_count += 1

board = [1, 1, 1, 2, 1, 1, 2, 0, 2, 1, 1, 2, 2, 1, 0, 1, 2, 0, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False), (4, True)]: print('computer_move test 190 failed - with winning move for p1'); win_count += 1

board = [1, 1, 1, 2, 1, 1, 2, 0, 2, 1, 1, 2, 2, 1, 0, 1, 2, 0, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, False), (6, True), (6, False)]: print('computer_move test 190 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2, 1, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# blocking move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (6, False)]: print('computer_move test 191 failed - with blocking move for p1'); block_count += 1

board = [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2, 1, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, False), (5, True), (5, False), (6, True), (6, False)]: print('computer_move test 191 failed - with blocking move for p2'); block_count += 1

board = [2, 2, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False), (6, False)]: print('computer_move test 192 failed - with winning move for p1'); win_count += 1

board = [2, 2, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, True), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 192 failed - with valid move for p2'); valid_count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 0, 1, 2, 2, 2, 0, 2, 0, 1, 1, 0, 2, 0, 1, 0, 2, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(3, False)]: print('computer_move test 193 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 0, 1, 2, 2, 2, 0, 2, 0, 1, 1, 0, 2, 0, 1, 0, 2, 0, 0]
move = computer_move(board, 2, 2)# blocking move exists for p2
if move not in [(0, True)]: print('computer_move test 193 failed - with blocking move for p2'); block_count += 1

board = [2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 0, 2, 1, 1, 0, 1, 0, 0, 2, 2, 1, 0, 1, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 2]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(0, False), (1, False)]: print('computer_move test 194 failed - with winning move for p1'); win_count += 1

board = [2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 0, 2, 1, 1, 0, 1, 0, 0, 2, 2, 1, 0, 1, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 2]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, True), (1, False), (2, True), (3, False), (4, True), (4, False), (5, False), (6, True)]: print('computer_move test 194 failed - with valid move for p2'); valid_count += 1

board = [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 195 failed - with valid move for p1'); valid_count += 1

board = [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (6, False)]: print('computer_move test 195 failed - with winning move for p2'); win_count += 1

board = [2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(1, True)]: print('computer_move test 196 failed - with winning move for p1'); win_count += 1

board = [2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, True), (0, False), (1, False), (2, False), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 196 failed - with valid move for p2'); valid_count += 1

board = [1, 1, 1, 2, 2, 1, 2, 1, 2, 0, 2, 1, 2, 2, 2, 1, 0, 0, 2, 1, 1, 2, 2, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, True), (1, False), (2, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 197 failed - with valid move for p1'); valid_count += 1

board = [1, 1, 1, 2, 2, 1, 2, 1, 2, 0, 2, 1, 2, 2, 2, 1, 0, 0, 2, 1, 1, 2, 2, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(4, True)]: print('computer_move test 197 failed - with winning move for p2'); win_count += 1

board = [1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 0, 2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# winning move exists for p1
if move not in [(2, True)]: print('computer_move test 198 failed - with winning move for p1'); win_count += 1

board = [1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 0, 2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# valid move exists for p2
if move not in [(0, False), (1, False), (2, False), (3, True), (3, False), (4, True), (4, False), (5, False), (6, False)]: print('computer_move test 198 failed - with valid move for p2'); valid_count += 1

board = [1, 0, 1, 2, 2, 1, 2, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, True), (0, False), (1, False), (2, True), (2, False), (3, False), (4, False), (5, True), (5, False), (6, False)]: print('computer_move test 199 failed - with valid move for p1'); valid_count += 1

board = [1, 0, 1, 2, 2, 1, 2, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (6, False)]: print('computer_move test 199 failed - with winning move for p2'); win_count += 1

board = [2, 2, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 1, 2)# valid move exists for p1
if move not in [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False)]: print('computer_move test 200 failed - with valid move for p1'); valid_count += 1

board = [2, 2, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move = computer_move(board, 2, 2)# winning move exists for p2
if move not in [(2, False), (4, False)]: print('computer_move test 200 failed - with winning move for p2'); win_count += 1

print(f"winning moves: {217 - win_count} out of 217 passed.")
print(f"blocking moves: {60 - block_count} out of 60 passed.")
print(f"valid moves: {123 - valid_count} out of 123 passed.")
