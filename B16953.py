# [A → B] https://www.acmicpc.net/problem/16953

a, b = map(int, input().split())
n = 1
while a < b:
    n += 1
    if b % 10 == 1:
        b //= 10
    elif b % 2:
        break
    else:
        b >>= 1
print(n if a == b else -1)
