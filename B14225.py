# [부분수열의 합] https://www.acmicpc.net/problem/14225

import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))
ch = [0] * sum(seq)
def dfs(s, ps):
    if s == n-1:
        ch[ps-1] = 1
        ch[seq[s]+ps-1] = 1
    else:
        dfs(s+1, ps)
        dfs(s+1, seq[s]+ps)
dfs(0, 0)
for i in range(len(ch)):
    if ch[i] == 0:
        print(i+1)
        sys.exit(0)
print(len(ch)+1)
