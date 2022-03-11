# [소수 만들기] https://programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    def primeSum(s, k, i):
        nonlocal answer
        if k == 3:
            if isPrime(s):
                answer += 1
        else:
            for j in range(i, n):
                primeSum(s + nums[j], k+1, j+1)
    answer = 0
    n = len(nums)
    primeSum(0, 0, 0)
    return answer

# using itertools
from itertools import combinations
def solution(nums):
    def isPrime(num):
        if num < 2:
            return 0
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return 0
        return 1
    return sum(isPrime(sum(comb)) for comb in combinations(nums, 3))
