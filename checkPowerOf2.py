class Solution:
    """
    @param: n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        return not n & (n-1) and n != 0
    # http://blog.csdn.net/guoziqing506/article/details/51602606
