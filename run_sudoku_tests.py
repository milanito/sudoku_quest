#!/usr/bin/env python3
"""
run_sudoku_tests.py

Small test runner for the Sudoku Quest exercises.

Usage:
    python3 run_sudoku_tests.py         # run all tests
    python3 run_sudoku_tests.py 3       # run tests for exercise 3 only
"""

import sys

FG_RED = "\033[31m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"
FG_CYAN = "\033[36m"
RESET = "\033[0m"


def c(text, code):
    if sys.stdout.isatty():
        return f"{code}{text}{RESET}"
    return text


def run_case(desc, fn):
    try:
        ok = fn()
    except Exception as e:
        print(f"  {c('[FAIL]', FG_RED)} {desc} (error: {e})")
        return False
    if ok:
        print(f"  {c('[ OK ]', FG_GREEN)} {desc}")
        return True
    else:
        print(f"  {c('[FAIL]', FG_RED)} {desc}")
        return False


# ----------------------
# Tests per exercise
# ----------------------


def test_ex01():
    print(c("== ex01_read_file ==", FG_CYAN))
    try:
        from ex01_read_file import read_sudoku_file
    except Exception as e:
        print("  Import error:", e)
        return 0, 1

    passed = 0
    total = 0

    total += 1

    def t1():
        lines = read_sudoku_file("puzzles/sudoku_easy.txt")
        # must have 9 lines
        return isinstance(lines, list) and len(lines) == 9 and all(
            isinstance(line, str) for line in lines
        )

    if run_case("read_sudoku_file('puzzles/sudoku_easy.txt') returns 9 lines", t1):
        passed += 1

    return passed, total


def test_ex02():
    print(c("== ex02_parse_grid ==", FG_CYAN))
    try:
        from ex01_read_file import read_sudoku_file
        from ex02_parse_grid import parse_sudoku
    except Exception as e:
        print("  Import error:", e)
        return 0, 2

    passed = 0
    total = 0

    lines = read_sudoku_file("puzzles/sudoku_easy.txt")

    total += 1

    def t1():
        grid = parse_sudoku(lines)
        return (
            isinstance(grid, list)
            and len(grid) == 9
            and all(isinstance(row, list) and len(row) == 9 for row in grid)
        )

    if run_case("parse_sudoku returns a 9x9 list", t1):
        passed += 1

    total += 1

    def t2():
        grid = parse_sudoku(lines)
        # first row "530070000" -> [5,3,0,0,7,0,0,0,0]
        return grid[0][0] == 5 and grid[0][1] == 3 and grid[0][2] == 0

    if run_case("parse_sudoku correctly converts digits/zeros", t2):
        passed += 1

    return passed, total


def test_ex03():
    print(c("== ex03_display_grid ==", FG_CYAN))
    try:
        from ex01_read_file import read_sudoku_file
        from ex02_parse_grid import parse_sudoku
        from ex03_display_grid import display_sudoku
    except Exception as e:
        print("  Import error:", e)
        return 0, 1

    passed = 0
    total = 0

    total += 1

    def t1():
        lines = read_sudoku_file("puzzles/sudoku_easy.txt")
        grid = parse_sudoku(lines)
        # We can't easily check the exact ASCII art here,
        # but we can check that it doesn't crash.
        display_sudoku(grid)
        return True

    if run_case("display_sudoku runs without error", t1):
        passed += 1

    return passed, total


