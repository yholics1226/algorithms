# [소수상근수] https://www.acmicpc.net/problem/9421

import sys, functools
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())

def isPrime(num):
    if num < 2:
        return False
    lim = int(num ** 0.5)
    for i in range(2, lim+1):
        if num % i == 0:
            return False
    return True

@functools.cache
def isHappy(num):
    res = 0
    while num:
        res += (num % 10) ** 2
        num //= 10
    if res == 1:
        return True
    if res in seen:
        return False
    seen.add(res)
    return isHappy(res)

for i in range(7, n+1):
    if isPrime(i):
        seen = {i}
        if isHappy(i):
            print(i)
