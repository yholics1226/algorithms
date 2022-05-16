# [Network Delay Time] https://leetcode.com/problems/network-delay-time/

import heapq
def networkDelayTime(times, n, k):
    dist = [0] + [700000] * n
    graph = [[] for _ in range(n+1)]
    for u, v, w in times:
        graph[u].append([v, w])
    tree = []
    dist[k] = 0
    heapq.heappush(tree, [0, k])
    while tree:
        d, v = heapq.heappop(tree)
        if d > dist[v]:
            continue
        for nv, nd in graph[v]:
            if d + nd < dist[nv]:
                dist[nv] = d + nd
                heapq.heappush(tree, [dist[nv], nv])
    for i in range(1, n+1):
        if dist[i] == 700000:
            return -1
    return max(dist)
