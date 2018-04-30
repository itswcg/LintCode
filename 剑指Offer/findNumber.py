class Solution:
    def FindNumbersWithSum(self, array, tsum):
        from functools import reduce
        res = []
        for i in range(len(array)-1):
            for j in range(1, len(array)):
                if array[i] + array[j] == tsum:
                    res.append([array[i], array[j]])
        if len(res) == 0: return res
        return res[0]
