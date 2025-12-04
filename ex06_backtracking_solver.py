"""
ex06 – Backtracking solver (full search)

Goal:
- Implement a recursive solver that can solve any valid sudoku.

Algorithm (backtracking):
1) Find an empty cell.
2) If there is none, the grid is solved.
3) Otherwise, try values 1..9:
   - if a value is allowed in the cell:
       - put the value in the cell
       - recursively try to solve the rest of the grid
       - if success, keep it and return True
       - if failure, reset the cell to 0 and try the next value
4) If no value works, return False.
"""

from ex01_read_file import read_sudoku_file
from ex02_parse_grid import parse_sudoku
from ex03_display_grid import display_sudoku
from ex04_validity_checks import is_row_valid, is_col_valid, is_box_valid, is_grid_valid
from ex05_easy_solver import is_cell_empty, is_value_allowed


def find_empty_cell(grid):
    """Return (row, col) of the first empty cell, or (-1, -1) if none."""
    # TODO: scan grid row by row, col by col, and return the first (r,c) with 0
    pass


def solve_sudoku_backtracking(grid):
    """Solve the sudoku using backtracking.

    Modify grid in place and return True if a solution was found.
    Return False if there is no solution.
    """
    # TODO:
    # 1) find an empty cell
    # 2) if none, return True
    # 3) for value in 1..9:
    #       if allowed:
    #           place it
    #           if recursive call succeeds: return True
    #           otherwise reset
    #    after loop, return False
    pass


def main():
    filename = "sudoku.txt"
    lines = read_sudoku_file(filename)
    grid = parse_sudoku(lines)

    print("Initial grid:")
    display_sudoku(grid)

    solved = solve_sudoku_backtracking(grid)

    print("\nAfter backtracking solver:")
    display_sudoku(grid)
    print("Solved?", solved)


if __name__ == "__main__":
    main()
