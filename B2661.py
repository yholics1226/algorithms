# [좋은수열] https://www.acmicpc.net/problem/2661

import sys
n = int(sys.stdin.readline())

def isGood(seq):
    rt = len(seq)
    k = 1
    lt = rt - 1
    while lt-k >= 0:
        if seq[lt:rt] == seq[lt-k:lt]:
            return 0
        k += 1
        lt -= 1
    return 1

def DFS(x):
    if len(x) == n:
        print(x)
        sys.exit(0)
    else:
        for y in ['1', '2', '3']:
            if x[-1] != y and isGood(x+y):
                DFS(x+y)

DFS('1')
