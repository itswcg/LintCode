class Solution:
    # array 二维列表
    def Find(self, target, array):
        m = len(array)
        for i in range(m):
            n = len(array[i])
            for j in range(n):
                if array[i][j] == target:
                    return True
        return False
