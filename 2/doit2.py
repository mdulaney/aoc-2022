#!/usr/bin/env python3

import sys

op2d = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6,
}

def outcome(op1, op2):
    print(op1, op2)
    op1 = ord(op1) - ord('A')

    if op2 == 'X':
        return ((op1 - 1) % 3) + 1
    elif op2 == 'Y':
        return op1 + 1

    return ((op1 + 1) % 3) + 1

total = 0

try:
    with open(sys.argv[1], 'r') as inf:
        for l in inf.readlines():
            op1, op2 = l.strip().split()
            total += outcome(op1, op2) + op2d[op2]
except:
    lines = 'A Y\nB X\nC Z'
    for l in lines.split('\n'):
        op1, op2 = l.strip().split()
        total += outcome(op1, op2) + op2d[op2]

print(total)
