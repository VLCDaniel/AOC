import os
from itertools import pairwise

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


# we need the points in order for the Shoelace formula
def get_border():	
	visited = {}
	visited[start_pos] = True
	
	# go in one direction so we don't do bfs
	directions = get_connected_dirs(start_pos)
	dir = directions[0]
	next_pos = (start_pos[0] + dir[0], start_pos[1] + dir[1])
	Q = [next_pos]
	
	while Q:
		pos = Q.pop()
		visited[pos] = True
		
		directions = get_connected_dirs(pos)
		for dir in directions:
			next_pos = (pos[0] + dir[0], pos[1] + dir[1])
			if next_pos not in visited:
				Q.append(next_pos)
	return list(visited.keys())


start_pos = get_start_pos()
assert start_pos != None, "Couldn't find starting position"
# print("start pos: ", start_pos)

# get S type
s_type = get_start_type(start_pos)
# print("Start type: ", s_type)
A[start_pos[0]][start_pos[1]] = s_type


# part1 - dfs
points = get_border()
border_length = len(points)
print(border_length // 2)

# part2 - Shoelace and Pick's theorem
# Shoelace - triangle formula
# Area = 1/2 * (x1y2 - x2y1 + x2y3 - x3y2 + ... + xny1 - x1yn)
points.append(points[0])
area = abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in pairwise(points)) // 2)

# Pick's theorem
# Area = i + b/2 - 1
# i = nr of interior points; b = nr of border points
# i = Area + 1 - b/2
print(area + 1 - border_length // 2)
