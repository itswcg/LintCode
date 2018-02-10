class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """

    def isPalindrome(self, n):
        if n == 0:
            return True
        a = str(bin(n))[2:]
        if a == a[::-1]:
            return True
        else:
            return False


print(Solution().isPalindrome(5))
