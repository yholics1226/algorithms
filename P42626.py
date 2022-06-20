# [더 맵게] https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        f1 = heapq.heappop(scoville)
        if f1 >= K:
            return answer
        f2 = heapq.heappop(scoville)
        heapq.heappush(scoville, f1 + f2 * 2)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer
