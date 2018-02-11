class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """

    def singleNumberII(self, A):
        ones = 0
        twos = 0
        for num in A:
            ones = (ones ^ num) & (~twos)
            twos = (twos ^ num) & (~ones)
        return ones
