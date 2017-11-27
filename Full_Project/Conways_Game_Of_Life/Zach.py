__author__ = "Zachary Higgs"

from copy import deepcopy
from time import sleep


def board_setup(x):
    """
    Setup the board
    :param x: Size of the board used as a x by x
    :return: The board as a List of Lists
    """
    row = [' ' for i in range(x)]
    board = [row.copy() for i in range(x)]
    return board


def display_board(x):
    """
    Displaying the board in a human readable way
    :param x: The Generated board
    """

    # For b in i in x
    c = ''
    for i in x:

        a = 0
        p = ''
        for b in i:
            ilen = len(b)
            a += 1
            if b == ' ':
                p = p + "_|"

            elif b == '*':
                p = p + "*|"

            elif a == ilen:
                p = p + '\n'

                # else:
                #     raise False
        c = c + p
        print(p)


def a_count(b, y, x):
    """
    Count the

    :param b: Board Input
    :param y: Y co-ordnate of where we are
    :param x: X Co-ordnate of where we are
    :return:
    """

    # PWP: Why do you need to know? (I know the aswer now...)
    is_on_live = 0
    if b[y][x] == "*":
        is_on_live = 1

    count_of = 0
    s = [-1, 0, 1]
    for i in s:
        for j in s:
            if b[y + i][x + j] == "*":
                count_of += 1

    # PWP: I see... Quite nice idea; yet, it can be implemented more cleanly
    # Check if were checking an Alive square
    if (is_on_live == 1):
        count_of -= 1
    return count_of
    # return 3


def do_sim_1tick(ob, nb):
    """
    Do exactly one tick of simulation, no more then 1 no less then 1. 3 is right out...

    :param ob: The previous generation's (tick's) board
    :param nb: the New blank board to be working off of
    :return: A list of lists With the newest generation  worked out
    """

    # PWP: What all these bX, bY are for?
    # PWP: It looks like a mess from the time you had no a_count function and tried to do 2 things at once...
    # bY = 0
    # bX = 0
    # alive = 0
    # New_Board[7][7] = "*"
    for i in range(1, len(ob) - 1):
        for j in range(1, len(ob) - 1):
            # if (bY != 0 | bY != (len(old_board)-1) | bX != 0 | bX != (len(old_board)-1)):
            # alive=a_count(old_board,bX, bY)
            alive = a_count(ob, i, j)

            # TODO: Fix the Rules

            # PWP: Well, this is bad!
            # PWP: The cell coordinates (i,j) set in the for-loops
            # PWP: are never used! No wonder nothing makes sense...

            # if (alive >= 4 or alive <= 2 ):
            #     New_Board[bY][bX] = " "      #PWP: means: do nothing, as the new board is like this...
            # elif (alive == 3):
            #     New_Board[bY][bX] = "*"
            # elif (alive == 3 or alive == 2): #PWP: "alive == 3" will never bring you here, as it is handled by

            # PWP: the previous elif case; so the condition "alive == 2" would be
            # PWP: enough, if it were correct; but it ain't (!), as that should
            # PWP: only be considered with old_board[i][j]=='*'. So, here you go:
            #     New_Board[bY][bX] = "*"

            if alive == 3:
                nb[i][j] = "*"
            elif alive == 2 and ob[i][j] == '*':
                nb[i][j] = "*"
                # else:
                #     you can pass, or set spaces, or (best) leave it alone...

                # PWP: ??
                #     bX += 1
                # bX = 0
                # bY += 1

    return nb


# Board Debug
# board1 = board_setup(10)
# board1[1][1] = '*'

# print(board1)
# print(display_board(board1))

# new_board = board_setup(10)
# old_board = board_setup(10)
# old_board[3][3] = '*'
# old_board[2][3] = '*'
# old_board[4][3] = '*'
#
# # while True:
# #     new_board=do_sim_1Tick(old_board, new_board)
# #     # old_board= new_board.copy()
# #     # display_board(old_board)
#
# # new_board=do_sim_1Tick(old_board, new_board)
# # display_board(old_board)
# # print("\n")
# # display_board(new_board)
#
# # Require Deepcopy as piotr solution doesn't account for death, Just straight up generate a new board and start working
# # off the old board from last tick
# # As well Include sleep for auto generations
#
#
#
# display_board(old_board)
#
# while True:
#     new_board = do_sim_1tick(old_board, new_board)
#     display_board(new_board)
#     old_board = deepcopy(new_board)
#     new_board = board_setup(10)
#     sleep(1)
