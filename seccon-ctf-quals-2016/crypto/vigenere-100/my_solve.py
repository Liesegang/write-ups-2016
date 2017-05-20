#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import itertools

char_set = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + ['{', '}']

def reverse(c, k):
    return char_set[(char_set.index(c) - char_set.index(k)) % 28]

def decrypt(enc, key):
    res = ""
    for i, c in enumerate(enc):
        res += reverse(enc[i], key[i % len(key)])
    return res

p = "SECCON{???????????????????????????????????}"
c = "LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ"
plain_md5 = 'f528a6ab914c1ecf856a1d93103948fe'
key_len = 12

k = ""

for i in range(7):
    k += reverse(c[i], p[i])


for res in itertools.product(char_set, repeat=key_len - len(k)):
    key = k + "".join(res)
    plain = decrypt(c, key)
    md5 = hashlib.md5(plain.encode('utf-8')).hexdigest()

    if md5 == plain_md5:
        print("flag:\t", plain)
        print("key:\t", key)
        break
