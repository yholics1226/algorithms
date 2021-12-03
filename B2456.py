# [나는 학급회장이다] https://www.acmicpc.net/problem/2456

# method 1
import sys, collections
input = sys.stdin.readline
n = int(input())
d = collections.defaultdict(int)
for _ in range(n):
    a, b, c = map(int, input().split())
    d[(1, a)] += 1
    d[(2, b)] += 1
    d[(3, c)] += 1
s = [0, 0, 0]
for i in range(1, 4):
    s[0] += d[(1, i)] * i
    s[1] += d[(2, i)] * i
    s[2] += d[(3, i)] * i
smax = max(s)
tmp = [0, 0, 0]
win = 0
cnt = 0
for i in range(3):
    if s[i] == smax:
        win = i+1
        cnt += 1
        tmp[i] += 1
if cnt != 1:
    for i in range(3):
        tmp[i] += d[(i+1, 3)]
    tmax = max(tmp)
    cnt = 0
    for i in range(3):
        if tmp[i] == tmax:
            win = i+1
            cnt += 1
    if cnt != 1:
        win = 0
print(win, smax)

# method 2 - sort
import sys
input = sys.stdin.readline
n = int(input())
candi = [{'num': i, 1: 0, 2: 0, 3: 0, 'score': 0} for i in range(1, 4)]
for _ in range(n):
    a, b, c = map(int, input().split())
    candi[0][a] += 1
    candi[0]['score'] += a
    candi[1][b] += 1
    candi[1]['score'] += b
    candi[2][c] += 1
    candi[2]['score'] += c
candi.sort(key=lambda x: (x['score'], x[3], x[2]))
a, b = candi[2], candi[1]
if a['score'] == b['score'] and a[3] == b[3]:
    print(0, a['score'])
else:
    print(a['num'], a['score'])
