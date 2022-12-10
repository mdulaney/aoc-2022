#!/usr/bin/env python3

import sys

def m(c):
    c = ord(c)
    if c > ord('a'):
        c = (c - ord('a')) + 1
    else:
        c = (c - ord('A')) + 27

    return c

total = 0
with open(sys.argv[1], 'r') as inf:
    lines = inf.readlines()
    for idx in range(0, len(lines), 3):
        ll = list(map(lambda x : set(x.strip()), lines[idx:idx+3]))
        c = list(ll[0] & ll[1] & ll[2])[0]
        print(c)
        c = m(c)
        total += c

print(total)
