"""
ex04 – Validity checks (rows, columns, boxes)

Goal:
- Implement functions to check if the sudoku respects the rules:

  1) No repeated non-zero number in any row.
  2) No repeated non-zero number in any column.
  3) No repeated non-zero number in any 3x3 box.

We will use these checks later in the solvers.
"""

from ex01_read_file import read_sudoku_file
from ex02_parse_grid import parse_sudoku


def no_duplicate_non_zero(values):
    """Return True if there is no repeated non-zero value in the list.

    Example: [5, 3, 0, 7] -> True
             [5, 3, 5, 0] -> False
    """
    # TODO: use a list to track seen numbers, or similar, with loops.
    pass


def is_row_valid(grid, row):
    """Return True if row "row" (0..8) has no repeated non-zero numbers."""
    # TODO: build a list of the row's values and call no_duplicate_non_zero
    pass


def is_col_valid(grid, col):
    """Return True if column "col" (0..8) has no repeated non-zero numbers."""
    # TODO: extract the column values with a loop, then call no_duplicate_non_zero
    pass


def is_box_valid(grid, box_row, box_col):
    """Return True if the 3x3 box is valid.

    box_row, box_col are in 0..2 and indicate which 3x3 block:
    (0,0) = top-left, (0,1) = top-middle, ..., (2,2) = bottom-right.
    """
    # TODO: compute starting row/col = box_row*3, box_col*3 and scan 3x3 cells
    pass


def is_grid_valid(grid):
    """Return True if all rows, cols and boxes are valid."""
    # TODO: loop over all rows, all cols, all boxes
    pass


def main():
    filename = "sudoku.txt"
    lines = read_sudoku_file(filename)
    grid = parse_sudoku(lines)
    print("Grid valid?", is_grid_valid(grid))


if __name__ == "__main__":
    main()
