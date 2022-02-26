# [음식 평론가] https://www.acmicpc.net/problem/1188

n, m = map(int, input().split())
def gcd(a, b):
    if a % b:
        return gcd(b, a % b)
    return b
print(m - gcd(n, m))
