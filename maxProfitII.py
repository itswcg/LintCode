class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        sum = 0
        if prices is None:
            return sum
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                sum += prices[i + 1] - prices[i]
        return sum
