# [Container With Most Water] https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    answer = 0
    lt = 0
    rt = len(height) - 1
    while 1:
        answer = max(answer, min(height[lt], height[rt]) * (rt - lt))
        if height[lt] < height[rt]:
            for i in range(lt+1, rt):
                if height[lt] < height[i]:
                    lt = i
                    break
            else:
                break
        else:
            for j in range(rt-1, lt, -1):
                if height[rt] < height[j]:
                    rt = j
                    break
            else:
                break
    return answer
