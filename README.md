# Sudoku Quest 🧩

Welcome to **Sudoku Quest**.

Your mission: read a sudoku from a text file, show it nicely in the terminal, then write solvers that can complete the grid — from a simple logical solver to a full backtracking one.

This project is designed to:

* train you on **file reading** in Python
* practice **2D lists (matrices)**
* understand and implement **Sudoku rules**
* write and compare **two solving algorithms**

Everything uses only **simple Python**: loops, conditions, lists, functions.

---

## 1. File Format

A sudoku is stored in a text file with:

* 9 lines
* 9 characters per line
* digits `1`–`9` for filled cells
* `0` or `.` for empty cells

### Example

```
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

We provide example puzzles inside the `puzzles/` directory:

* `puzzles/sudoku_easy.txt`
* `puzzles/sudoku_medium.txt`
* `puzzles/sudoku_hard.txt`

You may replace them or add new ones using the same format.

---

## 2. Exercises Overview

You must complete the exercises **in order**. Each one introduces concepts used later.

### **`ex01_read_file.py` – Read the file**

* Implement `read_sudoku_file(filename)`.
* Open the file, read 9 lines, remove `\n`, return a list.

### **`ex02_parse_grid.py` – Build the grid**

* Implement `parse_sudoku(lines)`.
* Convert the 9 strings into a **9×9 matrix** of integers.
* `'1'..'9'` → numbers, `'0'` or `'.'` → 0.

### **`ex03_display_grid.py` – Display the grid nicely**

* Implement `display_sudoku(grid)`.
* Replace `0` with `.` when printing.
* Add separators to make it readable.

### **`ex04_validity_checks.py` – Sudoku rules**

Implement:

* `no_duplicate_non_zero(values)`
* `is_row_valid(grid, row)`
* `is_col_valid(grid, col)`
* `is_box_valid(grid, box_row, box_col)`
* `is_grid_valid(grid)`

These check that no row/column/box contains repeated numbers.

### **`ex05_easy_solver.py` – Logical solver (naked singles)**

Implement:

* `is_value_allowed(grid, row, col, value)`
* `possible_values_for_cell(grid, row, col)`
* `solve_sudoku_easy(grid)`

Strategy: if a cell has **exactly one** valid possible number, fill it. Repeat until no progress.

### **`ex06_backtracking_solver.py` – Full solver**

Implement:

* `find_empty_cell(grid)`
* `solve_sudoku_backtracking(grid)`

Strategy: try values recursively, backtrack when stuck. Solves all valid sudokus.

### **`ex07_solver_comparison.py` – Compare solvers**

Implement:

* `copy_grid(grid)` (manual deep copy)

Then:

* Show the original puzzle
* Run the easy solver
* Run the backtracking solver
* Compare results

---

## 3. How to Test Your Code

A script `run_sudoku_tests.py` is provided.

### Run tests for **one exercise**

```bash
python3 run_sudoku_tests.py 1
python3 run_sudoku_tests.py 3
python3 run_sudoku_tests.py 6
```

### Run tests for **all exercises**

```bash
python3 run_sudoku_tests.py
```

### Or use the wrapper script (recommended)

```bash
./run_sudoku_exercise.sh 1
./run_sudoku_exercise.sh ex04
./run_sudoku_exercise.sh all
```

This behaves like your Sorting Quest launcher.

---

## 4. Suggested Workflow (2-hour session)

1. **ex01**: Read file, print lines
2. **ex02**: Build 9×9 matrix
3. **ex03**: Display sudoku clearly
4. **ex04**: Implement rule-checking helpers
5. **ex05**: Solve easy puzzles using naked singles
6. **ex06**: Implement backtracking (start it even if you don’t finish)
7. **ex07**: Run comparison script on easy/medium/hard puzzles

Run tests regularly:

```bash
python3 run_sudoku_tests.py 3
```

---

## 5. Tips

* Use **print** often to debug.
* Write **simple loops** before trying to be clever.
* If a test fails, read the message carefully.
* Your code does not have to solve everything perfectly — the goal is to learn.

Good luck, engineer. Your first Sudoku awaits. 🧩
