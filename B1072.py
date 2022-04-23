# [게임] https://www.acmicpc.net/problem/1072

x, y = map(int, input().split())
z = 100 * y // x
if z >= 99:
    print(-1)
else:
    lt, rt, ans = 0, x, x
    while lt <= rt:
        mid = (lt + rt) // 2
        if 100 * (y + mid) // (x + mid) > z:
            ans = mid
            rt = mid - 1
        else:
            lt = mid + 1
    print(ans)
