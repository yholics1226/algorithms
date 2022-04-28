# [Smallest String With Swaps] https://leetcode.com/problems/smallest-string-with-swaps/

# Union & Find
from collections import defaultdict
def smallestStringWithSwaps(s, pairs):
    unf = list(range(len(s)))
    def find(v):
        if v != unf[v]:
            unf[v] = find(unf[v])
        return unf[v]
    for a, b in pairs:
        fa, fb = find(a), find(b)
        if fa != fb:
            unf[fa] = fb
    igp = defaultdict(list)
    cgp = defaultdict(list)
    for i, c in enumerate(s):
        fi = find(i)
        igp[fi].append(i)
        cgp[fi].append(c)
    ans = [''] * len(s)
    for k in igp:
        igp[k].sort()
        cgp[k].sort()
        for i, c in zip(igp[k], cgp[k]):
            ans[i] = c
    return ''.join(ans)

# BFS
from collections import defaultdict
def smallestStringWithSwaps(s, pairs):
    n = len(s)
    graph = [[] for _ in range(n)]
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)
    seen = [False] * n
    d = defaultdict(list)
    p = list(range(n))
    for i in range(n):
        if seen[i]:
            continue
        seen[i] = True
        stack = [i]
        while stack:
            x = stack.pop()
            p[x] = i
            d[i].append(s[x])
            for y in graph[x]:
                if not seen[y]:
                    seen[y] = True
                    stack.append(y)
        d[i].sort(reverse=True)
    ans = []
    for i in range(n):
        ans.append(d[p[i]].pop())
    return ''.join(ans)
