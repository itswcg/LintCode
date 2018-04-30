class Solution:
    def LeftRotateString(self, s, n):
        return s[n:] + s[:n]
