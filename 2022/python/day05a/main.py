import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")

input_data = f.read()
input_data = input_data.split("\n\n")

initial_stacks = input_data[0].split('\n')
size = len(initial_stacks)
M = [[c for c in line] for line in initial_stacks[0:size - 1]]
size = len(M[0])
stack_size = (len(M[0]) + 1) // 4 # 3 chars + space
stacks = []
for i in range(stack_size):
    stacks.append([])

for r in range(len(M)):
    for c in range(1, size, 4):
        if M[r][c] != ' ':
            stacks[c // 4].insert(0, M[r][c])

moves = input_data[1].split('\n')
for move in moves:
    move = move.split()
    from_stack = int(move[3]) - 1
    move_count = int(move[1])
    to_stack = int(move[5]) - 1

    for i in range(move_count):
        value = stacks[from_stack].pop()
        stacks[to_stack].append(value)

message = ""
for stack in stacks:
    message += stack[-1]
print(message)
f.close()
