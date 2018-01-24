class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """

    def singleNumber(self, A):
        a = []
        for i in A:
            if i in a:
                a.remove(i)
            else:
                a.append(i)
        return a[0]


print(Solution().singleNumber([1, 2, 2, 1, 3, 4, 3]))
