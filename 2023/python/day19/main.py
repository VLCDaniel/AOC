import os
from collections import defaultdict
import copy

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read()
f.close()

workflows, parts = input_data.split('\n\n')
workflows = workflows.splitlines()
parts = parts.splitlines()

WORKFLOW = defaultdict(str)
for wf in workflows:
    key, rules = wf.split('{')
    rules = rules[:-1]
    rules = rules.split(',')
    n = len(rules)
    
    R = []
    for i in range(n - 1):
        curr_rule = rules[i]
        rating, next = curr_rule[2:].split(':')
        rating = int(rating)
        rule = (curr_rule[0], curr_rule[1], rating, next)
        R.append(rule)
    R.append(rules[-1])
    WORKFLOW[key] = R


# part 1
def apply_cond(target, sign, value):
    if sign == '<':
        return target < value
    else:
        return target > value


def get_rating(D, part2 = False):
    if part2:
        rating = 1
        for left, right in D.values():
            rating *= (right - left + 1)
    else:
        rating = 0
        for values in D.values():
            rating += values

    return rating
                    

sum = 0
for part in parts:
    d = defaultdict(int)
    part = part[1:-1]
    part = part.split(',')
    for p in part:
        key, value = p.split('=')
        value = int(value)
        d[key] = value

    current_key = 'in'
    Q = ['in']
    while Q:
        current_key = Q.pop(0)
        rules = WORKFLOW[current_key]
        for rule in rules:
            if isinstance(rule, str): # last state
                if rule == 'A':
                    sum += get_rating(d)
                elif rule != 'R':
                    Q.append(rule)
                break
            
            key, sign, val, next_key = rule
            target = d[key]
            if apply_cond(target, sign, val):
                if next_key == 'A':
                    sum += get_rating(d)
                elif rule != 'R':
                    Q.append(next_key)
                break

print(sum)


# part 2
def apply_cond(D, sign, key, val):
    if sign == '<':
        if D[key][1] >= val and D[key][0] <= val - 1:
            D[key][1] = val - 1
            return True
    else:
        if D[key][0] <= val and val + 1 <= D[key][1]:
            D[key][0] = val + 1
            return True
    return False


D = {
    "x": [1, 4000],
    "m": [1, 4000],
    "a": [1, 4000],
    "s": [1, 4000]
}
Q = [('in', D)]
sum = 0
while Q:
    current_key, D = Q.pop(0)
    rules = WORKFLOW[current_key]

    updated_D = None
    for rule in rules:
        if isinstance(rule, str): # last state
            if rule == 'A':
                sum += get_rating(D, True)
            elif rule != 'R':
                Q.append((rule, D))
            break
        
        key, sign, val, next_state = rule
        updated_D = copy.deepcopy(D)
        if apply_cond(updated_D, sign, key, val):
            if next_state == 'A':
                sum += get_rating(updated_D, True)
            elif next_state != 'R':
                Q.append((next_state, updated_D))
        
        # apply reversed cond
        sign = '>' if sign == '<' else '<'
        val = val + 1 if sign == '<' else val - 1 # treat equality
        if apply_cond(D, sign, key, val):
            continue
        else:
            break

print(sum)
