class Solution:
    """
    @param: : the given number
    @return: whether whether there're two integers
    """

    def checkSumOfSquareNumbers(self, num):
        l = []
        a = 0
        for i in range(num + 1):
            a += i * i
            l.append(a)
        if num < 0:
            return False
        if num in l:
            return True


print(Solution().checkSumOfSquareNumbers(5))
