#!/usr/bin/env python3

import os
import re
import sys

dirs = {}
dir_sizes = []

def finalize_dir_size(d, cwd=''):
    d['_size'] = d.get('_size', 0)

    for name, val in d.items():
        if name in ['_size', '_parent']:
            continue

        cwd = os.path.join(cwd, name)
        d['_size'] += finalize_dir_size(val, cwd)

    dir_sizes.append(d['_size'])
    return d['_size']

f = sys.argv[1]

with open(f, 'r') as inf:
    lines = inf.readlines()

    i = 0
    cwd = ''

    dcur = dirs
    for i in range(len(lines)):
        m = re.match('(\$ (?P<cd_cmd>[\w]+) (?P<param>[\w\/\.]+))|(\$ (?P<ls_cmd>[\w]+))|(dir (?P<dir>[\w+]))|((?P<size>[\d]+) (?P<file>[\w\.]+))', lines[i])

        if m.group('cd_cmd'):
            dest = m.group('param')
            if dest == '..':
                cwd = os.path.split(cwd)[0]
                dcur = dcur['_parent']
            else:
                parent = dcur

                try:
                    dcur = parent[dest]
                except KeyError:
                    parent[dest] = {}
                    dcur = parent[dest]
                dcur['_parent'] = parent
                cwd = os.path.join(cwd, dest)

            print(f'cd to={dest} new_cwd={cwd}')
            
        elif m.group('ls_cmd'):
            print('ls')
        elif m.group('dir'):
            dname = m.group('dir')
        elif m.group('file'):
            fname = m.group('file')
            size = int(m.group('size'))
            dcur['_size'] = dcur.get('_size', 0) + size


finalize_dir_size(dirs['/'])

part1 = sum([x for x in dir_sizes if x <= 100000])
print(f'part1: {part1}')


# part2
max_fs_size    = 70000000
needed_fs_size = 30000000

dir_sizes = sorted(dir_sizes)[::-1]
free_space = max_fs_size - dir_sizes[0]

old_size = 0
for size in dir_sizes:
    if free_space + size < needed_fs_size:
        break
    old_size = size
print(f'part2: {old_size}')

