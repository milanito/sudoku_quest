"""
ex02 – Parsing sudoku lines into a grid

Goal:
- Take the list of 9 strings read from the file.
- Convert it into a 9x9 matrix (list of 9 lists of 9 integers).

Rules:
- Digits '1'..'9' become integers 1..9.
- Characters '0' or '.' represent an empty cell and become 0.
- Use nested loops to fill the matrix.

You can reuse read_sudoku_file from ex01.
"""

from ex01_read_file import read_sudoku_file


def parse_sudoku(lines):
    """Convert lines (9 strings) into a 9x9 matrix of integers.

    Example line: "530070000"
    -> [5, 3, 0, 0, 7, 0, 0, 0, 0]

    Use loops and int(...) when appropriate.
    """
    # TODO:
    # 1) create an empty list 'grid'
    # 2) for each line, build a row list of 9 ints
    # 3) use 0 for '0' or '.' characters
    # 4) append each row to grid
    pass


def main():
    filename = "sudoku.txt"
    lines = read_sudoku_file(filename)
    grid = parse_sudoku(lines)
    print("Grid as Python list (raw):")
    # TODO: print each row of the grid
    pass


if __name__ == "__main__":
    main()
