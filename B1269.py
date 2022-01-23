# [대칭 차집합] https://www.acmicpc.net/problem/1269

import sys
input = sys.stdin.readline
na, nb = map(int, input().split())
a = {*map(int, input().split())}
b = {*map(int, input().split())}
print(na + nb - 2 * len(a & b))
