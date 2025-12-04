#!/usr/bin/env bash
set -e

# run_sudoku_exercise.sh
# Wrapper script to run tests for one Sudoku exercise (or all),
# mirroring the behavior of your sorting "run_exercise.sh".
#
# Usage:
#   ./run_sudoku_exercise.sh 1      # tests for ex01_read_file
#   ./run_sudoku_exercise.sh ex02   # tests for ex02_parse_grid
#   ./run_sudoku_exercise.sh all    # tests for all exercises

if [ $# -ne 1 ]; then
  echo "Usage: $0 <1-6 | ex01-ex06 | all>"
  exit 1
fi

ARG="$1"

case "$ARG" in
  1|ex01)
    EX_NUM=1
    TITLE="ex01_read_file (reading sudoku file)"
    ;;
  2|ex02)
    EX_NUM=2
    TITLE="ex02_parse_grid (building 9x9 grid)"
    ;;
  3|ex03)
    EX_NUM=3
    TITLE="ex03_display_grid (pretty printing)"
    ;;
  4|ex04)
    EX_NUM=4
    TITLE="ex04_validity_checks (rows/cols/boxes)"
    ;;
  5|ex05)
    EX_NUM=5
    TITLE="ex05_easy_solver (naked singles)"
    ;;
  6|ex06)
    EX_NUM=6
    TITLE="ex06_backtracking_solver (full solver)"
    ;;
  all)
    echo "Running tests for ALL Sudoku exercises (ex01..ex06)..."
    echo
    python3 run_sudoku_tests.py
    exit 0
    ;;
  *)
    echo "Unknown argument: $ARG"
    echo "Usage: $0 <1-6 | ex01-ex06 | all>"
    exit 1
    ;;

esac

# Simple colors
FG_CYAN="\033[36m"
RESET="\033[0m"

# Color helper
c() {
  local text="$1"
  local code="$2"
  if [ -t 1 ]; then
    printf "%b%s%b" "$code" "$text" "$RESET"
  else
    printf "%s" "$text"
  fi
}

BOX_LINE="+------------------------------------------+"

printf "%s\n" "$BOX_LINE"
printf "| %s |\n" "$(c "Running tests for $TITLE" "$FG_CYAN")"
printf "%s\n" "$BOX_LINE"
printf "\n"

python3 run_sudoku_tests.py "$EX_NUM"
