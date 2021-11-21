# [조이스틱] https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    n = len(name)
    answer = n - 1
    for lt in range(n-1):
        rt = lt + 1
        while rt < n and name[rt] == 'A':
            rt += 1
        re = min(lt, n - rt)
        answer = min(answer, lt + n - rt + re)
    for x in name:
        diff = ord(x) - ord('A')
        answer += min(diff, 26 - diff)
    return answer
