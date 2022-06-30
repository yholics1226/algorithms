# [Queue Reconstruction by Height] https://leetcode.com/problems/queue-reconstruction-by-height/

def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    ans = []
    for p in people:
        ans.insert(p[1], p)
    return ans
