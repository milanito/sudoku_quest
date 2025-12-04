"""
ex07 – Comparing solvers and showing statistics

Goal:
- Use both the easy solver (naked singles) and the backtracking solver.
- Display the sudoku before and after each solver.
- Optionally count steps or recursive calls to compare algorithms.

This exercise is a synthesis of everything you did:
- file reading
- grid parsing
- display
- validity checks
- two different solving strategies
"""

from ex01_read_file import read_sudoku_file
from ex02_parse_grid import parse_sudoku
from ex03_display_grid import display_sudoku
from ex04_validity_checks import is_grid_valid
from ex05_easy_solver import solve_sudoku_easy
from ex06_backtracking_solver import solve_sudoku_backtracking


def copy_grid(grid):
    """Return a deep copy of the grid (9x9 list of lists).

    You must NOT use advanced shortcuts. Use explicit loops.
    """
    # TODO: implement a manual copy of the 2D list
    pass


def main():
    filename = "sudoku.txt"  # you can change between easy/hard instances
    lines = read_sudoku_file(filename)
    original_grid = parse_sudoku(lines)

    print("Original grid:")
    display_sudoku(original_grid)

    print("\nTrying easy solver (ex05)...")
    grid_easy = copy_grid(original_grid)
    solved_easy = solve_sudoku_easy(grid_easy)
    display_sudoku(grid_easy)
    print("Solved by easy solver?", solved_easy)

    print("\nTrying backtracking solver (ex06)...")
    grid_bt = copy_grid(original_grid)
    solved_bt = solve_sudoku_backtracking(grid_bt)
    display_sudoku(grid_bt)
    print("Solved by backtracking solver?", solved_bt)


if __name__ == "__main__":
    main()
