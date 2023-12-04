import os
from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)
f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()

for line in input_data:
    match line.split():
        case '$', 'cd', '/': curr = ['/']
        case '$', 'cd', '..': curr.pop()
        case '$', 'cd', x: curr.append(x + '/')
        case '$', 'ls': pass
        case 'dir', _: pass
        case size, _:
            for p in accumulate(curr):
                dirs[p] += int(size)

print(sum(s for s in dirs.values() if s <= 100_000))
f.close()
