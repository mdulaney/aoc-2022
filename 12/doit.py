#!/usr/bin/env python3

import itertools
import sys

import functools

grid = []
visited = set()

@functools.cache
def traverse(prev, s):
    global visited

    if grid[s[0]][s[1]] == 'E':
        return 0

    visited.add(s)

    adj_row = [r for r in [s[0]-1, s[0], s[0]+1] if r in range(len(grid))]
    adj_col = [c for c in [s[1]-1, s[1], s[1]+1] if c in range(len(grid[0]))]

    adj = itertools.product(adj_row, adj_col)
    adj = [x for x in adj if x not in visited ]
    adj = [x for x in adj if x[0] == s[0] or x[1] == s[1]]

    v2 = grid[s[0]][s[1]]
    if v2 == 'S':
        v2 = 'a'

    heights = [len(grid)*len(grid[0])]
    for a in adj:
        v1 = grid[a[0]][a[1]]

        if v1 == 'E':
            v1 = 'z'

        if ord(v1) <= ord(v2)+1:
            heights.append(traverse(a) + 1)

    visited.remove(s)
    return min(heights)

f = open(sys.argv[1], 'r')

row = 0
for l in f.readlines():
    print(l.strip())
    grid.append(l.strip())
    col = l.find('S')
    if col >= 0:
        start = (row, col)
    row += 1

sys.setrecursionlimit(max(sys.getrecursionlimit(), len(grid)*len(grid[0])))
print(f'start={start}')
print(traverse(start, start))
print('')

