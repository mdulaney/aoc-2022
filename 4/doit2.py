#!/usr/bin/env python3

import sys

def make_range_set(tok):
    s1_start, s1_end = tok.split('-')
    return set(range(int(s1_start), int(s1_end)+1))

f = sys.argv[1]

count = 0
with open(f, 'r') as inf:
    for l in inf.readlines():
        s1, s2 = l.split(',')
        r1 = make_range_set(s1)
        r2 = make_range_set(s2)

        print(r1, r2)
        if len(r1 & r2) > 0:
            count += 1
print(count)
