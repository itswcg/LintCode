class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Their smallest difference.
    """

    def smallestDifference(self, A, B):
        A.sort()
        B.sort()
        i, j, ret = 0, 0, 2147483647
        while i < len(A) and j < len(B):
            ret = min(ret, abs(A[i] - B[j]))
            if A[i] > B[j]:
                j += 1
            elif A[i] < B[j]:
                i += 1
            elif A[i] == B[j]:
                ret = 0
                break
        return ret


print(Solution().smallestDifference([3, 4, 6, 7], [2, 3, 8, 9]))
