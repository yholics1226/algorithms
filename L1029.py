# [Two City Scheduling] https://leetcode.com/problems/two-city-scheduling/

def twoCitySchedCost(costs):
    n = len(costs) // 2
    costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
    ans = a = b = 0
    for x, y in costs:
        if a == n:
            ans += y
        elif b == n:
            ans += x
        else:
            if x < y:
                ans += x
                a += 1
            else:
                ans += y
                b += 1
    return ans
