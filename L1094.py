# [Car Pooling] https://leetcode.com/problems/car-pooling/

import heapq
def carPooling(trips, capacity):
    trips = sorted(trips, key=lambda x: x[1])
    car = [(0, 0)]
    for n, f, t in trips:
        while car:
            tmp = heapq.heappop(car)
            if f >= tmp[0]:
                capacity += tmp[1]
            else:
                heapq.heappush(car, tmp)
                break
        if n > capacity:
            return False
        else:
            heapq.heappush(car, (t, n))
            capacity -= n
    return True

# another solution (w/o sorting)
def carPooling(trips, capacity):
    nums = [0] * 1001
    for n, f, t in trips:
        nums[f] += n
        nums[t] -= n
    cnt = 0
    for num in nums:
        cnt += num
        if cnt > capacity:
            return False
    return True
