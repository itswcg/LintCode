class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        n = len(triangle)
        res = 0
        for i in range(n - 2, -1, -1):
            l = len(triangle[i])
            for j in range(l):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])
        return triangle[0][0]


print(Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
