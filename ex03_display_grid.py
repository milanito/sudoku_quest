"""
ex03 – Displaying the sudoku in the console

Goal:
- Print the 9x9 grid in a readable way.
- Add separators every 3 rows and 3 columns.

Example display (0 = empty):

+-------+-------+-------+
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
+-------+-------+-------+
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
+-------+-------+-------+
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
+-------+-------+-------+

Rules:
- Use '.' to display empty cells (value 0).
- Use nested loops and print.
"""

from ex01_read_file import read_sudoku_file
from ex02_parse_grid import parse_sudoku


def display_sudoku(grid):
    """Display the sudoku grid nicely in the console."""
    # TODO:
    # For each row index r:
    #   - print a horizontal line before rows 0, 3, 6
    #   - print values with '|' separators after columns 2 and 5
    # Use '.' for zeros, the number otherwise.
    pass


def main():
    filename = "sudoku.txt"
    lines = read_sudoku_file(filename)
    grid = parse_sudoku(lines)
    display_sudoku(grid)


if __name__ == "__main__":
    main()
