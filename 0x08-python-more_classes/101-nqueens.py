#!/usr/bin/python3
import sys
"""Attempt to solve nqueens chess challenge."""


def is_safe(board, row, col, n):
    """Checks if placing a Queen at the specified position is safe

    Param:
        board: current state of the chessboard
        row: row to check
        col: column to check
        n: size of the chessboard

    Returns:
        True if it is safe to place a Queen, False if otherwise
    """
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def print_board(board):
    """Print the chessboard with queens placed

    Param:
        board: current state of the chessboard
    """
    n = len(board)
    soln = [[i, board[i]] for i in range(n)]
    print(soln)


def solve_nqueens(board, row, n):
    """Recursively solve the N-Queens with the use of backtracking

    Param:
        board: current state of the chessboard
        row: row being considered in current state
        n: size of the chessboard
    """
    if row == n:
        # found a soln, print the board
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """Solve the N-queens problem for the given board size.

    Param:
        n: size of the chessboard
    Prints:
        every possible soln to the problem
    """
    if not isinstance(n, int):
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
