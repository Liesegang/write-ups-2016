#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3000))

def fixmatrix(matrixa, matrixb):
    out = [[0 for x in range(3)] for x in range(3)]	
    for rn in range(3):
        for cn in range(3):
            out[rn][cn] = (int(matrixa[cn][rn])|int(matrixb[cn][rn]))&~(int(matrixa[cn][rn])&int(matrixb[cn][rn]))
    return(out)


def printmat(matrix):
    for row in matrix:
        for value in row:
            print(value," ", end='')
        print()
    print()

def genBlockMatrix(s):
    outm = [[[7 for x in range(3)] for x in range(3)] for x in range(len(s)//9)]
    for matnum in range(0,len(s)//9):
        for y in range(0,3):
            for x in range(0,3):
                outm[matnum][y][x] = s[(matnum*9)+x+(y*3)]
    return(outm)

def makemat(l):
    res = []
    for i in l:
        res2 = []
        s = i.split()
        for j in s:
            res2.append(int(j))
        res.append(res2)
    return res

def mat2str(mat):
    res = []
    for raw in mat:
        for item in raw:
            res.append(str(item))
    return ",".join(res)

s.send(b'\n')
data = s.recv(2048)
data = data.decode('utf-8')
s.close()
data = data.split('\n')

seed = data[0][6:]
out = makemat(data[1:4])

key = genBlockMatrix([ord(c) for c in seed])

b = fixmatrix(out, key[1])
a = fixmatrix(b, key[0])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3000))
s.send(mat2str(a).encode('utf-8'))
s.send(b'\n')
data = s.recv(2048)
print(data.decode('utf-8'))
