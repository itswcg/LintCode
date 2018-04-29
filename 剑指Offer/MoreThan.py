class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        res = len(numbers)//2
        if numbers.count(numbers[res]) > res:
            return numbers[res]
        return 0
