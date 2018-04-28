class Solution:
    def reOrderArray(self, array):
        return [i for i in array if i % 2 != 0] + [j for j in array if j % 2 == 0]
