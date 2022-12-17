#!/usr/bin/env python3

import re
import sys

def range_rel_pos(start, count):
    nxt = start + 1
    return range(nxt, nxt+count)

def range_rel_neg(start, count):
    nxt = start - 1
    return range(nxt, nxt-count, -1)

f = sys.argv[1]

last_dir = None
rope = [(0,0)] * 10
head_positions = []
tails_visited = set([(0,0),])

print(rope)
with open(f, 'r') as inf:
    for l in inf.readlines():
        m = re.match('(?P<direction>[A-Z]) (?P<count>[\d]+)', l)
        direction = m.group('direction')
        count = int(m.group('count'))

        if direction == 'R':
            transform = (0,1)
        elif direction == 'L':
            transform = (0,-1)
        elif direction == 'D':
            transform = (-1,0)
        elif direction == 'U':
            transform = (1,0)


        for _ in range(count):
            rope[0] = (transform[0] + rope[0][0], transform[1] + rope[0][1])
            rope_prev = rope[0]

            for i in range(1, len(rope)):
                row_delta = rope_prev[0] - rope[i][0]
                col_delta = rope_prev[1] - rope[i][1]

                if abs(row_delta) == 2 and abs(col_delta) == 2:
                    row_delta = 1 if row_delta > 0 else -1
                    col_delta = 1 if col_delta > 0 else -1
                elif abs(row_delta) == 2:
                    row_delta = 1 if row_delta > 0 else -1
                elif abs(col_delta) == 2:
                    col_delta = 1 if col_delta > 0 else -1
                else:
                    row_delta = 0
                    col_delta = 0

                rope[i] = (rope[i][0] + row_delta, rope[i][1] + col_delta)
                rope_prev = rope[i]

            #print(direction, count, rope)
            tails_visited.add(rope[-1])

print(len(tails_visited))
