import os
from collections import defaultdict
import math

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().split("\n\n")
directions = input_data[0]
f.close()

nodes = defaultdict(str)
for line in input_data[1].split('\n'):
    line = line.split()
    node = line[0]
    left = line[2][1:-1]
    right = line[3][:-1]
    nodes[node] = (left, right)

steps = 0
i = 0
steps = 1
for k in nodes:
    if k[-1] == 'A':
        current_node = k
        i = 0
        step = 0
        while current_node[-1] != 'Z':
            if directions[i] == 'L':
                current_node = nodes[current_node][0]
            elif directions[i] == 'R':
                current_node = nodes[current_node][1]
            step += 1
            i = (i + 1) % len(directions)
        steps = math.lcm(steps, step)
print(steps)
