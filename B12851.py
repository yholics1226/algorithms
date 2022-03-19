# [숨바꼭질 2] https://www.acmicpc.net/problem/12851

from collections import deque, defaultdict
q = deque()
n, k = map(int, input().split())
if n == k:
    print(0)
    print(1)
    exit(0)
ans, cnt = float('inf'), 0
ch = [0] * 100001
q.append(n)
ch[n] = 1
L = 1
while q and L <= ans:
    length = len(q)
    tmp = defaultdict(int)
    for i in range(length):
        x = q.popleft()
        for nx in [x-1, x+1, 2*x]:
            if nx == k:
                ans = L
                cnt += ch[x]
            elif 0 <= nx <= 100000:
                if ch[nx] == 0 and nx not in tmp:
                    q.append(nx)
                tmp[nx] += ch[x]
    L += 1
    for key, val in tmp.items():
        ch[key] += val
print(ans)
print(cnt)

# another solution (faster)
n, k = map(int, input().split())
d = {n: 1}
seen = set()
ans = 0
while d:
    nd = {}
    for x in d:
        if x == k:
            print(ans)
            print(d[k])
            exit(0)
        if x in seen:
            continue
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx <= 100000:
                if nx in nd:
                    nd[nx] += d[x]
                else:
                    nd[nx] = d[x]
        seen.add(x)
    ans += 1
    d = nd
