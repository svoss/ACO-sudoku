import numpy as np
DIGITS = "123456789"


def parse_grid(grid):
    chars = [c for c in grid if c in DIGITS or c in "0."]
    values = [(i, c) for i, c in enumerate(chars) if c in DIGITS]
    result = np.zeros((9, 9, 9))
    for i, c in values:
        row = i // 9
        col = i % 9
        v = int(c) - 1
        result[row, col, v] = 1
    return result


def get_val(X, r, c):
    for v in range(0, 9):
        if X[r, c, v] == 1:
            return DIGITS[v]
    return "."


def display(X):
    chars = list()
    for r in range(0, 9):
        for c in range(0, 9):
            if c in (3, 6):
                chars.append("|")
            chars.append(get_val(X, r, c))
        if r != 8:
            chars.append("\n")
            if r in (2, 5):
                chars.append("---+---+---\n")
    print("".join(chars))


def load_file(filename):
    with open(filename, 'r') as fh:
        data = fh.read()
    return data

def get_valid_moves(X):
    valid_moves = np.ones((9, 9, 9))
    for v in range(0, 9):
        filled_boxes = []
        filled_rows = []
        filled_cols = []
        already_set = []
        # Find the location of the ones
        for r in range(0, 9):
            for c in range(0, 9):
                if X[r, c, v] == 1:
                    already_set.append((r, c))
                    if r not in filled_rows:
                        filled_rows.append(r)
                    if c not in filled_cols:
                        filled_cols.append(c)
                    sx = r // 3
                    sy = c // 3
                    box = (sx, sy)
                    if box not in filled_boxes:
                        filled_boxes.append(box)
        for r, c in already_set:
            valid_moves[r, c, v] = 0
        for sx, sy in filled_boxes:
            for x in range(0, 3):
                for y in range(0, 3):
                    r = sx * 3 + x
                    c = sy * 3 + y
                    valid_moves[r, c, v] = 0
        for r in range(0, 9):
            for c in range(0, 9):
                if r in filled_rows:
                    valid_moves[r, c, v] = 0
                for c in filled_cols:
                    valid_moves[r, c, v] = 0
    return valid_moves

data = load_file('s10a.txt')
grid = parse_grid(data)
display(grid)

moves = get_valid_moves(grid)
print(moves[:, :, 0])