def test_ex04():
    print(c("== ex04_validity_checks ==", FG_CYAN))
    try:
        from ex01_read_file import read_sudoku_file
        from ex02_parse_grid import parse_sudoku
        from ex04_validity_checks import (
            no_duplicate_non_zero,
            is_row_valid,
            is_col_valid,
            is_box_valid,
            is_grid_valid,
        )
    except Exception as e:
        print("  Import error:", e)
        return 0, 4

    passed = 0
    total = 0

    total += 1

    def t1():
        return no_duplicate_non_zero([5, 3, 0, 7]) and not no_duplicate_non_zero(
            [5, 3, 5, 0]
        )

    if run_case("no_duplicate_non_zero basic", t1):
        passed += 1

    lines = read_sudoku_file("puzzles/sudoku_easy.txt")
    grid = parse_sudoku(lines)

    total += 1

    def t2():
        return is_row_valid(grid, 0) and is_col_valid(grid, 0)

    if run_case("row/col valid on initial grid", t2):
        passed += 1

    total += 1

    def t3():
        # box (0,0) should be valid initially
        return is_box_valid(grid, 0, 0)

    if run_case("box valid on initial grid", t3):
        passed += 1

    total += 1

    def t4():
        return is_grid_valid(grid)

    if run_case("whole grid valid initially", t4):
        passed += 1

    return passed, total


def test_ex05():
    print(c("== ex05_easy_solver ==", FG_CYAN))
    try:
        from ex01_read_file import read_sudoku_file
        from ex02_parse_grid import parse_sudoku
        from ex05_easy_solver import solve_sudoku_easy
        from ex03_display_grid import display_sudoku
    except Exception as e:
        print("  Import error:", e)
        return 0, 1

    passed = 0
    total = 0

    total += 1

    def t1():
        lines = read_sudoku_file("puzzles/sudoku_easy.txt")
        grid = parse_sudoku(lines)
        solved = solve_sudoku_easy(grid)
        # We don't require full solve here (depends on implementation),
        # but grid should at least remain valid (no rule broken).
        # We just check it doesn't crash and returns a bool.
        return isinstance(solved, bool)

    if run_case("solve_sudoku_easy runs and returns a bool", t1):
        passed += 1

    return passed, total


def test_ex06():
    print(c("== ex06_backtracking_solver ==", FG_CYAN))
    try:
        from ex01_read_file import read_sudoku_file
        from ex02_parse_grid import parse_sudoku
        from ex06_backtracking_solver import solve_sudoku_backtracking
        from ex04_validity_checks import is_grid_valid
    except Exception as e:
        print("  Import error:", e)
        return 0, 2

    passed = 0
    total = 0

    total += 1

    def t1():
        lines = read_sudoku_file("puzzles/sudoku_easy.txt")
        grid = parse_sudoku(lines)
        solved = solve_sudoku_backtracking(grid)
        return solved is True and is_grid_valid(grid)

    if run_case("backtracking solves sudoku_easy.txt", t1):
        passed += 1

    total += 1

    def t2():
        lines = read_sudoku_file("puzzles/sudoku_hard.txt")
        grid = parse_sudoku(lines)
        solved = solve_sudoku_backtracking(grid)
        # For hard puzzle, we expect True as well (full solver)
        return solved is True and is_grid_valid(grid)

    if run_case("backtracking solves sudoku_hard.txt", t2):
        passed += 1

    return passed, total


ALL_TESTS = {
    1: test_ex01,
    2: test_ex02,
    3: test_ex03,
    4: test_ex04,
    5: test_ex05,
    6: test_ex06,
    # ex07 is mostly integration; you can run it directly
}


def run_one(ex_num):
    if ex_num not in ALL_TESTS:
        print(f"No tests defined for exercise {ex_num}.")
        return
    passed, total = ALL_TESTS[ex_num]()
    print(f"--> ex0{ex_num} summary: {passed}/{total} tests passed.\n")


def run_all():
    total_passed = 0
    total_tests = 0
    for ex_num in sorted(ALL_TESTS.keys()):
        p, t = ALL_TESTS[ex_num]()
        total_passed += p
        total_tests += t
        print(f"--> ex0{ex_num} summary: {p}/{t} tests passed.\n")
    print("======== OVERALL ========")
    print(f"Total: {total_passed}/{total_tests} tests passed.")


def main():
    if len(sys.argv) == 2:
        try:
            ex_num = int(sys.argv[1])
        except ValueError:
            print("Usage: python3 run_sudoku_tests.py [exercise_number]")
            return
        run_one(ex_num)
    else:
        run_all()


if __name__ == "__main__":
    main()
