import os
from collections import defaultdict

sum = 0
f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()
d = defaultdict(int)

for pos, line in enumerate(input_data):
    line = line.split(" | ")
    winning = line[0].split(": ")[1].split()
    mine = line[1].split()

    d[pos] += 1
    matches = 0
    for n in mine:
        for w in winning:
            if n == w:
                matches += 1
    for j in range(d[pos]):
        for i in range(matches):
            d[pos + i + 1] += 1

for key, value in d.items():
    sum+= value

print(sum)
f.close()
