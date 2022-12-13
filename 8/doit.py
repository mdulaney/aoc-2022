#!/usr/bin/env python3

import numpy as np
import sys

from pprint import pprint

f = sys.argv[1]

grid = []
with open(f, 'r') as inf:
    for l in inf.readlines():
        grid.append(list(map(lambda x : int(x), l[:-1])))

grid = np.array(grid)
visible_trees = set()

for row_idx in range(len(grid)):
    row = grid[row_idx]

    # forward rows, forward columns
    minm = -1
    print(row)
    for c_idx in range(len(row)):
        c = row[c_idx]
        if c > minm:
            print(f'-> {c}')
            minm = c
            visible_trees.add((row_idx, c_idx))
    
    # forward rows, backward columns
    minm = -1
    print(row[::-1])
    for c_idx in range(len(row)-1, -1, -1):
        c = row[c_idx]
        if c > minm:
            print(f'-> {c}')
            minm = c
            visible_trees.add((row_idx, c_idx))

grid2 = grid.transpose()
pprint(grid)
print('xxxx')
pprint(grid2)


for row_idx in range(len(grid2)-1, -1, -1):
    print('xxx', row_idx)
    row = grid2[row_idx]

    # forward rows, forward columns
    minm = -1
    print(row)
    for c_idx in range(len(row)):
        c = row[c_idx]
        if c > minm:
            print(f'-> {c}')
            minm = c
            visible_trees.add((c_idx, row_idx))
    
    # forward rows, backward columns
    minm = -1
    print(row[::-1])
    for c_idx in range(len(row)-1, -1, -1):
        c = row[c_idx]
        if c > minm:
            print(f'-> {c}')
            minm = c
            visible_trees.add((c_idx, row_idx))

print(f'part1: {len(visible_trees)}')

