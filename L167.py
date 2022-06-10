# [Two Sum II - Input Array Is Sorted] https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# two pointers
def twoSum(numbers, target):
    lt, rt = 0, len(numbers) - 1
    while lt < rt:
        s = numbers[lt] + numbers[rt]
        if s == target:
            return [lt+1, rt+1]
        elif s < target:
            lt += 1
        else:
            rt -= 1

# hash map
def twoSum(numbers, target):
    d = {}
    for i, n in enumerate(numbers):
        m = target - n
        if m in d:
            return [d[m], i + 1]
        d[n] = i + 1
