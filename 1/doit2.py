#!/usr/bin/env python3

import sys

totals = []
current = 0
with open(sys.argv[1], 'r') as inf:
    for l in inf.readlines():
        l = l.strip()
        if l == '':
            totals.append(current)
            current = 0 
            continue

        current += int(l)

print(sum(sorted(totals)[-3:]))
