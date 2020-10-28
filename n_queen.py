import numpy as np


def view_board(board):
    return np.matrix(board)


def gen_board(n):
    col = [0 for x in range(n)]
    board = [col.copy() for x in range(n)]
    return board


def safe(r, col, board):
    # errors
    if (col or r) > len(board):
        raise ValueError


    if col == 0:
        return True
    if 1 in board[r]:
        return False
    if r > 0:
        if board[r-1][col-1] == 1:
            return False
        if r < len(board)-1:
            if board[r+1][col-1] == 1:
                return False
    return True





def solve(col, N, board):
    if col >= N:
        return True

    for x in range(N):
        if safe(x, col, board):
            
            board[x][col] = 1

            if solve(col + 1, N, board):
                return True

            board[x][col] = 0

    return False



def main(size):
    board = gen_board(size)
    start_col = 0

    if solve(start_col, size, board):
        return print(view_board(board))
    else:
        print("The program did not solve.")



# testing
main(4)
# TODO: implement argparse so that you can choose the size of
# the board from the cli
