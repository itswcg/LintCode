class Solution:
    """
    @param: n: n
    @param: k: the k th permutation
    @return: return the k-th permutation
    """

    def getPermutation(self, n, k):
        from itertools import permutations
        from functools import reduce
        l = [i for i in range(1, n + 1)]
        res = list(permutations(l))
        r = reduce(lambda x, y: 10 * x + y, res[k - 1])
        return str(r)


print(Solution().getPermutation(3, 4))
