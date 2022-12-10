#!/usr/bin/env python3

import sys

total = 0
with open(sys.argv[1], 'r') as inf:
    for l in inf.readlines():
        l = l.strip()
        mid = int(len(l) / 2)
        p1 = set(l[:mid])
        p2 = set(l[mid:])

        c = ord(list(p1 & p2)[0])
        if c > ord('a'):
            c = (c - ord('a')) + 1
        else:
            c = (c - ord('A')) + 27

        total += c

print(total)
