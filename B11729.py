# [하노이 탑 이동 순서] https://www.acmicpc.net/problem/11729

def hanoi(n, x, y, z):
    if n > 0:
        hanoi(n-1, x, z, y)
        ans.append((x, z))
        hanoi(n-1, y, x, z)
n = int(input())
ans = []
hanoi(n, 1, 2, 3)
print(len(ans))
for a, b in ans:
    print(a, b)

# refactor
def hanoi(n, x, y, z):
    if n == 1:
        print(x, z)
    else:
        hanoi(n-1, x, z, y)
        print(x, z)
        hanoi(n-1, y, x, z)
'''
Note:
    Let A(n) be the number of moves for n disks.
    By the definition of hanoi(), notice A(n+1) = 2 * A(n) + 1
    This implies A(n) = 2 ^ n - 1
'''
n = int(input())
print(2**n-1)
hanoi(n, 1, 2, 3)
