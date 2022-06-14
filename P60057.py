# [문자열 압축] https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = n = len(s)
    for i in range(1, n//2 + 1):
        cnt = 0
        prev = s[:i]
        num = 1
        for j in range(i, n, i):
            curr = s[j:j+i]
            if prev == curr:
                num += 1
            else:
                cnt += i
                if num > 1:
                    cnt += len(str(num))
                prev = curr
                num = 1
        cnt += len(curr)
        if num > 1:
            cnt += len(str(num))
        answer = min(answer, cnt)
    return answer
