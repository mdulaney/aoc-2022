#!/usr/bin/env python3

import sys

f = sys.argv[1]

with open(f, 'r') as inf:
    data = inf.read()
    for i in range(0, len(data)):
        if len(set(data[i:i+4])) == 4:
            print(data[i:i+4])
            print(i+4)
            sys.exit(0)
