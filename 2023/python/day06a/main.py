import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read().split('\n')

timings = [int(x) for x in input_data[0].split()[1:]]
distances = [int(x) for x in input_data[1].split()[1:]]

def get_distance(wait_time, total_time):
    # speed * remaining_timing
    return wait_time * (total_time - wait_time)

def get_total_winning_ways(time, target_distance):
    # Binary search on first half, since it's symmetrical
    # Searching for first position the distance is greater than the target distance
    initial_mid = time // 2
    left, right = 0, initial_mid
    while left < right:
        mid = (left + right) // 2
        distance = get_distance(mid, time)
        if distance > target_distance:
            right = mid
        else:
            left = mid + 1
    
    starting_index = left
    ending_index = initial_mid + initial_mid - left
    if time % 2 == 1: # if the time is odd, we add 1 more index, since we have 2 identical elements in the middle
        ending_index += 1
    return ending_index - starting_index + 1

sum = 1
for i in range(len(timings)):
    time, distance = timings[i], distances[i]
    winning_ways = get_total_winning_ways(time, distance)
    sum *= winning_ways

print(sum)
