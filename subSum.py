class Solution:
    """
    @param: : the given number
    @return: Sum of elements in subsets
    """

    def subSum(self, n):
        from itertools import combinations
        l = [i for i in range(1, n + 1)]
        res = []
        for i in range(1, n + 1):
            res.append(list(combinations(l, i)))
        return res


print(Solution().subSum(4))
