# [미술가 미미] https://www.acmicpc.net/problem/20950

# accepted in pypy3, but time limit exceeded in python3
import sys
input = sys.stdin.readline
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
gom = list(map(int, input().split()))
ans = 1000
m = min(n, 7)
def diff(mun):
    res = 0
    for i in range(3):
        res += abs(gom[i] - mun[i])
    return res
def mix(s, k, lst):
    global ans
    if k < 2:
        for i in range(s, n):
            mix(i+1, k+1, lst + nums[i])
    elif k <= m:
        mun = [0, 0, 0]
        for i in range(3):
            for j in range(k):
                mun[i] += lst[i+3*j]
            mun[i] //= k
        ans = min(ans, diff(mun))
        for i in range(s, n):
            mix(i+1, k+1, lst + nums[i])
mix(0, 0, [])
print(ans)

# python3 acceepted
import sys
input = sys.stdin.readline
n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
gom = [*map(int, input().split())]
ans = 1000
def solve(c, k, s, r, g, b):
    global ans
    if c == k:
        diff = abs(r//k-gom[0]) + abs(g//k-gom[1]) + abs(b//k-gom[2])
        ans = min(ans, diff)
        return
    for i in range(s, n):
        solve(c+1, k, i+1, r+nums[i][0], g+nums[i][1], b+nums[i][2])
for k in range(2, min(8, n+1)):
    solve(0, k, 0, 0, 0, 0)
print(ans)
