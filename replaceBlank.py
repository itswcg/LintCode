class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """

    def replaceBlank(self, string, length):
        return len(string.replace(' ', '%20'))


print(Solution().replaceBlank("Mr John Smith", 13))
