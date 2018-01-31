class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        start, end = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while start <= end:
            mid1 = (start + end) // 2
            if matrix[mid1][0] == target:
                return True
            else:
                if target < matrix[mid1][0]:
                    end = mid1 - 1
                else:
                    start = mid1 + 1
        # start-1 因为 target > matrix[mid1][0] start=mid1+1
        while left <= right:
            mid2 = (left + right) // 2
            if matrix[start - 1][mid2] == target:
                return True
            else:
                if target < matrix[start - 1][mid2]:
                    right = mid2 - 1
                else:
                    left = mid2 + 1
        return False
