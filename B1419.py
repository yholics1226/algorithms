# [등차수열의 합] https://www.acmicpc.net/problem/1419

# accepted in PyPy3, TLE in Python3
l, r, k = (int(input()) for _ in range(3))
cnt = 0
if k == 2:  # 2x + d
    cnt = r - max(l, 3) + 1
elif k == 3:    # 3x + 3d
    l = max(l, 6)
    for i in range(l, r+1):
        if i % 3 == 0:
            cnt += 1
elif k == 4:    # 4x + 6d
    l = max(l, 10)
    for i in range(l, r+1):
        if i % 2 == 0:
            cnt += 1
    if cnt and l <= 12 <= r:
        cnt -= 1
else:   # 5x + 10d
    l = max(l, 15)
    for i in range(l, r+1):
        if i % 5 == 0:
            cnt += 1
print(cnt)
