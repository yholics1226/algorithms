# [이진 검색 트리] https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**8)
pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break
def dfs(s, e):
    if e == s:
        print(pre[s])
    elif s < e:
        for i in range(s+1, e+1):
            if pre[s] < pre[i]:
                rc = i
                break
        else:
            rc = e+1
        dfs(s+1, rc-1)
        dfs(rc, e)
        print(pre[s])
dfs(0, len(pre)-1)
