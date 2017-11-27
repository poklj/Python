from Conways_Game_Of_Life.Zach import *


new_board = board_setup(10)
old_board = board_setup(10)
old_board[3][3] = '*'
old_board[2][3] = '*'
old_board[4][3] = '*'

display_board(old_board)

while True:
    new_board = do_sim_1tick(old_board, new_board)
    display_board(new_board)
    old_board = deepcopy(new_board)
    new_board = board_setup(10)
    sleep(1)