class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        if n is None:
            return False
        tmp = 0
        while tmp != 1 and tmp != 4:
            tmp = 0
            n = str(n)
            for i in n:
                tmp += int(i) ** 2
            if tmp == 1:
                return True
            n = tmp
        if tmp == 1:
            return True
        return False
# http://blog.csdn.net/yurenguowang/article/details/76849974


print(Solution().isHappy(19))
