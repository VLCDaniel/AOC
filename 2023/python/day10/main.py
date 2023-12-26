import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()
f.close()

Dirs = {
	"U": (-1, 0),
	"D": (1, 0),
	"L": (0, -1),
	"R": (0, 1)
}

Connections = {
	"U": "|7F",
	"D": "|LJ",
	"L": "-LF",
	"R": "-J7"
}

A = [[c for c in line] for line in input_data]
R = len(A)
C = len(A[0])
start_pos = None
visited = set()


def get_start_pos():
	for i, line in enumerate(A):
		for j, c in enumerate(line):
			if c == 'S':
				return (i, j)


def legit_pos(pos):
	return 0 <= pos[0] < R and 0 <= pos[1] < C


def get_start_type(start_pos):
	connected = ""
	for d, dir in Dirs.items():
		next_pos = (start_pos[0] + dir[0], start_pos[1] + dir[1])
		if not legit_pos(next_pos):
			continue
		ch = A[next_pos[0]][next_pos[1]]
		if ch in Connections[d]:
			connected += d
	
	conn_type = None
	match connected:
		case "UD": conn_type = '|'
		case "UL": conn_type = 'J'
		case "UR": conn_type = 'L'
		case "DL": conn_type = '7'
		case "DR": conn_type = 'F'
		case "LR": conn_type = '-'
		case _: assert False, "Starting position not connected"
	assert conn_type != None, "Couldn't find the pipe type of the starting position"
	return conn_type


def get_connected_dirs(pos):
	ch = A[pos[0]][pos[1]]
	dirs = None
	match ch:
		case '|': dirs = "UD"
		case 'J': dirs = "UL"
		case 'L': dirs = "UR"
		case '7': dirs = "DL"
		case 'F': dirs = "DR"
		case '-': dirs = "LR"
		case _: assert False, "Character not found"
	assert dirs != None, "Directions not found"
	return (Dirs[dirs[0]], Dirs[dirs[1]])


# part1 - BFS
def part1():
	length = 0
	Q = [start_pos]
	while Q:
		pos = Q.pop(0)
		visited.add(pos)
		length += 1
		
		directions = get_connected_dirs(pos)
		for dir in directions:
			next_pos = (pos[0] + dir[0], pos[1] + dir[1])
			if next_pos not in visited:
				Q.append(next_pos)
	return length // 2


# part2 - ray cast -> odd number of intersections means point is in interior and even number - outside
# Imagine the ray is being cast left to right, from the top of the tile and not from the center of it
#	  |		|
#	F-J		L-7
#	|		  |
# In this case, the ray would intersect J,L and not F,7 (since L,J are connected above)
# You can also think the ray is cast from the bottom part of the tile, intersecting F,7 since they're connected bellow
def part2():
	enclosed = 0
	for i in range(R):
		inside = False
		for j in range(C):
			if (i, j) in visited:
				if A[i][j] in "|JL": # |F7 works the same
					inside = not inside
			else:
				enclosed += inside
	return enclosed

# My personal demonstration :)
# Casting from left to right -> Taking '|' in consideration by default
# If we don't count corners, the dots bellow aren't considered.
# Row
# 1)    S----------------7
# 2)    |	    	 	 |
# 3)  F-J................|
# 4)  |			 		 |
# 5)  L-7.......F7.......|
# 6)    |	    ||		 |
# 7)    L-------JL-------J

# The question remains: Which corners should we consider? The above example tells us:
#	- We can't consider all 4 corners, F7LJ (it would result in 2 intersections for each dot, which is an even number, and they would still be considered outside)
#	- We can't consider 3 corners (one row of dots would be considered inside and the other row outside for every possibility)

# So, we have to consider at least 2 corners, but:
# 	- We can't consider (L7) or (FJ) since it would result in 2 intersections for all dots
#	- We can't consider (LF) since the second half of row 5) would be considered outside
#	- We can't consider (J7) since any point on the first row after the 7 would be considered inside
# So, we can only consider: (LJ) or (F7) which gives us the correct answer


start_pos = get_start_pos()
assert start_pos != None, "Couldn't find starting position"
# print("start pos: ", start_pos)

# get S type
s_type = get_start_type(start_pos)
# print("Start type: ", s_type)
A[start_pos[0]][start_pos[1]] = s_type

length = part1()
print(length)
print(part2())
