#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('kek.txt') as f:
    source = f.readline().split()

data = ""

for b in source:
    if b.startswith('KEK'):
        data += '0' * b.count('!')
    else:
        data += '1' * b.count('!')

data = int(data, 2)

print(data.to_bytes((data.bit_length() + 7) // 8, byteorder='big'))

