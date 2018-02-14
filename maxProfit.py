class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0
        Min = prices[0]
        res = 0
        for p in prices:
            res = max(res, p - Min)
            Min = min(Min, p)
        return res
