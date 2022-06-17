# [기능개발] https://programmers.co.kr/learn/courses/30/lessons/42586

import math
def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    cnt, day = 0, 1
    for d in days:
        if day < d:
            if cnt != 0:
                answer.append(cnt)
            day = d
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer

# refactor
def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        if not answer or answer[-1][0] < -((p-100)//s):
            answer.append([-((p-100)//s), 1])
        else:
            answer[-1][1] += 1
    return [x[1] for x in answer]
