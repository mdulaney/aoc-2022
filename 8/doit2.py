#!/usr/bin/env python3

import numpy as np
import operator
import sys

from pprint import pprint
import itertools

f = sys.argv[1]

grid = []
with open(f, 'r') as inf:
    for l in inf.readlines():
        grid.append(list(map(lambda x : int(x), l[:-1])))

grid = np.array(grid)

maxxes = []
width = len(grid)
height = len(grid)
for (row,col) in itertools.product(range(height), range(width)):
    maxm = row * col * (height - 1 - row) * (width - 1 - col)
    print(f'row={row} col={col} maxm={maxm}')
    maxxes.append((row, col, maxm))

ordered = sorted(maxxes, key=operator.itemgetter(2))[::-1]

print('')
print('calculating best score')

best_max = -1
for row, col, maxm in ordered:

    if maxm < best_max:
        break

    vectors = [
        grid[row,col+1:],
        grid[row,:col][::-1],
        grid[:row,col][::-1],
        grid[row+1:,col],
    ]    

    newmaxm = 1
    print(f'row={row} col={col}', end='')
    for vec in vectors:
        curmax = 0
        for item in vec:
            if item < grid[row][col]:
                curmax += 1
            elif item >= grid[row][col]:
                curmax += 1
                break

        print(f' {curmax}({len(vec)})', end='')
        newmaxm *= curmax
    print('')

    if newmaxm > best_max:
        best_max = newmaxm

print(f'part2: {best_max}')
