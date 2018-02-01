class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """

    def addDigits(self, num):
        tmp = 0
        for i in str(num):
            tmp += int(i)
        if len(str(tmp)) != 1:
            return self.addDigits(tmp)
        else:
            return tmp


print(Solution().addDigits(38))
