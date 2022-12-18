#!/usr/bin/env python3

import sys


f = sys.argv[1]

with open(f, 'r') as inf:
    lines = inf.readlines()


monkeys = []
for idx in range(0, len(lines), 7):
    div = int(lines[idx+3].split()[-1])
    op = lines[idx+2].split('=')[1].strip()
    monkeys.append({
        'items' : list(map(lambda x : int(x), lines[idx+1].split(':')[1].strip().split(','))),
        'op'    : op,
        'test'  : div,
        True    : int(lines[idx+4].split()[-1]),
        False   : int(lines[idx+5].split()[-1]),
        'total' : 0
    })


for i in range(20):
    for m in monkeys:
        for item in m['items']:
            new_item = int(eval(m['op'], {'old':item})/3)
            throws = m[new_item % m['test'] == 0]
            monkeys[throws]['items'].append(new_item)
            m['total'] += 1
        m['items'] = []

results = sorted(map(lambda x : x['total'], monkeys))

print(results[-2] * results[-1])
        
