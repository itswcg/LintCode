class Solution:
    """
    @param: s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        a = 'abcdefghijklmnopqrstuvwxyz'
        b = '1234567890'
        ss = []
        for i in s.lower():
            if i in a or i in b:
                ss.append(i)
        if ss == ss[::-1]:
            return True
        else:
            return False


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
