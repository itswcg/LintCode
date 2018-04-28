class Solution:
    def NumberOf1(self, n):
        return sum([n >> i & 1 for i in range(32)])

# >> 右移 & 一样的话返回1
