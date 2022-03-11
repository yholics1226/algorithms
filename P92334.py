# [신고 결과 받기] https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    d = defaultdict(set)
    for rep in report:
        x, y = rep.split()
        d[y].add(x)
    cnt = defaultdict(int)
    for y in d:
        if len(d[y]) >= k:
            for x in d[y]:
                cnt[x] += 1
    for x in id_list:
        answer.append(cnt[x])
    return answer
