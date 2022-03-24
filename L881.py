# [Boats to Save People] https://leetcode.com/problems/boats-to-save-people/

def numRescueBoats(people, limit):
    n = len(people)
    people.sort()
    lt, rt = 0, n-1
    while lt < rt:
        if people[lt] + people[rt] <= limit:
            n -= 1
            lt += 1
        rt -= 1
    return n
