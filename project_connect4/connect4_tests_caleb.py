from connect4 import *
count = 0
board = [2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 0, 0, 1, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0]
# board with 9 rows
if not check_move(board, 1, 5, False) == True: print('check_move test 1 failed'); count += 1

board = [2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 0, 1, 2, 1, 1, 1, 2, 0, 1, 1, 2, 0, 1, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 2, 4, True) == False: print('check_move test 2 failed'); count += 1

board = [1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 0, 1, 2, 2, 1, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 1, 0, True) == True: print('check_move test 3 failed'); count += 1

board = [2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# board with 11 rows
if not check_move(board, 2, 2, False) == True: print('check_move test 4 failed'); count += 1

board = [2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 2, 1, True) == False: print('check_move test 5 failed'); count += 1

board = [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0]
# board with 8 rows
if not check_move(board, 1, 6, False) == True: print('check_move test 6 failed'); count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 0, 2, 1, 2, 1, 1, 2, 0, 2, 1, 1, 2, 1, 2, 0, 0, 0, 1, 0, 1, 2]
# board with 6 rows
if not check_move(board, 1, 2, True) == True: print('check_move test 7 failed'); count += 1

board = [2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 0, 2, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 1, 0, True) == False: print('check_move test 8 failed'); count += 1

board = [2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 0, 2, 1, 2, 2, 1, 2, 0, 1, 1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 2, 6, False) == True: print('check_move test 9 failed'); count += 1

