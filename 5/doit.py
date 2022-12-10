#!/usr/bin/env python3

import re
import sys

f = sys.argv[1]

lines = open(f, 'r').readlines()

stacks = {}
idx = 0
while True:
    line = lines[idx]
    idx += 1
    if line.strip() == '':
        break

    stack_idx = 1
    for chr_idx in range(0, len(line), 4):
        m = re.match('\[(?P<v>[A-Z])\]', line[chr_idx:chr_idx+4])
        if m != None:
            print(m.group('v'), end='')
            stacks[stack_idx] = stacks.get(stack_idx, [])
            stacks[stack_idx].append(m.group('v'))

        stack_idx += 1

    print('')

from pprint import pprint
pprint(stacks)
sys.exit(1)
for l in lines[idx:]:
    m = re.match('move (?P<move>[\d]{1,2}) from (?P<from>[\d]) to (?P<to>[\d])', l)
    print(l)
    print(f'  {m.group("move")}')
    print(f'  {m.group("from")}')
    print(f'  {m.group("to")}')

