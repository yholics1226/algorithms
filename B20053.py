import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    print(min(ls), max(ls))
