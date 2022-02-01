# [Best Time to Buy and Sell Stock] https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > buy:
            profit = max(profit, prices[i] - buy)
        else:
            buy = prices[i]
    return profit
