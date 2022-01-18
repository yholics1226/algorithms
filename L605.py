# [Can Place Flowers] https://leetcode.com/problems/can-place-flowers/

def canPlaceFlowers(flowerbed, n):
    m = len(flowerbed)
    prev = -2
    for i in range(m):
        if flowerbed[i]:
            n -= (i - prev - 2) // 2
            if n <= 0:
                return True
            prev = i
    if flowerbed[-1] == 0:
        n -= (m - prev - 1) // 2
    return n <= 0
