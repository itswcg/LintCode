class Solution:
    def FindGreatestSumOfSubArray(self, array):
        i, _sum, sum = 0, 0, -0xffffff
        while i < len(array):
            _sum += array[i]
            if _sum > sum:
                sum = _sum
            if _sum < 0:
                _sum = 0
            i += 1
        return sum
