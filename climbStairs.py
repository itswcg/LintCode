class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        for i in range(3, n + 1):
            res = a + b
            a = b
            b = res
        return res
