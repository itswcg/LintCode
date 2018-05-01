class Solution:
    def Sum_Solution(self, n):
        from functools import reduce
        list = [i for i in range(1, n+1)]
        return reduce(lambda x, y: x+y, list)
