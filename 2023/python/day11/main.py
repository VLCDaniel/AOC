import os
from itertools import combinations

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()
f.close()

A = [[c for c in line] for line in input_data]
R = len(A)
C = len(A[0])

EMPTY_ROWS = []
for i, line in enumerate(A):
    if '#' not in line:
        EMPTY_ROWS.append(i)

EMPTY_COLUMNS = []
for c in range(C):
    empty_col = True
    for r in range(R):
        if A[r][c] == '#':
            empty_col = False
            break
    if empty_col:
        EMPTY_COLUMNS.append(c)

GALAXIES = []
for r in range(R):
    for c in range(C):
        if A[r][c] == '#':
            GALAXIES.append((r, c))


for expansion_factor in (1, 10 ** 6 - 1):
    sum = 0
    for (r1, c1), (r2, c2) in combinations(GALAXIES, 2):
        dist = abs(r1 - r2) + abs(c1 - c2)
        for er in EMPTY_ROWS:
            if min(r1, r2) <= er <= max(r1, r2):
                dist += expansion_factor
        for ec in EMPTY_COLUMNS:
            if min(c1, c2) <= ec <= max(c1, c2):
                dist += expansion_factor
        sum += dist

    print(sum)
