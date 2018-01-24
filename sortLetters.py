class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, chars):
        a = 0
        char = list(chars)
        for i in range(len(char)):
            if char[i].islower():
                char[i], char[a] = char[a], char[i]
                a += 1
        return ''.join(char)


print(Solution().sortLetters('abAcD'))
