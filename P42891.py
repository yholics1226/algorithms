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

# another solution
def solution(food_times, k):
    n = len(food_times)
    sorted_times = [0] + sorted(food_times)
    for i in range(1, n+1):
        t = (sorted_times[i] - sorted_times[i-1]) * n
        if k >= t:
            k -= t
            n -= 1
        else:
            k %= n
            for j in range(len(food_times)):
                if food_times[j] >= sorted_times[i]:
                    if k == 0:
                        return j+1
                    k -= 1
    return -1
