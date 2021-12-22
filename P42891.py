# [무지의 먹방 라이브] https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq
def solution(food_times, k):
    h = []
    n = len(food_times)
    for i in range(n):
        heapq.heappush(h, (food_times[i], i+1))
    answer = -1
    prev = 0
    while h:
        t = (h[0][0] - prev) * n
        if t <= k:
            k -= t
            prev, _ = heapq.heappop(h)
            n -= 1
        else:
            h.sort(key=lambda x: x[1])
            answer = h[k % n][1]
            break
    return answer
