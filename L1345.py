# [Jump Game 4] https://leetcode.com/problems/jump-game-iv/

from collections import defaultdict, deque
def minJumps(arr):
    n = len(arr)
    if n == 1:
        return 0
    nH = defaultdict(list)
    for i, x in enumerate(arr):
        nH[x].append(i)
    dist = [-1] * n
    dist[-1] = 0
    Q = deque([n-1])
    visit = {n-1}
    while Q:
        x = Q.popleft()
        for y in nH[arr[x]]:
            if y == 0:
                return dist[x] + 1
            if y not in visit:
                dist[y] = dist[x] + 1
                Q.append(y)
                visit.add(y)
        y = x + 1
        if y < n and y not in visit:
            dist[y] = dist[x] + 1
            Q.append(y)
            visit.add(y)
        y = x - 1
        if y == 0:
            return dist[x] + 1
        if y > 0 and y not in visit:
            dist[y] = dist[x] + 1
            Q.append(y)
            visit.add(y)
    return -1
