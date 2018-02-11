class Solution:
    """
    @param k:
    @return: the sum of first k even-length palindrome numbers
    """

    def sumKEven(self, k):
        res = 0
        for i in range(1, k + 1):
            tmp = str(i) + str(i)[::-1]
            res += int(tmp)
        return res
