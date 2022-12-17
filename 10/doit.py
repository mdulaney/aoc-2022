#!/usr/bin/env python3

import sys

f = sys.argv[1]

with open(f, 'r') as inf:
    lines = inf.readlines()
    
reg_values = [1]
cycle = 1
for l in lines:
    toks = l.split(' ')
    if toks[0] == 'addx':
        oper = int(toks[1])
        reg_values.append(reg_values[cycle-1])
        reg_values.append(reg_values[cycle] + oper)
        cycle += 2
    else:
        reg_values.append(reg_values[cycle-1])
        cycle += 1 

acc = 0
for i in range(20, len(reg_values), 40):
    acc += i * reg_values[i-1]


print('')
print(f'part1: {acc}')
print('')



print(reg_values)
sprite_pos = reg_values[1]
sprite_pos = range(sprite_pos-1, sprite_pos+2)
for i in range(1, len(reg_values)):
    
    if (i-1)%40 in sprite_pos:
        print('#', end='')
    else:
        print('.', end='')

    if i % 40 == 0:
        print('')

    sprite_pos = reg_values[i]
    sprite_pos = range(sprite_pos-1, sprite_pos+2)
