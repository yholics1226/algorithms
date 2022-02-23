# [팔] https://www.acmicpc.net/problem/1105

l, r = input().split()
if len(l) < len(r):
    print(0)
else:
    c = i = 0
    while i < len(l) and l[i] == r[i]:
        c += l[i] == '8'
        i += 1
    print(c)
