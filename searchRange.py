class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        if target not in A:
            return [-1, -1]
        index1 = A.index(target)
        if index1 == len(A) - 1:
            return [index1, index1]
        else:
            B = A[::-1]
            index2 = B.index(target)
            return [index1, len(A) - index2 - 1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
