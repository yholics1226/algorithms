# [배] https://www.acmicpc.net/problem/1092

# PyPy3 Accepted, Python3 TLE
import sys
input = sys.stdin.readline
n = int(input())
wlim = [*map(int, input().split())]
wlim.sort(reverse=True)
m = int(input())
bw = [*map(int, input().split())]
bw.sort(reverse=True)
if bw[0] > wlim[0]: 
    print(-1)
else:
    ans = 0
    while bw:
        ans += 1
        for wl in wlim:
            for i in range(len(bw)):
                if bw[i] <= wl:
                    del bw[i]
                    break
    print(ans)
