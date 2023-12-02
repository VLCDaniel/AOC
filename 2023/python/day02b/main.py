import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")

input_data = f.read().splitlines()
sum = 0
for line in input_data:
    d = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

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
                d[color] = number

    sum+= d["red"] * d["blue"] * d["green"]

print(sum)

f.close()
