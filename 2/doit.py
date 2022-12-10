#!/usr/bin/env python3

import sys

op2d = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
}

def outcome(op1, op2):
    print(op1, op2)
    op1 = ord(op1) - ord('A')
    op2 = ord(op2) - ord('X')

    if op2 == op1:
        r = 3
    elif op1 == 0:
        if op2 == 2:
            r = 0
        else:
            r = 6
    elif op2 == 0:
        if op1 == 2:
            r = 6
        else:
            r = 0
    elif op2 > op1:
        r = 6
    else:
        r = 0

    print(' ', op1, op2, r)
    return r

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
