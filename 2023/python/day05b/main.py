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

def apply_range_map(I, m):
  # Each mapping has disjunct intervals, so if a part of our target interval (the one with seeds) gets mapped, we can no longer look for it
  calculatedI = []
  for map in m:
    dst_range, src_range, size = map
    src_end = src_range + size

    # Below process can be optimised, but it makes the most sense to me as it is
    remainingI = []
    while I:
      (start, end) = I.pop()

      # outside target interval
      if src_end < start or src_range >= end:
        remainingI.append((start, end))

      # containing whole target interval
      if src_range <= start and src_end >= end:
        calculatedI.append((start + dst_range - src_range, end + dst_range - src_range))

      # containing start only
      if src_range <= start and src_end >= start and src_end < end:
        remainingI.append((src_end, end))
        calculatedI.append((start + dst_range - src_range, src_end + dst_range - src_range))

      # containing end only
      if src_range > start and src_range < end and src_end >= end:
        remainingI.append((start, src_range))
        calculatedI.append((dst_range, end + dst_range - src_range))

      # inside target interval
      if src_range > start and src_end < end:
        remainingI.append((start, src_range))
        remainingI.append((src_end, end))
        calculatedI.append((dst_range, src_end + dst_range - src_range))

    I = remainingI
    
  return I + calculatedI

# Horrible hack but who has time to learn how to use zip :)
S = []
i = 0
while i < len(seeds):
  S.append((seeds[i], seeds[i] + seeds[i + 1]))
  i += 2
seeds = S

S = []
for seed in seeds:
  seed = [seed]
  for map in mappings:
    seed = apply_range_map(seed, map)
  S.append(min(seed))

print(min(S)[0])