board = [2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
# board with 6 rows
if not check_move(board, 2, 1, False) == True: print('check_move test 10 failed'); count += 1

board = [1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0]
# board with 10 rows
if not check_move(board, 2, 5, False) == True: print('check_move test 11 failed'); count += 1

board = [1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 0, 2, 2, 1, 2, 2, 2, 0, 1, 2, 0, 0, 1, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 2, 5, True) == False: print('check_move test 12 failed'); count += 1

board = [2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 1, 2, True) == True: print('check_move test 13 failed'); count += 1

board = [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 1, 2, False) == True: print('check_move test 14 failed'); count += 1

board = [2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 0, 1, 2, 1, 1, 2, 2, 0, 1, 2, 2, 2, 2, 2, 0, 0, 1, 0, 1, 1, 2, 0, 0, 1, 0, 1, 1, 0, 0, 0, 2, 0, 1]
# board with 11 rows
if not check_move(board, 1, 3, True) == False: print('check_move test 15 failed'); count += 1

board = [2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 0, 2, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0]
# board with 7 rows
if not check_move(board, 2, 3, True) == True: print('check_move test 16 failed'); count += 1

board = [2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 0, 0, 1, 2, 2, 1, 2, 0, 0, 2, 2, 0, 1, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 13 rows
if not check_move(board, 1, 2, True) == True: print('check_move test 17 failed'); count += 1

board = [1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2]
# board with 6 rows
if not check_move(board, 1, 0, False) == True: print('check_move test 18 failed'); count += 1

board = [1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 0, 2, 2, 2, 1, 1, 2, 0, 2, 1, 2, 1, 1, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1]
# board with 13 rows
if not check_move(board, 2, 3, False) == True: print('check_move test 19 failed'); count += 1

board = [2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 0, 2, 1, 1, 2, 1, 1, 0, 2, 0, 0, 2, 1, 1, 0, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 1, 5, False) == True: print('check_move test 20 failed'); count += 1

board = [2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 0, 2, 0, 1, 2, 1, 1, 0, 2, 0, 0, 0, 1, 0]
# board with 6 rows
if not check_move(board, 2, 6, False) == True: print('check_move test 21 failed'); count += 1

board = [1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 0, 2, 1, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
# board with 6 rows
if not check_move(board, 1, 3, False) == True: print('check_move test 22 failed'); count += 1

board = [2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 0, 2, 2, 2, 2, 1, 0, 0, 2, 2, 1, 1, 2, 0, 0, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0]
# board with 7 rows
if not check_move(board, 2, 4, True) == False: print('check_move test 23 failed'); count += 1

board = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 0, 2, 2, 1, 1, 2, 1, 0, 0, 1, 1, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 2, 5, False) == True: print('check_move test 24 failed'); count += 1

board = [1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 0, 2, 1, 2, 2, 1, 2, 0, 2, 2, 2, 0, 2, 1, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 1, 0, 1, 0]
# board with 11 rows
if not check_move(board, 2, 3, False) == False: print('check_move test 25 failed'); count += 1

board = [1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 0, 2, 1, 1, 0, 2, 1, 0, 0, 2, 0, 0, 1, 0, 0]
# board with 6 rows
if not check_move(board, 2, 0, False) == True: print('check_move test 26 failed'); count += 1

board = [1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 1, 2, 1, 2, 2, 2, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0]
# board with 11 rows
if not check_move(board, 2, 6, True) == False: print('check_move test 27 failed'); count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 0, 1, 2, 0, 2, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0]
# board with 12 rows
if not check_move(board, 1, 6, True) == False: print('check_move test 28 failed'); count += 1

board = [2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0]
# board with 6 rows
if not check_move(board, 1, 6, True) == True: print('check_move test 29 failed'); count += 1

board = [1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 0, 1, 1, 2, 1, 2, 0, 0, 2, 2, 1, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0]
# board with 8 rows
if not check_move(board, 2, 5, False) == False: print('check_move test 30 failed'); count += 1

board = [2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 1, 3, False) == True: print('check_move test 31 failed'); count += 1

board = [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 0, 1, 0, 2, 2, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 13 rows
if not check_move(board, 2, 5, False) == True: print('check_move test 32 failed'); count += 1

board = [2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 0, 2, 1, 1, 1, 0, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 1, 2, 0]
# board with 7 rows
if not check_move(board, 1, 5, False) == False: print('check_move test 33 failed'); count += 1

board = [2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 1, 4, False) == True: print('check_move test 34 failed'); count += 1

board = [2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 0, 2, 0, 1, 2, 1, 0, 0, 2, 0, 1, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
# board with 13 rows
if not check_move(board, 2, 6, False) == True: print('check_move test 35 failed'); count += 1

board = [1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 0, 2, 2, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 2, 0, 2, 1, 2, 0, 0, 2, 0, 0, 0, 0, 0]
# board with 7 rows
if not check_move(board, 2, 4, True) == True: print('check_move test 36 failed'); count += 1

board = [2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 0, 2, 1, 1, 1, 2, 1, 0, 2, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 2]
# board with 9 rows
if not check_move(board, 2, 2, False) == False: print('check_move test 37 failed'); count += 1

board = [1, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 0, 0, 2, 2, 1, 1, 2, 0, 0, 2, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 13 rows
if not check_move(board, 1, 6, False) == True: print('check_move test 38 failed'); count += 1

board = [1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 2, 1, False) == True: print('check_move test 39 failed'); count += 1

board = [1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0]
# board with 6 rows
if not check_move(board, 2, 2, True) == False: print('check_move test 40 failed'); count += 1

board = [1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 0, 2, 2, 1, 2, 2, 1, 0, 1, 0, 0, 2, 1, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 2, 5, False) == True: print('check_move test 41 failed'); count += 1

board = [2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0]
# board with 7 rows
if not check_move(board, 1, 2, False) == True: print('check_move test 42 failed'); count += 1

board = [1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0]
# board with 6 rows
if not check_move(board, 2, 3, False) == True: print('check_move test 43 failed'); count += 1

board = [1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 0, 1, 2, 1, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 0, 2, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0]
# board with 12 rows
if not check_move(board, 2, 0, True) == False: print('check_move test 44 failed'); count += 1

board = [1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2]
# board with 7 rows
if not check_move(board, 1, 4, False) == True: print('check_move test 45 failed'); count += 1

board = [1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 0, 1, 1, 2, 1, 1, 2, 0, 2, 2, 1, 1, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 1, 2, 0, 0]
# board with 6 rows
if not check_move(board, 1, 2, True) == True: print('check_move test 46 failed'); count += 1

board = [1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 0, 1, 1, 1, 2, 1, 0, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0]
# board with 12 rows
if not check_move(board, 2, 3, True) == False: print('check_move test 47 failed'); count += 1

board = [2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1]
# board with 7 rows
if not check_move(board, 1, 4, False) == True: print('check_move test 48 failed'); count += 1

board = [2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 2, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
# board with 11 rows
if not check_move(board, 1, 0, False) == True: print('check_move test 49 failed'); count += 1

board = [2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 7 rows
if not check_move(board, 1, 3, True) == False: print('check_move test 50 failed'); count += 1

board = [2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 0, 2, 1, 2, 0, 2, 1, 0, 2, 1, 2, 0, 2, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 13 rows
if not check_move(board, 1, 3, False) == True: print('check_move test 51 failed'); count += 1

board = [1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 0, 1, 0, 1, 1, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 11 rows
if not check_move(board, 2, 5, False) == True: print('check_move test 52 failed'); count += 1

board = [2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 0, 2, 1, 1, 1, 2, 2, 0, 1, 0, 2, 1, 2, 2, 0, 2, 0, 1, 1, 1, 2, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 13 rows
if not check_move(board, 2, 3, True) == False: print('check_move test 53 failed'); count += 1

board = [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2, 2, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1]
# board with 9 rows
if not check_move(board, 1, 6, True) == True: print('check_move test 54 failed'); count += 1

board = [1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2, 2, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 2, 2, 1]
# board with 7 rows
if not check_move(board, 2, 1, True) == False: print('check_move test 55 failed'); count += 1

board = [1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 13 rows
if not check_move(board, 2, 0, True) == False: print('check_move test 56 failed'); count += 1

board = [2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 0, 1, 0, 0, 2, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0]
# board with 12 rows
if not check_move(board, 1, 5, False) == True: print('check_move test 57 failed'); count += 1

board = [1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 0, 1, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0]
# board with 7 rows
if not check_move(board, 2, 5, False) == True: print('check_move test 58 failed'); count += 1

board = [2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 0, 2, 1, 2, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 1, 3, False) == True: print('check_move test 59 failed'); count += 1

board = [1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 1, 1, 0, 1, 2, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 1, 2, False) == True: print('check_move test 60 failed'); count += 1

board = [2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 0, 1, 2, 2, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 12 rows
if not check_move(board, 2, 3, True) == True: print('check_move test 61 failed'); count += 1

board = [1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 0, 1, 0, 1, 1, 1, 2, 0, 0, 0, 2, 1, 2, 1, 0, 0, 0, 1, 2, 0, 0]
# board with 8 rows
if not check_move(board, 1, 1, False) == True: print('check_move test 62 failed'); count += 1

board = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 0, 2, 1, 1, 2, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 2, 0, True) == False: print('check_move test 63 failed'); count += 1

board = [1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 0, 2, 0, 0, 1, 2, 1, 0, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 1, 4, False) == True: print('check_move test 64 failed'); count += 1

board = [2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 0, 2, 2, 2, 1, 2, 1, 0, 1, 2, 2, 2, 1, 2, 0, 0, 1, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0]
# board with 11 rows
if not check_move(board, 1, 0, False) == False: print('check_move test 65 failed'); count += 1

board = [1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0, 1, 1, 2, 1, 1, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 2, 2, True) == False: print('check_move test 66 failed'); count += 1

board = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
# board with 8 rows
if not check_move(board, 1, 5, True) == True: print('check_move test 67 failed'); count += 1

board = [2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 2]
# board with 8 rows
if not check_move(board, 2, 2, False) == False: print('check_move test 68 failed'); count += 1

board = [2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0]
# board with 9 rows
if not check_move(board, 2, 3, True) == True: print('check_move test 69 failed'); count += 1

board = [1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 0, 2, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 2, 6, False) == True: print('check_move test 70 failed'); count += 1

board = [2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 2, 2, False) == True: print('check_move test 71 failed'); count += 1

board = [2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0]
# board with 7 rows
if not check_move(board, 2, 3, False) == True: print('check_move test 72 failed'); count += 1

board = [2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 0, 2, 2, 2, 1, 2, 1, 0, 2, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 1, 5, True) == True: print('check_move test 73 failed'); count += 1

board = [2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 0, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1, 1, 2, 0, 2, 1, 1, 0, 1, 0, 0, 1, 2, 2, 0, 2, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 2, 2, True) == True: print('check_move test 74 failed'); count += 1

board = [1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0]
# board with 6 rows
if not check_move(board, 1, 0, False) == True: print('check_move test 75 failed'); count += 1

board = [1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 0, 2, 1, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 2, 4, True) == True: print('check_move test 76 failed'); count += 1

board = [1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
# board with 7 rows
if not check_move(board, 1, 1, False) == True: print('check_move test 77 failed'); count += 1

board = [1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 0, 2, 2, 1, 2, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 2, 4, True) == True: print('check_move test 78 failed'); count += 1

board = [2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 0, 2, 1, 1, 1, 2, 1, 0, 1, 1, 2, 2, 2, 2, 0, 2, 2, 1, 2, 1, 0, 0, 0, 0, 2, 0]
# board with 8 rows
if not check_move(board, 1, 6, False) == True: print('check_move test 79 failed'); count += 1

board = [2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 0, 1, 1, 1, 1, 2, 2, 0, 2, 0, 2, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 1, 4, False) == True: print('check_move test 80 failed'); count += 1

board = [1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 0, 2, 2, 1, 1, 2, 2, 0, 1, 1, 1, 2, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0]
# board with 8 rows
if not check_move(board, 2, 5, True) == True: print('check_move test 81 failed'); count += 1

board = [1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 0, 2, 2, 1, 0, 1, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# board with 8 rows
if not check_move(board, 1, 3, True) == False: print('check_move test 82 failed'); count += 1

board = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 0, 1, 2, 1, 1, 2, 2, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 2, 2, True) == False: print('check_move test 83 failed'); count += 1

board = [1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 1, 2, False) == True: print('check_move test 84 failed'); count += 1

board = [2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 2, 1, 2, 1, 0, 0, 0, 2, 0, 2, 0]
# board with 9 rows
if not check_move(board, 2, 2, False) == True: print('check_move test 85 failed'); count += 1

board = [2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 0, 2, 1, 2, 2, 1, 1, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 2, 0, True) == True: print('check_move test 86 failed'); count += 1

board = [2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 2, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# board with 10 rows
if not check_move(board, 1, 5, True) == True: print('check_move test 87 failed'); count += 1

board = [1, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 0, 1, 1, 0, 2, 2, 1, 0, 0, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0]
# board with 6 rows
if not check_move(board, 2, 1, True) == False: print('check_move test 88 failed'); count += 1

board = [2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
# board with 12 rows
if not check_move(board, 1, 6, False) == True: print('check_move test 89 failed'); count += 1

board = [1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 2, 1, 2, 2, 0, 1, 1, 1, 2, 2, 1, 0, 1, 2, 2, 2, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0]
# board with 8 rows
if not check_move(board, 1, 3, False) == True: print('check_move test 90 failed'); count += 1

board = [1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 0, 2, 1, 1, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# board with 10 rows
if not check_move(board, 1, 0, False) == True: print('check_move test 91 failed'); count += 1

board = [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 0, 1, 2, 1, 2, 1, 1, 0, 0, 1, 1, 1, 2, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 2, 1, 0, 0]
# board with 9 rows
if not check_move(board, 2, 5, True) == False: print('check_move test 92 failed'); count += 1

board = [2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 0, 2, 2, 1, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0]
# board with 13 rows
if not check_move(board, 2, 4, False) == False: print('check_move test 93 failed'); count += 1

board = [1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0]
# board with 9 rows
if not check_move(board, 1, 6, False) == True: print('check_move test 94 failed'); count += 1

board = [2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 0, 0, 2, 2, 1, 1, 2, 0, 0, 1, 0, 1, 2, 1, 0, 0, 2, 0, 1, 2, 2, 0, 0, 0, 0, 1, 1, 0]
# board with 8 rows
if not check_move(board, 2, 1, False) == True: print('check_move test 95 failed'); count += 1

board = [2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 0, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 2]
# board with 6 rows
if not check_move(board, 1, 2, True) == False: print('check_move test 96 failed'); count += 1

board = [1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1]
# board with 8 rows
if not check_move(board, 2, 3, True) == True: print('check_move test 97 failed'); count += 1

board = [2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 0, 2, 1, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 1, 0, 2, 2, 0, 0, 1, 2, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0]
# board with 11 rows
if not check_move(board, 2, 1, True) == True: print('check_move test 98 failed'); count += 1

board = [1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0]
# board with 6 rows
if not check_move(board, 2, 5, False) == True: print('check_move test 99 failed'); count += 1

board = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 0, 0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0]
# board with 8 rows
if not check_move(board, 2, 4, False) == False: print('check_move test 100 failed'); count += 1

print(f"check_move: {100 - count} out of 100 passed.")
count = 0
board = [2, 2, 2, 1, 2, 2, 2, 2, 1, 0, 2, 2, 1, 1, 1, 1, 0, 2, 2, 1, 1, 0, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 1, 2, 2, 1, 2, 1, 0, 2, 2, 1, 1, 1, 1, 0, 2, 2, 1, 2, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 6, True)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 1 failed'); count += 1

board = [2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 0, 1, 2, 1, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 0, 1, 2, 1, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 2 failed'); count += 1

board = [1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 0, 1, 1, 2, 2, 1, 0, 0, 2, 1, 0, 2, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 0, 0, 2, 1, 0, 2, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 3 failed'); count += 1

board = [2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 0, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 4 failed'); count += 1

board = [1, 2, 2, 1, 0, 2, 2, 1, 2, 1, 2, 0, 1, 2, 0, 1, 2, 1, 0, 1, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 1, 0, 2, 2, 0, 2, 1, 2, 0, 1, 2, 0, 1, 2, 1, 0, 1, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, True)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 5 failed'); count += 1

board = [1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 0, 2, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 0, 2, 1, 2, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 3, False)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 6 failed'); count += 1

board = [1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 0, 1, 2, 2, 2, 1, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 0, 1, 2, 2, 2, 1, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 3, False)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 7 failed'); count += 1

board = [2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 0, 2, 0, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, True)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 8 failed'); count += 1

board = [1, 1, 0, 1, 2, 2, 1, 1, 0, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 0, 1, 2, 2, 1, 1, 1, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 9 failed'); count += 1

board = [2, 1, 1, 1, 2, 2, 1, 0, 2, 0, 2, 0, 1, 2, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 1, 2, 2, 1, 0, 2, 0, 2, 0, 1, 2, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 3, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 10 failed'); count += 1

board = [2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 2, 2, 2, 0, 0, 1, 0, 1, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 2, 2, 2, 0, 0, 1, 0, 1, 1, 2, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 5, False)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 11 failed'); count += 1

board = [1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 2, 1, 1, 2, 1, 2, 0, 2, 2, 2, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, True)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 12 failed'); count += 1

board = [2, 2, 2, 2, 2, 2, 1, 1, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 2, 2, 1, 1, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 0, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 13 failed'); count += 1

board = [1, 2, 2, 2, 2, 1, 1, 1, 2, 0, 1, 2, 1, 2, 1, 2, 0, 1, 1, 1, 0, 1, 1, 0, 2, 0, 0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 2, 2, 1, 1, 1, 2, 0, 1, 2, 1, 2, 1, 2, 0, 1, 1, 1, 0, 2, 1, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, True)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 14 failed'); count += 1

board = [2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 0, 1, 0, 2, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 2, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 15 failed'); count += 1

board = [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 0, 2, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 0, 2, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 5, False)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 16 failed'); count += 1

board = [2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 0, 1, 2, 1, 2, 2, 1, 0, 1, 2, 1, 1, 2, 0, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 0, 1, 2, 1, 2, 2, 0, 0, 1, 2, 1, 1, 2, 0, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, True)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 17 failed'); count += 1

board = [2, 1, 2, 2, 1, 2, 1, 1, 0, 1, 2, 2, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 2, 1, 2, 1, 1, 0, 1, 2, 2, 0, 2, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 0, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 18 failed'); count += 1

board = [1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 1, 2, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 5, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 19 failed'); count += 1

board = [1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 0, 2, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 0, 2, 1, 2, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 20 failed'); count += 1

board = [1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 2, 0, 1, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
board_expected = [1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 2, 0, 1, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0]
board_result = apply_move(board, 1, 0, False)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 21 failed'); count += 1

board = [1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 0, 2, 2, 2, 0, 1, 2, 0, 2, 1, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 0, 2, 2, 2, 0, 1, 2, 0, 2, 1, 2, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 6, False)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 22 failed'); count += 1

board = [2, 1, 2, 2, 2, 0, 2, 1, 2, 2, 2, 2, 0, 2, 1, 0, 0, 1, 2, 0, 2, 2, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 2, 2, 0, 2, 1, 2, 2, 2, 2, 0, 2, 1, 0, 0, 1, 2, 0, 2, 2, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 23 failed'); count += 1

board = [2, 1, 2, 1, 2, 1, 2, 0, 0, 2, 2, 2, 1, 2, 0, 0, 1, 2, 2, 1, 2, 0, 0, 2, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 1, 2, 1, 2, 0, 0, 2, 2, 2, 1, 2, 0, 0, 1, 2, 2, 1, 2, 0, 0, 2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 5, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 24 failed'); count += 1

board = [2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 0, 0, 2, 1, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 0, 2, 0, 0, 2, 1, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 0, True)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 25 failed'); count += 1

board = [1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 26 failed'); count += 1

board = [2, 1, 2, 2, 2, 2, 1, 0, 2, 2, 1, 2, 0, 2, 0, 2, 2, 2, 1, 0, 2, 0, 1, 2, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 2, 2, 2, 1, 0, 2, 2, 1, 2, 0, 2, 0, 2, 2, 2, 1, 0, 2, 0, 1, 2, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 27 failed'); count += 1

board = [1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 0, 2, 2, 0, 2, 2, 2, 0, 1, 2, 0, 1, 1, 2, 0, 2, 1, 0, 2, 2, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 2, 1, 2, 2, 1, 2, 0, 1, 2, 1, 0, 2, 2, 0, 2, 2, 2, 0, 1, 2, 0, 1, 1, 2, 0, 2, 1, 0, 2, 2, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, True)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 28 failed'); count += 1

board = [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 1, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 29 failed'); count += 1

board = [1, 1, 1, 2, 2, 1, 2, 2, 1, 0, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 2, 2, 1, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 2, 1, 2, 2, 1, 0, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 2, 2, 1, 0, 1, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 30 failed'); count += 1

board = [2, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 31 failed'); count += 1

board = [1, 1, 1, 2, 2, 1, 2, 0, 1, 2, 1, 2, 1, 2, 0, 1, 1, 1, 2, 1, 1, 0, 2, 1, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 2, 1, 2, 0, 1, 2, 1, 2, 1, 2, 0, 1, 1, 1, 2, 1, 1, 0, 2, 1, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 4, False)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 32 failed'); count += 1

board = [2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 0, 1, 2, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 0, 1, 2, 1, 0, 1, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 33 failed'); count += 1

board = [2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 0, 1, 0, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 0, 1, 2, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 4, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 34 failed'); count += 1

board = [2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 0, 2, 2, 1, 2, 1, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 3, True)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 35 failed'); count += 1

board = [2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 4, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 36 failed'); count += 1

board = [1, 2, 2, 1, 2, 2, 1, 2, 0, 2, 1, 2, 1, 2, 2, 0, 2, 1, 1, 2, 2, 2, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 1, 2, 2, 1, 2, 0, 2, 1, 2, 1, 2, 2, 0, 2, 1, 1, 2, 2, 2, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 3, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 37 failed'); count += 1

board = [2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 2, 2, 0, 1, 0, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 2, 2, 0, 1, 1, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 38 failed'); count += 1

board = [1, 1, 1, 2, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 4, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 39 failed'); count += 1

board = [1, 1, 1, 0, 2, 2, 2, 2, 1, 1, 0, 1, 2, 2, 2, 2, 2, 0, 2, 1, 1, 2, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 0, 2, 2, 2, 2, 1, 1, 0, 1, 2, 2, 2, 2, 2, 0, 2, 1, 1, 2, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 2, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 4, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 40 failed'); count += 1

board = [2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 1, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 0, 1, 2, 1, 2, 2, 1, 0, 1, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 1, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 0, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 41 failed'); count += 1

board = [1, 1, 2, 1, 1, 1, 2, 2, 0, 2, 0, 1, 2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 2, 1, 1, 1, 2, 2, 0, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 4, True)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 42 failed'); count += 1

board = [2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 0, 1, 2, 2, 2, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 0, 1, 2, 2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 43 failed'); count += 1

board = [1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 1, 2, 2, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 44 failed'); count += 1

board = [2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 1, 1, 2, 2, 2, 2, 0, 1, 1, 1, 2, 1, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, True)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 45 failed'); count += 1

board = [1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 2, 2, 0, 0, 1, 1, 2, 1, 1, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 2, 2, 0, 0, 1, 1, 2, 1, 1, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 4, True)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 46 failed'); count += 1

board = [1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, True)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 47 failed'); count += 1

board = [1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 2, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 5, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 48 failed'); count += 1

board = [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 4, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 49 failed'); count += 1

board = [1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, False)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 50 failed'); count += 1

board = [2, 1, 1, 2, 1, 2, 2, 1, 0, 2, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 2, 1, 2, 2, 1, 0, 2, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 51 failed'); count += 1

board = [2, 0, 1, 2, 1, 2, 2, 2, 0, 2, 2, 1, 2, 1, 1, 0, 2, 2, 2, 2, 1, 1, 0, 2, 2, 2, 2, 1, 2, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 0, 2, 2, 1, 2, 2, 2, 0, 2, 2, 1, 2, 1, 1, 0, 2, 2, 2, 2, 1, 1, 0, 1, 2, 2, 2, 1, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, True)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 52 failed'); count += 1

board = [1, 2, 2, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 2, 0, 2, 1, 0, 0, 1, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 6, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 53 failed'); count += 1

board = [2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 0, 2, 1, 1, 2, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 0, 2, 1, 1, 2, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 5, False)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 54 failed'); count += 1

board = [2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 0, 2, 2, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 55 failed'); count += 1

board = [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 0, 2, 0, 2, 2, 2, 1, 0, 1, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 0, 2, 0, 2, 2, 2, 1, 0, 1, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, False)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 56 failed'); count += 1

board = [1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 0, 0, 1, 2, 1, 1, 1, 0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, True)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 57 failed'); count += 1

board = [1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 0, 1, 2, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 0, 1, 2, 0, 2, 0, 0, 0, 1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 5, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 58 failed'); count += 1

board = [1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0, 2, 1, 1, 2, 1, 0, 0, 1, 1, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0, 2, 1, 1, 2, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 2, True)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 59 failed'); count += 1

board = [2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 0, 1, 2, 1, 1, 2, 2, 0, 2, 0, 2, 2, 0, 1, 0, 2, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 3, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 60 failed'); count += 1

board = [2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0, 1, 1, 1, 1, 2, 2, 0, 0, 2, 1, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 0, 1, 1, 1, 1, 2, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, True)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 61 failed'); count += 1

board = [2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 0, 0, 1, 1, 2, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 0, 0, 1, 1, 2, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 62 failed'); count += 1

board = [2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 0, 2, 2, 1, 1, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 3, False)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 63 failed'); count += 1

board = [2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 0, 2, 2, 2, 0, 1, 2, 0, 1, 2, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 0, 2, 2, 2, 0, 1, 2, 0, 1, 2, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, False)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 64 failed'); count += 1

board = [1, 1, 1, 1, 2, 1, 2, 2, 0, 2, 2, 2, 1, 2, 2, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 1, 2, 1, 2, 2, 0, 2, 2, 2, 1, 2, 2, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 6, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 65 failed'); count += 1

board = [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 2, 2, 0, 2, 1, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 1, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 6, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 66 failed'); count += 1

board = [1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 0, 0, 1, 2, 2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 3, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 67 failed'); count += 1

board = [1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 68 failed'); count += 1

board = [1, 2, 1, 2, 1, 2, 2, 0, 1, 2, 1, 2, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 2, 1, 2, 2, 0, 1, 2, 1, 2, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 6, True)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 69 failed'); count += 1

board = [2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 0, 2, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 3, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 70 failed'); count += 1

board = [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 0, 1, 1, 0, 2, 2, 2, 0, 1, 0, 0, 2, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 0, 2, 2, 2, 1, 2, 1, 0, 1, 1, 0, 2, 2, 2, 0, 1, 0, 0, 2, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, True)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 71 failed'); count += 1

board = [2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 0, 2, 2, 0, 2, 1, 1, 0, 2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 0, 2, 2, 0, 2, 1, 2, 0, 2, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 3, True)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 72 failed'); count += 1

board = [1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 5, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 73 failed'); count += 1

board = [2, 2, 1, 2, 0, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 2, 0, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 5, False)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 74 failed'); count += 1

board = [1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 0, 2, 1, 2, 0, 2, 2, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 0, 0, 1, 2, 0, 2, 2, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 2, True)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 75 failed'); count += 1

board = [2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 0, 2, 2, 1, 2, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 76 failed'); count += 1

board = [2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 0, 1, 1, 2, 1, 0, 2, 0, 1, 1, 2, 1, 0, 1, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 0, 1, 1, 2, 1, 0, 2, 0, 2, 1, 2, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 2, True)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 77 failed'); count += 1

board = [2, 2, 2, 2, 1, 2, 2, 1, 0, 1, 2, 2, 2, 0, 2, 0, 2, 1, 2, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 1, 2, 2, 1, 0, 1, 2, 2, 2, 0, 2, 0, 2, 1, 2, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 78 failed'); count += 1

board = [2, 1, 1, 2, 1, 2, 1, 0, 1, 1, 1, 2, 2, 2, 0, 2, 1, 0, 2, 1, 2, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 2, 1, 2, 1, 0, 1, 1, 1, 2, 2, 2, 0, 2, 1, 0, 2, 1, 2, 0, 1, 1, 0, 2, 2, 2, 0, 2, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 1, False)
# board with 10 rows
if not board_result == board_expected: print('apply_move test 79 failed'); count += 1

board = [1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 0, 0, 2, 1, 1, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 0, 2, 1, 1, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 80 failed'); count += 1

board = [2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 0, 2, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 0, False)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 81 failed'); count += 1

board = [2, 2, 2, 2, 2, 1, 1, 1, 0, 2, 1, 2, 2, 2, 2, 0, 2, 2, 1, 1, 1, 2, 0, 2, 1, 2, 2, 1, 0, 0, 2, 1, 1, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 2, 1, 1, 1, 0, 2, 1, 2, 2, 2, 2, 0, 2, 2, 1, 1, 1, 2, 0, 2, 1, 2, 2, 1, 0, 0, 2, 1, 1, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 3, False)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 82 failed'); count += 1

board = [2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 0, 2, 2, 2, 1, 1, 2, 0, 0, 1, 2, 2, 0, 1, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 0, 0, 1, 2, 2, 0, 1, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 3, False)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 83 failed'); count += 1

board = [0, 1, 0, 1, 1, 2, 1, 0, 2, 0, 1, 0, 2, 1, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [0, 1, 0, 1, 1, 2, 1, 0, 2, 0, 1, 0, 2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, True)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 84 failed'); count += 1

board = [2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, False)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 85 failed'); count += 1

board = [1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 4, True)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 86 failed'); count += 1

board = [1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 1, 1, 1, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 1, False)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 87 failed'); count += 1

board = [1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 0, 2, 2, 2, 0, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 0, 2, 2, 2, 0, 2, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 11 rows
if not board_result == board_expected: print('apply_move test 88 failed'); count += 1

board = [2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 1, True)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 89 failed'); count += 1

board = [1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 0, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 0, 1, 1, 0, 2, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 90 failed'); count += 1

board = [1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 0, 2, 1, 2, 1, 0, 2, 0, 1, 1, 1, 2, 0, 1, 0, 0, 2, 1, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 0, 2, 1, 2, 1, 0, 2, 0, 1, 1, 1, 2, 0, 1, 0, 0, 2, 1, 1, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 6, False)
# board with 13 rows
if not board_result == board_expected: print('apply_move test 91 failed'); count += 1

board = [1, 2, 2, 1, 0, 2, 2, 1, 2, 2, 2, 0, 1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 1, 2, 1, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 2, 1, 0, 2, 2, 1, 1, 2, 2, 0, 1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 1, True)
# board with 7 rows
if not board_result == board_expected: print('apply_move test 92 failed'); count += 1

board = [2, 2, 2, 2, 2, 1, 1, 0, 2, 2, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 0, 2, 1, 1, 1, 1, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 2, 1, 1, 0, 2, 2, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 0, 2, 1, 1, 1, 1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 5, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 93 failed'); count += 1

board = [2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 5, True)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 94 failed'); count += 1

board = [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 0, False)
# board with 8 rows
if not board_result == board_expected: print('apply_move test 95 failed'); count += 1

board = [2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 0, 1, 1, 0, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 0, 1, 1, 0, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 2, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 96 failed'); count += 1

board = [1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 0, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 0, 0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 1, True)
# board with 6 rows
if not board_result == board_expected: print('apply_move test 97 failed'); count += 1

board = [1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 0, 1, 1, 2, 2, 2, 2, 0, 2, 1, 0, 2, 1, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 0, 1, 1, 2, 2, 2, 2, 0, 2, 1, 0, 2, 1, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 0, False)
# board with 12 rows
if not board_result == board_expected: print('apply_move test 98 failed'); count += 1

board = [2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 1, 6, False)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 99 failed'); count += 1

board = [2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_expected = [1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_result = apply_move(board, 2, 0, True)
# board with 9 rows
if not board_result == board_expected: print('apply_move test 100 failed'); count += 1

print(f"apply_move: {100 - count} out of 100 passed.")
count = 0
board = [2, 2, 0, 2, 1, 2, 2, 1, 1, 0, 1, 2, 2, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 1 failed'); count += 1

board = [1, 1, 0, 2, 2, 1, 2, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 2 failed'); count += 1

board = [1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 0, 2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 3 failed'); count += 1

board = [2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 0, 2, 2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 4 failed'); count += 1

board = [1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 0, 2, 0, 1, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 5 failed'); count += 1

board = [1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 0, 2, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 6 failed'); count += 1

board = [2, 2, 1, 1, 1, 1, 1, 2, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 7 failed'); count += 1

board = [1, 2, 1, 2, 1, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 0, 2, 1, 2, 1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 8 failed'); count += 1

board = [1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 0, 2, 0, 1, 2, 1, 2, 0, 1, 0, 1, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 9 failed'); count += 1

board = [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0, 2, 2, 2, 2, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 10 failed'); count += 1

board = [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 0, 1, 1, 2, 2, 1, 2, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 11 failed'); count += 1

board = [2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 0, 1, 1, 1, 1, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 12 failed'); count += 1

board = [0, 1, 2, 1, 0, 2, 1, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 13 failed'); count += 1

board = [2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 14 failed'); count += 1

board = [2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 0, 1, 1, 2, 2, 0, 2, 0, 1, 1, 2, 2, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 15 failed'); count += 1

board = [2, 0, 1, 2, 1, 2, 1, 2, 0, 1, 2, 2, 0, 2, 0, 0, 2, 1, 1, 0, 2, 0, 0, 2, 2, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 16 failed'); count += 1

board = [1, 1, 1, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 1, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 17 failed'); count += 1

board = [1, 2, 1, 1, 2, 2, 2, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 18 failed'); count += 1

board = [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 0, 2, 1, 2, 2, 2, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 19 failed'); count += 1

board = [1, 1, 2, 2, 1, 1, 2, 1, 2, 0, 2, 2, 2, 2, 1, 2, 0, 2, 0, 1, 2, 2, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 20 failed'); count += 1

board = [2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 21 failed'); count += 1

board = [0, 1, 2, 1, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 22 failed'); count += 1

board = [2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 0, 2, 1, 1, 2, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 23 failed'); count += 1

board = [2, 1, 2, 2, 1, 2, 1, 2, 2, 0, 1, 0, 2, 1, 1, 1, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 24 failed'); count += 1

board = [1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 2, 2, 1, 2, 0, 1, 1, 0, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 25 failed'); count += 1

board = [2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 26 failed'); count += 1

board = [2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 0, 2, 1, 0, 2, 1, 2, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 27 failed'); count += 1

board = [1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 28 failed'); count += 1

board = [1, 2, 2, 1, 2, 1, 2, 1, 0, 2, 1, 2, 1, 2, 2, 0, 0, 2, 2, 1, 0, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 29 failed'); count += 1

board = [2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 30 failed'); count += 1

board = [2, 1, 1, 0, 2, 1, 2, 0, 1, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 31 failed'); count += 1

board = [1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 0, 1, 0, 1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 32 failed'); count += 1

board = [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 1, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 2, 1, 0, 2, 1, 2, 1, 1, 2, 0, 2, 0, 2, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 33 failed'); count += 1

board = [1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 34 failed'); count += 1

board = [1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 1, 2, 2, 2, 1, 1, 0, 1, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 35 failed'); count += 1

board = [2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 0, 2, 1, 2, 1, 2, 1, 0, 0, 2, 1, 2, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 36 failed'); count += 1

board = [2, 1, 2, 1, 2, 2, 1, 0, 1, 1, 2, 2, 2, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 37 failed'); count += 1

board = [2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 38 failed'); count += 1

board = [2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 0, 0, 1, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 39 failed'); count += 1

board = [1, 1, 2, 0, 2, 1, 1, 2, 2, 2, 0, 1, 0, 2, 2, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 40 failed'); count += 1

board = [1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 0, 1, 2, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 41 failed'); count += 1

board = [1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 0, 2, 1, 2, 1, 1, 1, 0, 2, 1, 0, 2, 2, 1, 0, 2, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 42 failed'); count += 1

board = [1, 1, 1, 1, 2, 0, 2, 2, 1, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 43 failed'); count += 1

board = [1, 2, 2, 2, 1, 1, 2, 1, 1, 0, 2, 2, 2, 1, 2, 1, 0, 2, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 44 failed'); count += 1

board = [2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 2, 1, 0, 2, 2, 2, 1, 1, 1, 0, 1, 1, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 45 failed'); count += 1

board = [2, 1, 1, 1, 2, 1, 1, 2, 2, 0, 2, 0, 0, 1, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 46 failed'); count += 1

board = [2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 0, 0, 1, 1, 2, 1, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 47 failed'); count += 1

board = [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 1, 0, 1, 1, 2, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 48 failed'); count += 1

board = [1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 0, 2, 2, 1, 2, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 49 failed'); count += 1

board = [2, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 50 failed'); count += 1

board = [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 51 failed'); count += 1

board = [1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 52 failed'); count += 1

board = [2, 2, 1, 1, 2, 0, 2, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 53 failed'); count += 1

board = [2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 54 failed'); count += 1

board = [2, 1, 2, 2, 2, 1, 2, 1, 0, 2, 2, 1, 1, 1, 1, 0, 2, 2, 2, 2, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 55 failed'); count += 1

board = [1, 2, 1, 1, 1, 1, 0, 2, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 56 failed'); count += 1

board = [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 0, 1, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 57 failed'); count += 1

board = [2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 0, 2, 2, 2, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 58 failed'); count += 1

board = [1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 0, 1, 1, 2, 0, 1, 0, 0, 2, 2, 1, 0, 1, 0, 0, 1, 1, 2, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 59 failed'); count += 1

board = [2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 60 failed'); count += 1

board = [2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 0, 1, 0, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 61 failed'); count += 1

board = [2, 1, 1, 2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 2, 2, 0, 1, 2, 1, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 62 failed'); count += 1

board = [1, 1, 2, 1, 2, 2, 2, 0, 1, 1, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 63 failed'); count += 1

board = [1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 64 failed'); count += 1

board = [1, 2, 1, 2, 1, 2, 1, 2, 0, 0, 2, 1, 2, 1, 2, 0, 0, 1, 2, 1, 2, 1, 0, 0, 2, 0, 1, 0, 2, 0, 0, 2, 0, 2, 0, 2, 0, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 65 failed'); count += 1

board = [2, 1, 1, 1, 2, 2, 1, 2, 2, 0, 2, 2, 2, 0, 1, 2, 0, 2, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 66 failed'); count += 1

board = [2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 67 failed'); count += 1

board = [2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 0, 0, 1, 1, 2, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 68 failed'); count += 1

board = [1, 1, 1, 2, 1, 1, 2, 1, 0, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 69 failed'); count += 1

board = [2, 2, 1, 1, 1, 2, 2, 0, 2, 1, 1, 2, 2, 1, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 70 failed'); count += 1

board = [2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1, 2, 0, 2, 0, 1, 1, 2, 2, 0, 1, 0, 2, 1, 1, 2, 0, 2, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 71 failed'); count += 1

board = [1, 0, 2, 2, 1, 2, 1, 2, 0, 2, 1, 2, 2, 1, 0, 0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 72 failed'); count += 1

board = [2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 0, 1, 1, 2, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 73 failed'); count += 1

board = [2, 1, 2, 1, 2, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 74 failed'); count += 1

board = [2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 0, 2, 2, 2, 0, 1, 1, 0, 2, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 75 failed'); count += 1

board = [2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 0, 1, 2, 2, 2, 2, 2, 0, 2, 0, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 76 failed'); count += 1

board = [1, 1, 1, 1, 2, 1, 2, 2, 0, 1, 2, 0, 2, 2, 0, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 77 failed'); count += 1

board = [1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 1, 0, 2, 1, 0, 1, 2, 2, 0, 2, 2, 0, 0, 1, 2, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 78 failed'); count += 1

board = [1, 2, 2, 2, 1, 2, 2, 1, 0, 1, 2, 2, 2, 2, 2, 0, 2, 1, 2, 0, 2, 1, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 79 failed'); count += 1

board = [2, 1, 1, 2, 2, 2, 1, 0, 2, 0, 0, 2, 1, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 80 failed'); count += 1

board = [1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 0, 1, 1, 1, 2, 1, 1, 0, 1, 1, 0, 2, 1, 2, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 81 failed'); count += 1

board = [2, 2, 2, 2, 1, 1, 1, 2, 2, 0, 2, 0, 1, 2, 1, 1, 0, 1, 0, 2, 1, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 82 failed'); count += 1

board = [2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 0, 2, 0, 1, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 0: print('check_victory test 83 failed'); count += 1

board = [2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 0, 2, 1, 1, 1, 2, 1, 0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 84 failed'); count += 1

board = [2, 1, 1, 1, 1, 0, 1, 2, 2, 1, 1, 2, 0, 2, 0, 1, 2, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 85 failed'); count += 1

board = [1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 0, 1, 2, 1, 1, 2, 2, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 86 failed'); count += 1

board = [1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 0, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 87 failed'); count += 1

board = [2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 0, 0, 1, 2, 1, 2, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 88 failed'); count += 1

board = [1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 0, 0, 2, 2, 0, 1, 2, 0, 0, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 89 failed'); count += 1

board = [2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 2, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 90 failed'); count += 1

board = [1, 2, 2, 1, 2, 1, 2, 0, 1, 1, 2, 2, 2, 1, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 91 failed'); count += 1

board = [2, 2, 2, 1, 2, 2, 2, 1, 0, 2, 1, 0, 1, 2, 2, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 92 failed'); count += 1

board = [2, 2, 1, 1, 2, 1, 0, 2, 2, 0, 2, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 93 failed'); count += 1

board = [1, 1, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 94 failed'); count += 1

board = [2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 2, 1, 2, 2, 2, 0, 2, 1, 1, 1, 0, 1, 0, 1, 2, 1, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 1: print('check_victory test 95 failed'); count += 1

board = [2, 1, 1, 2, 2, 2, 0, 1, 2, 2, 2, 2, 2, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 2: print('check_victory test 96 failed'); count += 1

board = [2, 2, 1, 1, 1, 2, 1, 0, 2, 0, 0, 2, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 1) == 0: print('check_victory test 97 failed'); count += 1

board = [2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 0, 1, 1, 1, 1, 2, 2, 0, 2, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 98 failed'); count += 1

board = [1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 1: print('check_victory test 99 failed'); count += 1

board = [1, 2, 1, 1, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2, 0, 2, 2, 1, 1, 2, 1, 0, 0, 1, 2, 1, 2, 1, 0, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_victory(board, 2) == 2: print('check_victory test 100 failed'); count += 1

print(f"check_victory: {100 - count} out of 100 passed.")
