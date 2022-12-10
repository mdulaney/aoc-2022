#!/usr/bin/env python3

import sys

highest = 0
current = 0
with open(sys.argv[1], 'r') as inf:
    for l in inf.readlines():
        l = l.strip()
        if l == '':
            if current > highest:
                highest = current

            current = 0
            continue

        current += int(l)

print(highest)
