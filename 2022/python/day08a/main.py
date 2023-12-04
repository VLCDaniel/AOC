import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()
sum = 0
line_size = len(input_data[0])
border_trees = 2 * len(input_data) - 4 + 2 * line_size



M = [[c for c in line] for line in input_data]
R = len(M)
C = len(M[0])
sum = border_trees
sum = 2 * R + 2 * C - 4

def check_visibility_rec(line, col, el, dir):    
    next_line = line + dir[0]
    next_col = col + dir[1]
    if next_line == 0 or next_line == R - 1 or next_col == 0 or next_col == C - 1:
        return not M[next_line][next_col] >= el
    if M[next_line][next_col] >= el:
        return False
    return check_visibility_rec(next_line, next_col, el, dir)


def check_visibility(line, col):
    el = M[line][col]

    # check up
    if check_visibility_rec(line, col, el, [-1, 0]):
        return True

    # check down
    if check_visibility_rec(line, col, el, [1, 0]):
        return True

    # check left
    if check_visibility_rec(line, col, el, [0, -1]):
        return True

    # check right
    if check_visibility_rec(line, col, el, [0, 1]):
        return True
    return False


for i in range(1, R - 1):
    for j in range(1, C - 1):
        if check_visibility(i, j):
            sum += 1

print(sum)
f.close()
