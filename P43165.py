# [타겟 넘버] https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    def dfs(i, result):
        nonlocal answer
        if i == n:
            if result == target:
                answer += 1
        else:
            dfs(i+1, result + numbers[i])
            dfs(i+1, result - numbers[i])
    n = len(numbers)
    answer = 0
    dfs(0, 0)
    return answer

# using itertools
from itertools import product
def solution(numbers, target):
    s = list(map(sum, product(*[(x, -x) for x in numbers])))
    return s.count(target)
