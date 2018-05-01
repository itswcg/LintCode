class Solution:
    # s字符串
    def isNumeric(self, s):
        try:
            p = float(s)
            return True
        except:
            return False
