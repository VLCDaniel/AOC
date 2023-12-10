import os
from collections import defaultdict

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()
f.close()

sum = 0
for line in input_data:
    d = defaultdict(int)
    d[0] = [int(x) for x in line.split()]

    i = 0
    while True:
        d[i + 1] = []
        all_zeroes = True
        for j in range(len(d[i]) - 1):
            elem = d[i][j + 1] - d[i][j]
            d[i + 1].append(elem)
            if elem!= 0:
                all_zeroes = False
        i += 1
        if all_zeroes:
            break

    d[i].insert(0, 0)
    i -= 1
    nr = 0
    while i >= 0:
        nr = d[i][0] - d[i + 1][0]
        d[i].insert(0, nr)
        i -= 1
    sum += nr
print(sum)