import os

sum = 0
f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()

for line in input_data:
    occurences = []
    for pos, c in enumerate(line):
        initial_size = len(occurences)
        occurences.append(c)
        set_size = len(set(occurences))
        if set_size == initial_size:
            while occurences[0] != c:
                occurences.pop(0)
            occurences.pop(0)
        elif set_size == 14:
            sum += pos + 1
            break

print(sum)
f.close()
