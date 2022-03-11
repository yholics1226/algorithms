# [완주하지 못한 선수] https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter
def solution(participant, completion):
    pH = Counter(participant)
    cH = Counter(completion)
    for x in pH:
        if pH[x] != cH[x]:
            return x

# another solution (slower)
from collections import Counter
def solution(participant, completion):
    res = Counter(participant) - Counter(completion)
    return list(res.keys())[0]

# using sort (slower)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('')
    for p, c in zip(participant, completion):
        if p != c:
            return p
