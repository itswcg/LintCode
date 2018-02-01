class Solution:
    """
    @param: num: An integer
    @return: true if num is an ugly number or false
    """

    def isUgly(self, num):
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        if num == 1:
            return True
        else:
            return False


print(Solution().isUgly(14))
