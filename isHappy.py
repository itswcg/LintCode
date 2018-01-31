class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        from functools import reduce
        num = []
        while True:
            num.append(n % 10)
            n //= 10


print(Solution().isHappy(19))
