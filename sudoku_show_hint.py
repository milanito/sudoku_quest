#!/usr/bin/env python3
"""
sudoku_show_hint.py

Show progressive hints for the Sudoku Quest exercises.

Usage:
    python3 sudoku_show_hint.py 1
    python3 sudoku_show_hint.py 4
    python3 sudoku_show_hint.py 6
"""

import sys

FG_CYAN = "\033[36m"
FG_YELLOW = "\033[33m"
FG_GREEN = "\033[32m"
RESET = "\033[0m"


def c(text, code):
    if sys.stdout.isatty():
        return f"{code}{text}{RESET}"
    return text


def print_header(title):
    line = "-" * (len(title) + 4)
    print(c(line, FG_CYAN))
    print(c(f"| {title} |", FG_CYAN))
    print(c(line, FG_CYAN))
    print()


# -------------------------
# Hints per exercise
# -------------------------

def hints_ex01():
    print_header("Hints for ex01_read_file.py – Reading a file")

    print(c("Hint 1 – What does ex01 want?", FG_YELLOW))
    print("- You have a text file like puzzles/sudoku_easy.txt.")
    print("- You must open this file, read the 9 lines, and remove the '\\n' at the end.")
    print("- The function read_sudoku_file(filename) must return a list of 9 strings.")
    print()

    print(c("Hint 2 – Using open(...)", FG_YELLOW))
    print("Basic pattern to read a file:")
    print("    f = open(filename, \"r\")")
    print("    lines = f.readlines()")
    print("    f.close()")
    print("This gives you a list of lines, each line ending with '\\n'.")
    print()

    print(c("Hint 3 – Safer version with with open(...)", FG_YELLOW))
    print("A very common pattern is:")
    print("    with open(filename, \"r\") as f:")
    print("        lines = f.readlines()")
    print("In this case, you do NOT call f.close(), Python does it for you.")
    print()

    print(c("Hint 4 – Removing the newline", FG_YELLOW))
    print("Each line you read ends with '\\n'. You can remove it with:")
    print("    clean_line = line.strip(\"\\n\")")
    print("So you can build a new list:")
    print("    result = []")
    print("    for line in lines:")
    print("        result.append(line.strip(\"\\n\"))")
    print("Return result at the end.")
    print()

    print(c("Hint 5 – Testing your function", FG_YELLOW))
    print("- Call read_sudoku_file(\"puzzles/sudoku_easy.txt\") in main()")
    print("- Print the list, and check that you get 9 strings with no '\\n'.")
    print("- You can also print len(lines) to check.")


def hints_ex02():
    print_header("Hints for ex02_parse_grid.py – Building the 9x9 grid")

    print(c("Hint 1 – What do you start from?", FG_YELLOW))
    print("- You already have a list of 9 strings from ex01, each string has 9 characters.")
    print("- You now need to convert these 9 strings into a 9x9 list of integers.")
    print()

    print(c("Hint 2 – Structure of the grid", FG_YELLOW))
    print("- The grid is a list of rows.")
    print("- Each row is a list of 9 integers.")
    print("So you want something like: [[...9 ints...], [...9 ints...], ... 9 rows ...]")
    print()

    print(c("Hint 3 – Translating characters", FG_YELLOW))
    print("- For each character:")
    print("    - if it is '0' or '.', it becomes 0 (empty cell).")
    print("    - otherwise it is a digit '1'..'9', so you can convert with int().")
    print("Example:")
    print("    if ch == '0' or ch == '.':")
    print("        value = 0")
    print("    else:")
    print("        value = int(ch)")
    print()

    print(c("Hint 4 – Nested loops", FG_YELLOW))
    print("- Outer loop: go through each line.")
    print("- Inner loop: go through each character in the line.")
    print("Build a row like this:")
    print("    row = []")
    print("    for col_index from 0 to 8:")
    print("        ch = line[col_index]")
    print("        convert ch to value as above, then append to row.")
    print("After the inner loop, append row to grid.")
    print()

    print(c("Hint 5 – Sanity checks", FG_YELLOW))
    print("- After parse_sudoku, print len(grid) -> should be 9.")
    print("- Print len(grid[0]) -> should also be 9.")
    print("- Try printing the first row to see if it matches what you expect.")


def hints_ex03():
    print_header("Hints for ex03_display_grid.py – Displaying the grid")

    print(c("Hint 1 – Basic printing", FG_YELLOW))
    print("- You already have a 9x9 grid of integers.")
    print("- First step: try to print each row with a simple loop.")
    print("Example:")
    print("    for r in range(9):")
    print("        print(grid[r])  # just to check")
    print()

    print(c("Hint 2 – Replace 0 with '.'", FG_YELLOW))
    print("- When you display, you MUST not show 0, but '.'.")
    print("Inside your printing loop:")
    print("    if grid[r][c] == 0:")
    print("        ch = '.'")
    print("    else:")
    print("        ch = str(grid[r][c])")
    print("Then print ch with a space.")
    print()

    print(c("Hint 3 – Add vertical separators", FG_YELLOW))
    print("- You want vertical bars after columns 2 and 5.")
    print("Example inside the inner loop:")
    print("    if c == 3 or c == 6:  # after 3 elements printed")
    print("        print('|', end=' ')")
    print("Adjust depending on how you count columns (0..8).")
    print()

    print(c("Hint 4 – Add horizontal separators", FG_YELLOW))
    print("- Before printing rows 0, 3, and 6, print a line like:")
    print("    print('+-------+-------+-------+')")
    print("- After printing row 8, print it again.")
    print()

    print(c("Hint 5 – end=' ' and print()", FG_YELLOW))
    print("- If you want to print several things on the same line, use end=' ' in print().")
    print("Example:")
    print("    print(ch, end=' ')")
    print("At the end of the row, call:")
    print("    print()  # to move to next line")


