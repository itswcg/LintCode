class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        i = len(A) - 1
        while i > 0:
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                return i
            i -= 1
