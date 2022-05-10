# [뱀과 사다리 게임] https://www.acmicpc.net/problem/16928

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = {i: i for i in range(1, 101)}
for _ in range(n+m):
    x, y = map(int, input().split())
    board[x] = y
ch = [True] * 2 + [False] * 99
q = deque([(1, 0)])
while q:
    x, c = q.popleft()
    if x == 100:
        print(c)
        break
    for y in range(x+1, min(x+7, 101)):
        z = board[y]
        if not ch[z]:
            ch[z] = True
            q.append((z, c+1))
