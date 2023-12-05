import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read()
f.close()

seeds, *input_data = input_data.split('\n\n')
seeds = [int(x) for x in seeds.split(':')[1].split()]
mappings = []

for lines in input_data:
    lines = lines.split('\n')
    map = []
    for line in lines[1:]:
        line = line.split()
        map.append([int(x) for x in line])
    mappings.append(map)

def apply_map(x, m):
    for map in m:
        dst_range, src_range, size = map
        if src_range <= x < src_range + size:
            return x + dst_range - src_range
    return x

S = []
for seed in seeds:
    for map in mappings:
        seed = apply_map(seed, map)
    S.append(seed)
print(min(S))
