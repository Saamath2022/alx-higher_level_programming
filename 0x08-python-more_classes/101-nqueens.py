#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the given position on the board.

    Args:
        board (list): The chessboard configuration.
        row (int): The row index to place the queen.
        col (int): The column index to place the queen.
        N (int): The size of the board.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(row):
        if board[i][col] == 'Q':
            return False

for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True


def solve_n_queens(N):
    """
    Solve the N queens problem and return all possible solutions.

    Args:
        N (int): The size of the chessboard.

    Returns:
        list: A list of all possible solutions.
    """
    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        """
        Backtrack to find all possible solutions.

        Args:
            row (int): The current row being considered.
        """
        if row == N:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)


    solutions = solve_n_queens(N)
    for solution in solutions:
        for row in solution:
            print(row)
        print()
