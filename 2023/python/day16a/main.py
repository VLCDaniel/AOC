import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()
f.close()

A = [[x for x in line] for line in input_data]
R = len(A)
C = len(A[0])

Dir = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}


def get_next_dirs(pos, dir):
    ch = A[pos[0]][pos[1]]
    next_dirs = None

    if ch == '.':
        next_dirs = [dir]
    elif ch == '|':
        next_dirs = {
            "N": ["N"],
            "S": ["S"],
            "W": ["N", "S"],
            "E": ["N", "S"]
        }[dir]
    elif ch == '-':
        next_dirs = {
            "N": ["E", "W"],
            "S": ["E", "W"],
            "E": ["E"],
            "W": ["W"]
        }[dir]
    elif ch == '\\':
        next_dirs = {
            "N": ["W"],
            "S": ["E"],
            "E": ["S"],
            "W": ["N"]
        }[dir]
    elif ch == '/':
        next_dirs = {
            "N": ["E"],
            "S": ["W"],
            "E": ["N"],
            "W": ["S"]
        }[dir]
    else:
        assert False, "Unexpected char in input"
    assert next_dirs != None, "Couldn't get next directions"
    return next_dirs


def get_next_locations(curr_pos, curr_dir):
    next_locations = []
    next_dirs = get_next_dirs(curr_pos, curr_dir)

    for dir in next_dirs:
        next_pos = (curr_pos[0] + Dir[dir][0], curr_pos[1] + Dir[dir][1])
        if next_pos[0] >= 0 and next_pos[0] < R and next_pos[1] >= 0 and next_pos[1] < C:
            next_locations.append((next_pos, dir))
    return next_locations



VisitedPos = set()
VisitedLoc = set()

Q = [((0, 0), "E")]
while len(Q) != 0:
    curr_location = Q.pop(0)
    curr_pos, curr_dir = curr_location
    VisitedPos.add(curr_pos)
 
    next_locations = get_next_locations(curr_pos, curr_dir)
    if len(next_locations) == 0 or curr_location in VisitedLoc:
        continue
    VisitedLoc.add(curr_location)

    for location in next_locations:
        Q.append(location)


energized_tiles = [['.' for x in range(C)] for i in range(R)]

for pos in VisitedPos:
    energized_tiles[pos[0]][pos[1]] = '#'

sum = 0
for row in energized_tiles:
    for tile in row:
        if tile == '#':
            sum += 1

print(sum)
