class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        count = 0
        l = [str(x) for x in range(0, n + 1)]
        a = ''.join(l)
        return a.count(str(k))


print(Solution().digitCounts(1, 12))
