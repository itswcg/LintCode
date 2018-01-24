class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        count = 0
        while n > 1:
            n //= 5
            count += n
        return count


print(Solution().trailingZeros(10))
