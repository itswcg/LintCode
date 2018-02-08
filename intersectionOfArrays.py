class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):
        from functools import reduce
        res = reduce(lambda x, y: list(set(x) & set(y)), arrs)
        return len(res)
