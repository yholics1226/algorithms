# [스타트와 링크] https://www.acmicpc.net/problem/14889

import sys
input = sys.stdin.readline
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
r = n // 2
res = [0] * r

def DFS(L, s):
    global answer
    if L == r:
        start = link = 0
        tmp = list(set([i for i in range(1, n+1)]) - set(res))
        for i in range(r):
            for j in range(i+1,r):
                start += (nums[res[i]-1][res[j]-1] + nums[res[j]-1][res[i]-1])
                link += (nums[tmp[i]-1][tmp[j]-1] + nums[tmp[j]-1][tmp[i]-1])
        diff = abs(start - link)
        answer = min(answer, diff)
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)
            
DFS(0, 1)
print(answer)
