import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()
f.close()

visited = 0
A = [['.']]
C = len(A[0])
R = len(A)
head_pos = [0, 0]
tail_pos = [0, 0]

for line in input_data:
    line = line.split()
    line[1] = int(line[1])
    direction = None
    magnitude = None

    match line:
        case 'D', magnitude:
            direction = (1, 0)
        case 'U', magnitude:
            direction = (-1, 0)
        case 'L', magnitude:
            direction = (0, -1)
        case 'R', magnitude:
            direction = (0, 1)
        case _:
            assert False, "Invalid input!"
    assert direction != None and magnitude != None, "{next_pos} and {magnitude} shouldn't be None"

    next_pos = [head_pos[0] + direction[0] * magnitude, head_pos[1] + direction[1] * magnitude]

    # Make sure next position exists
    if next_pos[0] < 0: # up
        # rows needed
        rows = abs(next_pos[0])
        for i in range(rows):
            row = ['.'] * C
            A.insert(0, row)
            R += 1
            # shift existing positions accordingly
            head_pos[0] += 1
            next_pos[0] += 1
            tail_pos[0] += 1
    elif next_pos[0] >= R: # down
        # rows needed
        rows = next_pos[0] - R + 1
        for i in range(rows):
            row = ['.'] * C
            A.append(row)
            R += 1
    elif next_pos[1] < 0:
        # columns needed
        columns = abs(next_pos[1])
        for i in range(columns):
            for row in A:
                row.insert(0, '.')
            C += 1
            # shift existing positions accordingly
            head_pos[1] += 1
            next_pos[1] += 1
            tail_pos[1] += 1
    elif next_pos[1] >= C:
        # columns needed
        columns = next_pos[1] - C + 1
        for i in range(columns):
            for row in A:
                row.append('.')
            C += 1


    # Move towards destination
    while head_pos[0] != next_pos[0] or head_pos[1] != next_pos[1]:
        head_pos = [head_pos[0] + direction[0], head_pos[1] + direction[1]]
        hr, hc = head_pos[0], head_pos[1]
        tr, tc = tail_pos[0], tail_pos[1]
        
        # move tail if it's the case
        # tail on same row or same column as head
        if tr == hr and abs(hc - tc) > 1 or \
           tc == hc and abs(hr - tr) > 1:
            tail_pos = [tr + direction[0], tc + direction[1]]
        # tail and head 2 positions apart on a diagonal
        elif abs(hr - tr) > 1 or abs(hc - tc) > 1:
            tail_dir = [0, 0]
            if hr > tr:
                tail_dir[0] = 1
            else:
                tail_dir[0] = -1
            if hc > tc:
                tail_dir[1] = 1
            else:
                tail_dir[1] = -1
            tail_pos = [tr + tail_dir[0], tc + tail_dir[1]]
        
        A[tail_pos[0]][tail_pos[1]] = '#'

for line in A:
    for ch in line:
        if ch == '#':
            visited += 1

print(visited)
