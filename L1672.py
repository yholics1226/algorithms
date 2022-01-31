# [Richest Customer Wealth] https://leetcode.com/problems/richest-customer-wealth/

def maximumWealth(accounts):
    return max([sum(accounts[i]) for i in range(len(accounts))])
