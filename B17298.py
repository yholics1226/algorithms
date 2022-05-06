# [오큰수] https://www.acmicpc.net/problem/17298

n = int(input())
a = [*map(int, input().split())]
s = []
nge = [-1] * n
for i in range(n):
    while s and a[s[-1]] < a[i]:
        nge[s.pop()] = a[i]
    s.append(i)
print(*nge)
