import os
from collections import defaultdict

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()
d = defaultdict(list)

def get_gear_part_numbers(top_line, target_line, bottom_line, line_number):
    gear_positions = []
    if top_line != None:
        for i in range(0, len(top_line)):
            if top_line[i] == '*':
                gear_positions.append(i)
    if bottom_line != None:
        for i in range(0, len(bottom_line)):
            if bottom_line[i] == '*':
                gear_positions.append(i)
    gear_positions = set(gear_positions)

    i = 0
    while i < len(target_line):
        if target_line[i].isdigit():
            starting_pos = i
            while i < len(target_line) and target_line[i].isdigit():
                i += 1
            ending_pos = i

            # Gears next to the number
            if starting_pos > 0 and target_line[starting_pos - 1] == '*':
                d[(line_number, starting_pos - 1)].append(int(target_line[starting_pos:ending_pos]))
            if ending_pos < len(target_line) and target_line[ending_pos] == '*':
                d[(line_number, ending_pos)].append(int(target_line[starting_pos:ending_pos]))
            # Gears above and below the number
            for g in gear_positions: 
                if g >= starting_pos - 1 and g <= ending_pos:
                    if top_line != None and top_line[g] == '*':
                       d[(line_number - 1, g)].append(int(target_line[starting_pos:ending_pos]))
                    if bottom_line!= None and bottom_line[g] == '*':
                       d[(line_number + 1, g)].append(int(target_line[starting_pos:ending_pos]))
        else:
            i += 1


first_line = input_data[0]
second_line = input_data[1]
get_gear_part_numbers(None, first_line, second_line, 0)

for l in range(1, len(input_data) - 1):
    top_line = input_data[l - 1]
    mid_line = input_data[l]
    bottom_line = input_data[l + 1]

    get_gear_part_numbers(top_line, mid_line, bottom_line, l)

last_line = input_data[-1]
penult_line = input_data[-2]
get_gear_part_numbers(penult_line, last_line, None, len(input_data) - 1)

sum = 0
for l in d.values():
    if len(l) == 2:
        sum += l[0] * l[1]
        # ratio = 1
        # for part in l:
        #     ratio *= part
        # sum += ratio

print(sum)

f.close()