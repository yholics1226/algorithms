# [소수 구하기] https://www.acmicpc.net/problem/1929

m, n = map(int, input().split())
prime = [True] * 1000001
prime[1] = False
for i in range(2, 500001):
    if prime[i]:
        for j in range(2*i, 1000001, i):
            prime[j] = False
for i in range(m, n+1):
    if prime[i]:
        print(i)
