# [N과 M (4)] https://www.acmicpc.net/problem/15652

n, m = map(int, input().split())
res = []
def dfs(s):
    if len(res) == m:
        print(*res)
    else:
        for i in range(s, n+1):
            res.append(i)
            dfs(i)
            res.pop()
dfs(1)
