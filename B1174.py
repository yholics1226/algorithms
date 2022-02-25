# [줄어드는 수] https://www.acmicpc.net/problem/1174

from itertools import combinations
n = int(input())
nums = []
for i in range(1, 11):
    for comb in combinations('9876543210', i):
        comb = list(comb)
        nums.append(int(''.join(comb)))
nums.sort()
if n > len(nums):
    print(-1)
else:
    print(nums[n-1])

# w/o itertools
n = int(input())
if n > 1023:
    print(-1)
else:
    nums = list(range(10))
    for num in nums:
        for i in range(num % 10):
            nums.append(num * 10 + i)
    print(nums[n-1])
