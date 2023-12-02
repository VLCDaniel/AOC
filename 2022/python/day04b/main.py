import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")

input_data = f.read().splitlines()
sum = 0
for line in input_data:
    line = line.split(',')
    first_range = line[0].split('-')
    second_range = line[1].split('-')
    
    a, b = int(first_range[0]), int(first_range[1])
    c, d = int(second_range[0]), int(second_range[1])
    if c >= a and c <= b or \
       d >= a and d <= b or \
       a >= c and a <= d or \
       b >= c and b <= d:
        sum += 1


print(sum)

f.close()
