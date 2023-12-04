import os

sum = 0
f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()

for line in input_data:
    line = line.split(" | ")
    winning = line[0].split(": ")[1].split()
    mine = line[1].split()

    found = False
    points = 0
    for n in mine:
        for w in winning:
            if n == w:
                if not found:
                    points += 1
                    found = True
                else:
                    points *= 2
    sum += points

print(sum)
f.close()
