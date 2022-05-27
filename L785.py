# [Is Graph Bipartite?] https://leetcode.com/problems/is-graph-bipartite/

# DFS
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
                return False
    return True

# BFS
from collections import deque
def isBipartite(graph):
    p = {}
    for i in range(len(graph)):
        if i not in p:
            p[i] = 0
            q = deque([i])
            while q:
                v = q.popleft()
                for nv in graph[v]:
                    if nv in p:
                        if p[nv] == p[v]:
                            return False
                    else:
                        p[nv] = 1 - p[v]
                        q.append(nv)
    return True
