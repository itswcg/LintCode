class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        tinput.sort()
        if k > len(tinput):
            return []
        return tinput[:k]
