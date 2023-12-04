import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()

M = [[c for c in line] for line in input_data]
R = len(M)
C = len(M[0])


def check_visibility_rec(line, col, el, dir):    
    next_line = line + dir[0]
    next_col = col + dir[1]
    if next_line == 0 or next_line == R - 1 or next_col == 0 or next_col == C - 1:
        return 1
    if M[next_line][next_col] >= el:
        return 1
    return 1 + check_visibility_rec(next_line, next_col, el, dir)


def check_visibility(line, col):
    el = M[line][col]
    visibility = 1

    # check up
    visibility *= check_visibility_rec(line, col, el, [-1, 0])

    # check down
    visibility *= check_visibility_rec(line, col, el, [1, 0])

    # check left
    visibility *= check_visibility_rec(line, col, el, [0, -1])

    # check right
    visibility *= check_visibility_rec(line, col, el, [0, 1])

    return visibility


max = 0
for i in range(1, R - 1):
    for j in range(1, C - 1):
        visibility = check_visibility(i, j)
        max = max if max > visibility else visibility

print(max)
f.close()
