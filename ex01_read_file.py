"""
ex01 – Reading a Sudoku file

Goal:
- Open a text file containing a sudoku.
- Read its content line by line.
- Return the list of lines without the final "\n".

Example file format (9 lines, 9 characters each):

530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079

Empty cells can be represented with '0' or '.'.

Rules:
- Use only basic Python: open, read, loops, len, print.
- Do NOT use advanced libraries.
"""


def read_sudoku_file(filename):
    """Open the file and return the list of lines without "\\n".

    Steps to implement:
    1) Open the file in read mode.
    2) Read all lines.
    3) Remove the final "\\n" from each line (if present).
    4) Return the list of cleaned lines.
    """
    # TODO: implement this function using open(...), a loop, and line.strip("\n")
    pass


def main():
    filename = "sudoku.txt"  # you can change this for tests
    print("Reading:", filename)
    lines = read_sudoku_file(filename)
    print("Raw lines from file:")
    # TODO: print each line to check everything works
    pass


if __name__ == "__main__":
    main()
