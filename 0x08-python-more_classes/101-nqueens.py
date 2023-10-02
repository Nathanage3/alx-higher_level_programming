#!/usr/bin/python3
import sys

def print_solution(board):
    """Print the board"""
    res = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                res.append([i, j])
    print(res)


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """Using backtracking to place the N queens"""

    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens(board, col + 1):
                print_solution(board)
            board[i][col] = 0

    return False


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0 for _ in range(N)] for _ in range(N)]
solve_nqueens(board, 0)
