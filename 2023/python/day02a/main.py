import os

d = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")

input_data = f.read().splitlines()
sum = 0
for line in input_data:
    game, rounds = line.split(": ")
    id = int(game.split(' ')[1])

    rounds = rounds.split("; ")
    cont = False
    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            cube = cube.split(' ')
            color = cube[1]
            number = int(cube[0])
            if d[color] < number:
                cont = True
                break
    if cont:
        continue
    else:
        sum += id

print(sum)

f.close()
