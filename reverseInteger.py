class Solution:
    """
    @param: n: the integer to be reversed
    @return: the reversed integer
    """

    def reverseInteger(self, n):
        num = abs(n)
        res = []
        while num > 0:
            res.append(num % 10)
            num //= 10
        a = 0
        for i in range(len(res)):
            a = a * 10 + res[i]
        if a > 0x7fffffff:
            return 0
        else:
            if n > 0:
                return a
            else:
                return -a
