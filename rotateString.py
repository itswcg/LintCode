class Solution:
    """
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        if not str:
            return
        if not offset:
            return
        offset = offset % len(str)
        return str[len(str) - offset:len(str)] + str[:len(str) - offset]


print(Solution().rotateString("abcdefg", 2))
