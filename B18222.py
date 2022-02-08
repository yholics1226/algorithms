# [투에-모스 문자열] https://www.acmicpc.net/problem/18222

import sys
k = int(sys.stdin.readline())
def thue(n):
    if n == 0:
        return 0
    if n % 2:
        return 1 - thue(n//2)
    else:
        return thue(n//2)
print(thue(k-1))
