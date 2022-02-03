# [감소하는 수] https://www.acmicpc.net/problem/1038

from itertools import combinations
import sys
n = int(sys.stdin.readline())
nums = []
for i in range(1, 11):
    for comb in combinations(range(10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int(''.join(map(str, comb))))
    if len(nums) > n:
        nums.sort()
        print(nums[n])
        sys.exit(0)
print(-1)
