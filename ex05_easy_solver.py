"""
ex05 – Easy logical solver (naked singles)

Goal:
- Implement a simple solver based on the idea:
  "If a cell has only ONE possible value, fill it." (naked single)

This solver will not solve all sudokus, but it's a good first algorithm.

You will need the validity checks from ex04 to know which values are allowed
in a cell.
"""

from ex01_read_file import read_sudoku_file
from ex02_parse_grid import parse_sudoku
from ex03_display_grid import display_sudoku
from ex04_validity_checks import is_row_valid, is_col_valid, is_box_valid, is_grid_valid


def is_cell_empty(grid, row, col):
    """Return True if the cell (row, col) is empty (value 0)."""
    return grid[row][col] == 0


def is_value_allowed(grid, row, col, value):
    """Return True if putting 'value' in (row, col) keeps the grid valid.

    Hint: temporarily set the cell, check row/col/box, then reset.
    """
    # TODO: implement the check without using any shortcuts.
    pass


def possible_values_for_cell(grid, row, col):
    """Return a list of possible values (1..9) for cell (row, col).

    If the cell is not empty, return an empty list.
    """
    # TODO: loop value from 1 to 9, test with is_value_allowed
    pass


def solve_sudoku_easy(grid):
    """Try to solve the sudoku using only naked singles.

    Algorithm idea:
    - Repeat:
        - for each cell:
            - if it is empty, compute its possible values
            - if there is exactly ONE possible value, fill it
      until:
        - no cell was filled in a full pass, or
        - the grid is complete (no zeros).

    Return True if the grid is completely solved, False otherwise.
    """
    # TODO: implement the iterative algorithm, with a flag to detect progress
    pass


def main():
    filename = "sudoku.txt"
    lines = read_sudoku_file(filename)
    grid = parse_sudoku(lines)

    print("Initial grid:")
    display_sudoku(grid)

    solved = solve_sudoku_easy(grid)

    print("\nAfter easy solver:")
    display_sudoku(grid)
    print("Solved by easy solver?", solved)


if __name__ == "__main__":
    main()
