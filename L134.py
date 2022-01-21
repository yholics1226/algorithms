# [Gas Station] https://leetcode.com/problems/gas-station/

def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start, tank = 0, 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start, tank = i+1, 0
    return start
