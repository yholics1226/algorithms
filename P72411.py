# [메뉴 리뉴얼] https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        sH = Counter()
        for x in orders:
            segs = combinations(sorted(x), k)
            sH += Counter(segs)
        if sH:
            cmax = max(sH.values())
            if cmax > 1:
                for x in sH:
                    if sH[x] == cmax:
                        answer.append(''.join(x))
    return sorted(answer)
