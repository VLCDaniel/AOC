import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().splitlines()

def get_part_numbers_sum(top_line, target_line, bottom_line):
    symbol_positions = []
    if top_line != None:
        for i in range(0, len(top_line)):
            if top_line[i]!= '.' and not top_line[i].isdigit():
                symbol_positions.append(i)
    if bottom_line != None:
        for i in range(0, len(bottom_line)):
            if bottom_line[i]!= '.' and not bottom_line[i].isdigit():
                symbol_positions.append(i)
    symbol_positions = set(symbol_positions)

    i = 0
    sum = 0
    while i < len(target_line):
        if target_line[i].isdigit():
            starting_pos = i
            while i < len(target_line) and target_line[i].isdigit():
                i += 1
            ending_pos = i

            # Symbols next to the number
            if starting_pos > 0 and target_line[starting_pos - 1] != '.' or ending_pos < len(target_line) and target_line[ending_pos] != '.':
                sum += int(target_line[starting_pos:ending_pos])
            # Symbols above and below the number
            for p in symbol_positions: 
                if p >= starting_pos - 1 and p <= ending_pos:
                    sum += int(target_line[starting_pos:ending_pos])
                    break
        else:
            i += 1
    
    return sum


first_line = input_data[0]
second_line = input_data[1]
sum = get_part_numbers_sum(None, first_line, second_line)

for l in range(1, len(input_data) - 1):
    top_line = input_data[l - 1]
    mid_line = input_data[l]
    bottom_line = input_data[l + 1]

    sum += get_part_numbers_sum(top_line, mid_line, bottom_line)

last_line = input_data[-1]
penult_line = input_data[-2]
sum += get_part_numbers_sum(penult_line, last_line, None)

print(sum)
f.close()
