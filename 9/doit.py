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
head_pos = (0,0)
head_positions = []
tails_visited = set()

with open(f, 'r') as inf:
    for l in inf.readlines():
        m = re.match('(?P<direction>[A-Z]) (?P<count>[\d]+)', l)
        direction = m.group('direction')
        count = int(m.group('count'))

        if direction == 'R':
            range_vec = zip([head_pos[0]]*count, range_rel_pos(head_pos[1], count))
        elif direction == 'L':
            range_vec = zip([head_pos[0]]*count, range_rel_neg(head_pos[1], count))
        elif direction == 'D':
            range_vec = zip(range_rel_neg(head_pos[0], count), [head_pos[1]]*count)
        elif direction == 'U':
            range_vec = zip(range_rel_pos(head_pos[0], count), [head_pos[1]]*count)

        range_vec = list(range_vec)
        head_positions += range_vec
        head_pos = range_vec[-1]


tail = (0,0)
tails_visited.add(tail)
for i in range(0, len(head_positions)-1):
    head_cur = head_positions[i]
    head_next = head_positions[i+1]

    if abs(head_next[0] - tail[0]) > 1 or abs(head_next[1] - tail[1]) > 1:
        tail = head_cur
        tails_visited.add(tail)


print(head_positions)
print('')
print(len(tails_visited))