def hints_ex04():
    print_header("Hints for ex04_validity_checks.py – Rules")

    print(c("Hint 1 – no_duplicate_non_zero", FG_YELLOW))
    print("- Idea: build a list of 'seen' numbers.")
    print("- For each value in the list:")
    print("    - if value == 0: skip")
    print("    - if value already in seen: return False")
    print("    - otherwise, add it to seen.")
    print("At the end, if no duplicates: return True.")
    print()

    print(c("Hint 2 – is_row_valid(grid, row)", FG_YELLOW))
    print("- Take the row (grid[row]).")
    print("- Call no_duplicate_non_zero on that list.")
    print("Return the result.")
    print()

    print(c("Hint 3 – is_col_valid(grid, col)", FG_YELLOW))
    print("- Build a list of values in column col:")
    print("    values = []")
    print("    for r in range(9):")
    print("        values.append(grid[r][col])")
    print("- Then call no_duplicate_non_zero(values).")
    print()

    print(c("Hint 4 – is_box_valid(grid, box_row, box_col)", FG_YELLOW))
    print("- Each box is 3x3.")
    print("- Starting row index = box_row * 3")
    print("- Starting col index = box_col * 3")
    print("- Then loop r from start_row to start_row+2, same for c.")
    print("- Collect values in a list and call no_duplicate_non_zero.")
    print()

    print(c("Hint 5 – is_grid_valid(grid)", FG_YELLOW))
    print("- Check all rows with is_row_valid.")
    print("- Check all columns with is_col_valid.")
    print("- Check all boxes with is_box_valid:")
    print("    for box_row in 0..2:")
    print("        for box_col in 0..2:")
    print("            if box not valid -> grid not valid.")


def hints_ex05():
    print_header("Hints for ex05_easy_solver.py – Naked singles")

    print(c("Hint 1 – is_value_allowed(grid, row, col, value)", FG_YELLOW))
    print("- A simple method:")
    print("  1) Remember the old value: old = grid[row][col]")
    print("  2) Put the new value: grid[row][col] = value")
    print("  3) Check row/col/box with is_row_valid, is_col_valid, is_box_valid")
    print("  4) Restore the old value: grid[row][col] = old")
    print("  5) Return True/False depending on validity.")
    print()

    print(c("Hint 2 – possible_values_for_cell", FG_YELLOW))
    print("- If the cell is not empty, return [].")
    print("- Otherwise:")
    print("    possibilities = []")
    print("    for value in range(1, 10):")
    print("        if is_value_allowed(grid, row, col, value):")
    print("            possibilities.append(value)")
    print("    return possibilities")
    print()

    print(c("Hint 3 – solve_sudoku_easy(grid)", FG_YELLOW))
    print("- Use a loop that repeats until no progress:")
    print("    progress = True")
    print("    while progress:")
    print("        progress = False")
    print("        for each cell:")
    print("            if empty:")
    print("                compute possible values")
    print("                if exactly one value:")
    print("                    put it in the grid")
    print("                    progress = True")
    print()

    print(c("Hint 4 – Stop conditions", FG_YELLOW))
    print("- When an entire pass over the grid does not fill any cell, stop.")
    print("- Then check if the grid is complete (no zeros) and valid.")
    print("- If yes, return True; otherwise return False.")


def hints_ex06():
    print_header("Hints for ex06_backtracking_solver.py – Full solver")

    print(c("Hint 1 – find_empty_cell(grid)", FG_YELLOW))
    print("- Loop over all rows and columns.")
    print("- As soon as you find grid[r][c] == 0, return (r, c).")
    print("- If you never find 0, return (-1, -1).")
    print()

    print(c("Hint 2 – General idea of backtracking", FG_YELLOW))
    print("- Backtracking tries values and goes deeper recursively.")
    print("- If a choice leads to a dead end, you go back and try another value.")
    print()

    print(c("Hint 3 – Structure of solve_sudoku_backtracking", FG_YELLOW))
    print("- First, find an empty cell:")
    print("    row, col = find_empty_cell(grid)")
    print("- If row == -1: there is no empty cell -> sudoku solved -> return True.")
    print()

    print(c("Hint 4 – Trying values 1..9", FG_YELLOW))
    print("- For value in 1..9:")
    print("    if is_value_allowed(grid, row, col, value):")
    print("        put value in grid[row][col]")
    print("        if solve_sudoku_backtracking(grid) returns True:")
    print("            return True")
    print("        else:")
    print("            reset grid[row][col] = 0  (backtrack)")
    print()

    print(c("Hint 5 – Failure", FG_YELLOW))
    print("- After trying all values 1..9, if none works:")
    print("    return False")
    print("- This tells the previous recursive call that this path leads nowhere.")
    print()

    print(c("Hint 6 – Combine with easy solver (optional idea)", FG_YELLOW))
    print("- You can (optionally) call the easy solver first to simplify the grid.")
    print("- Not required, but can be a nice improvement once backtracking works.")


HINTS = {
    1: hints_ex01,
    2: hints_ex02,
    3: hints_ex03,
    4: hints_ex04,
    5: hints_ex05,
    6: hints_ex06,
}


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 sudoku_show_hint.py <exercise_number>")
        print("Example: python3 sudoku_show_hint.py 1")
        return
    try:
        ex = int(sys.argv[1])
    except ValueError:
        print("Exercise number must be an integer.")
        return

    if ex not in HINTS:
        print(f"No hints defined for exercise {ex}.")
        return

    HINTS[ex]()


if __name__ == "__main__":
    main()
