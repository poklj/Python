__author__ = "Zachary Higgs"



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
                p = p + "_"
            elif b == '*':
                p = p + "*"
            elif a == ilen:
                p = p + '\n'
            else:
                raise False
        c = c + p
        print(p)

def a_count(b, y, x):
    is_on_live = 0
    if b[y][x] == "*":
        is_on_live = 1

    countof = 0
    s = [-1, 0, 1]
    for i in s:
        for j in s:
            if (b[y+i][x+j] == "*"):
               countof += 1
    # Check if were checking an Alive square
    if (is_on_live == 1):
        countof -= 1
    return countof
    #return 3

def do_sim_1Tick(old_board, New_Board):
    bY = 0
    bX = 0
    alive = 0
    # New_Board[7][7] = "*"
    for i in range(1,len(old_board)-1):
        for j in range(1,len(old_board)-1):
            # if (bY != 0 | bY != (len(old_board)-1) | bX != 0 | bX != (len(old_board)-1)):
            alive=a_count(old_board,bX, bY)
            if (alive >= 4 | alive <= 2 ):
                New_Board[bY][bX] = "_"
            elif (alive == 3):
                New_Board[bY][bX] = "*"
            elif (alive == 3 | alive == 2):
                New_Board[bY][bX] = "*"

            bX += 1
        bX = 0
        bY += 1

    return New_Board






# Board Debug
# board1 = board_setup(10)
# board1[1][1] = '*'

# print(board1)
# print(display_board(board1))

new_board = board_setup(10)
old_board = board_setup(10)
old_board[3][3] = '*'
old_board[2][3] = '*'
old_board[4][3] = '*'
# while True:
#     new_board=do_sim_1Tick(old_board, new_board)
#     # old_board= new_board.copy()
#     # display_board(old_board)

new_board=do_sim_1Tick(old_board, new_board)
display_board(old_board)
display_board(new_board)