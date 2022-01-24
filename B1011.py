# [Fly me to the Alpha Centauri] https://www.acmicpc.net/problem/1011

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    d, k = y - x, 0
    while True:
        k += 1
        d -= k
        if d <= 0:
            print(k * 2 - 1)
            break
        d -= k
        if d <= 0:
            print(k * 2)
            break
            
# another solution
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = y - x
    sd = d ** 0.5
    cnt = int(sd) * 2 - 1
    if sd % 1 == 0:
        print(cnt)
    elif sd % 1 < 0.5:
        print(cnt + 1)
    else:
        print(cnt + 2)
