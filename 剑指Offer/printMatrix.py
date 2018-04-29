class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for i in matrix:
                    res.append(i.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for j in matrix[::-1]:
                    res.append(j.pop(0))
        return res
