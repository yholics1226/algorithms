# [숨바꼭질 3] https://www.acmicpc.net/problem/13549

from collections import deque
n, k = map(int, input().split())
if n >= k:
    print(n-k)
else:
    ch = [False] * 100001
    q = deque([(n, 0)])
    ch[n] = True
    while q:
        x, t = q.popleft()
        if x == k:
            print(t)
            break
        if x <= 50000 and not ch[2*x]:
            q.appendleft((2*x, t))
            ch[2*x] = True
        if x > 0 and not ch[x-1]:
            q.append((x-1, t+1))
            ch[x-1] = True
        if x < 100000 and not ch[x+1]:
            q.append((x+1, t+1))
            ch[x+1] = True

# another solution (faster)
n, k = map(int, input().split())
def sol(n, k):
    if n >= k:
        return n-k
    if n == 0:
        return 1 + sol(1, k)
    if k % 2:
        return 1 + min(sol(n, k-1), sol(n, k+1))
    else:
        return min(sol(n, k//2), k-n)
print(sol(n, k))
