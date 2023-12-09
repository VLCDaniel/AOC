import os
from collections import defaultdict

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
current_node = 'AAA'

while current_node != 'ZZZ':        
    if directions[i] == 'L':
        current_node = nodes[current_node][0]
    elif directions[i] == 'R':
        current_node = nodes[current_node][1]
    steps += 1
    i = (i + 1) % len(directions)

print(steps)
