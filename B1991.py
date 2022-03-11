# [트리 순회] https://www.acmicpc.net/problem/1991

import sys
input = sys.stdin.readline
n = int(input())
tree = {}
for _ in range(n):
    rt, lc, rc = input().split()
    tree[rt] = (lc, rc)
def preo(v):
    lc, rc = tree[v]
    print(v, end='')
    if lc != '.':
        preo(lc)
    if rc != '.':
        preo(rc)
def ino(v):
    lc, rc = tree[v]
    if lc != '.':
        ino(lc)
    print(v, end='')
    if rc != '.':
        ino(rc)
def posto(v):
    lc, rc = tree[v]
    if lc != '.':
        posto(lc)
    if rc != '.':
        posto(rc)
    print(v, end='')
preo('A')
print()
ino('A')
print()
posto('A')
