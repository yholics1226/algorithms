# [이분 그래프] https://www.acmicpc.net/problem/1707

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def isBipartite(graph):
    partition = {}
    def dfs(v):
        for nv in graph[v]:
            if nv in partition:
                if partition[nv] == partition[v]:
                    return False
            else:
                partition[nv] = 1 - partition[v]
                if not dfs(nv):
                    return False
        return True
    for i in range(len(graph)):
        if i not in partition:
            partition[i] = 0
            if not dfs(i):
                return 'NO'
    return 'YES'
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(isBipartite(graph))
